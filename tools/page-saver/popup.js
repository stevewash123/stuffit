const $ = (id) => document.getElementById(id);
let tab;
chrome.tabs.query({ active: true, currentWindow: true }).then(([t]) => { tab = t; $("page").textContent = t ? t.title || t.url : ""; });

async function save() {
  if (!tab) return;
  $("save").disabled = true;
  $("msg").className = ""; $("msg").textContent = "Saving…";
  const r = await chrome.runtime.sendMessage({ type: "save", tabId: tab.id, note: $("note").value });
  if (r && r.ok) {
    $("msg").textContent = "Saved" + (r.pdfs ? ` + ${r.pdfs} PDF${r.pdfs > 1 ? "s" : ""}` : "") + (r.failed.length ? ` (${r.failed.length} PDF(s) failed)` : "") + ": " + r.where;
    setTimeout(() => window.close(), 1800);
  } else {
    $("msg").className = "err"; $("msg").textContent = "Not saved: " + (r && r.error || "no answer");
    $("save").disabled = false;
  }
}
$("save").addEventListener("click", save);
$("note").addEventListener("keydown", (e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); save(); } });
