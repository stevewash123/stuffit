// StuffIt Page Saver: save the rendered source of the current tab.
// 1) POST to the local receiver (receiver.py) which writes into the StuffIt folder.
// 2) If it is not running, download into Downloads/StuffIt-pages/<host>/ instead.
const DOC_URL = /\.(pdf|docx?|rtf)($|[?#])/i;
const RECEIVER = "http://127.0.0.1:8791/save";

const clean = (s, max = 80) => (String(s || "").replace(/[^A-Za-z0-9._-]+/g, "_").replace(/^_+|_+$/g, "").slice(0, max)) || "page";

function stamp() {
  const d = new Date(), p = (n) => String(n).padStart(2, "0");
  return `${d.getFullYear()}${p(d.getMonth() + 1)}${p(d.getDate())}-${p(d.getHours())}${p(d.getMinutes())}${p(d.getSeconds())}`;
}

async function badge(tabId, text, color) {
  await chrome.action.setBadgeBackgroundColor({ color, tabId });
  await chrome.action.setBadgeText({ text, tabId });
  setTimeout(() => chrome.action.setBadgeText({ text: "", tabId }), 4000);
}

async function pageOf(tabId) {
  const [r] = await chrome.scripting.executeScript({
    target: { tabId },
    func: () => ({
      url: location.href, title: document.title, html: document.documentElement.outerHTML,
      pdfs: [...new Set([...document.querySelectorAll("a[href]")].map((a) => a.href).filter((h) => /^https?:/i.test(h) && /\.(pdf|docx?|rtf)($|[?#])/i.test(h)))]
    })
  });
  return r.result;
}

const isPdfUrl = (u) => DOC_URL.test(u);   // a PDF or Word document

// Fetch a PDF or Word document and hand it to the receiver (or Downloads). Skips anything that is not really one:
// the first bytes must match the type the address claims (a login page saved as ".pdf" is refused).
const MAGIC = { pdf: [0x25, 0x50, 0x44, 0x46], docx: [0x50, 0x4b, 0x03, 0x04], doc: [0xd0, 0xcf, 0x11, 0xe0], rtf: [0x7b, 0x5c, 0x72, 0x74] };
async function savePdf(url, host) {
  const base = decodeURIComponent(new URL(url).pathname.split("/").pop() || "document");
  const ext = (base.match(/\.(pdf|docx?|rtf)$/i) || [, "pdf"])[1].toLowerCase();
  const name = clean(base).replace(/\.(pdf|docx?|rtf)$/i, "") + "." + ext;
  const res = await fetch(url, { credentials: "include" });
  if (!res.ok) throw new Error("HTTP " + res.status);
  const bytes = new Uint8Array(await res.arrayBuffer());
  if (!MAGIC[ext].every((v, i) => bytes[i] === v)) throw new Error("not a real ." + ext + " file");
  try {
    const r = await fetch(RECEIVER.replace("/save", "/save-file"), {
      method: "POST", headers: { "content-type": "application/octet-stream", "x-host": host, "x-name": name, "x-url": encodeURIComponent(url) }, body: bytes
    });
    if (!r.ok) throw new Error("HTTP " + r.status);
    return (await r.json()).path;
  } catch (e) {
    await chrome.downloads.download({ url, filename: `StuffIt-pages/${host}/${name}`, conflictAction: "uniquify" });
    return `Downloads/StuffIt-pages/${host}/${name}`;
  }
}

async function save(tab, note = "") {
  // A tab that is itself a PDF has no source to save: save the file.
  if (isPdfUrl(tab.url || "")) {
    return { where: await savePdf(tab.url, clean(new URL(tab.url).host)), pdfs: 1, failed: [] };
  }
  const page = await pageOf(tab.id);
  const noteLine = note.trim() ? `\n     note: ${note.trim().replace(/-{2,}>?/g, "-").replace(/\s*\n\s*/g, " ")}` : "";
  const meta = `<!-- StuffIt saved source\n     url: ${page.url}\n     title: ${page.title}\n     saved: ${new Date().toISOString()}${noteLine} -->\n`;
  const html = meta + page.html;
  const host = clean(new URL(page.url).host);
  const name = `${stamp()}_${clean(page.title)}.html`;

  try {
    const res = await fetch(RECEIVER, {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ url: page.url, title: page.title, host, name, html })
    });
    if (!res.ok) throw new Error("HTTP " + res.status);
    const where = (await res.json()).path;
    const pdf = await savePdfs(page.pdfs, host);
    return { where, ...pdf };
  } catch (e) {
    if (e.message === "pdfs") throw e;
    // receiver not running: fall back to the Downloads folder (a data URL: service workers have no blob URLs)
    const dataUrl = "data:text/html;charset=utf-8," + encodeURIComponent(html);
    await chrome.downloads.download({ url: dataUrl, filename: `StuffIt-pages/${host}/pagesource/${name}`, conflictAction: "uniquify", saveAs: false });
    return { where: `Downloads/StuffIt-pages/${host}/pagesource/${name}`, ...(await savePdfs(page.pdfs, host)) };
  }
}

async function savePdfs(urls, host) {
  let pdfs = 0; const failed = [];
  for (const u of urls || []) {
    try { await savePdf(u, host); pdfs++; } catch (e) { failed.push(u + " (" + e.message + ")"); }
  }
  return { pdfs, failed };
}

async function run(tab, note) {
  try {
    const r = await save(tab, note);
    console.log("Saved", r.where, r.pdfs + " PDF(s)", r.failed);
    if (r.failed.length) console.warn("PDFs not saved:", r.failed);
    await badge(tab.id, r.pdfs ? "+" + r.pdfs : "OK", r.failed.length ? "#ef6c00" : "#2e7d32");
    return { ok: true, where: r.where, pdfs: r.pdfs, failed: r.failed };
  } catch (e) {
    console.error("Save failed", e);
    await badge(tab.id, "ERR", "#c62828");
    return { ok: false, error: String(e.message || e) };
  }
}

// The popup (toolbar click / Alt+Shift+S) asks for a save with an optional note.
chrome.runtime.onMessage.addListener((msg, _sender, sendResponse) => {
  if (!msg || msg.type !== "save") return false;
  chrome.tabs.get(msg.tabId).then((tab) => run(tab, msg.note || "")).then(sendResponse);
  return true;
});

// Alt+Shift+Q: save straight away, no note.
chrome.commands.onCommand.addListener(async (command) => {
  if (command !== "quick-save") return;
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (tab) await run(tab, "");
});
