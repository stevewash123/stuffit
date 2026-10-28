const $ = (id) => document.getElementById(id);
const RECEIVER = "http://127.0.0.1:8791";
const clean = (s, max = 80) => (String(s || "").replace(/[^A-Za-z0-9._-]+/g, "_").replace(/^_+|_+$/g, "").slice(0, max)) || "page";
let tab, cfg = { api: "", token: "" }, found = null, pollTimer = null;

const el = (tag, props = {}, ...kids) => { const e = Object.assign(document.createElement(tag), props); kids.flat().forEach((k) => e.append(k)); return e; };

chrome.tabs.query({ active: true, currentWindow: true }).then(([t]) => {
  tab = t; $("page").textContent = t ? t.title || t.url : "";
  try { $("site").value = clean(new URL(t.url).host); } catch { /* not a web page */ }
  resume();
});
chrome.storage.local.get(["api", "token"]).then((v) => {
  cfg = { api: v.api || "", token: v.token || "" };
  $("api").value = cfg.api; $("token").value = cfg.token;
  if (!cfg.api || !cfg.token) $("setup").open = true;
});

// ---------- save the page (unchanged) ----------
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

// ---------- StuffIt connection ----------
async function api(path, opts = {}) {
  if (!cfg.api || !cfg.token) throw new Error("Set the StuffIt connection below first.");
  const res = await fetch(cfg.api.replace(/\/+$/, "") + "/api/web-data" + path, {
    ...opts, headers: { "X-StuffIt-Token": cfg.token, ...(opts.body ? { "content-type": "application/json" } : {}) }
  });
  if (res.status === 401) throw new Error("The key was refused: wrong, expired or revoked. Make a new one in Admin.");
  const body = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(body.detail || body.title || ("HTTP " + res.status));
  return body;
}

$("saveSetup").addEventListener("click", async () => {
  cfg = { api: $("api").value.trim(), token: $("token").value.trim() };
  await chrome.storage.local.set(cfg);
  $("setupMsg").className = ""; $("setupMsg").textContent = "Testing…";
  try { const r = await api("/ping"); $("setupMsg").className = "good"; $("setupMsg").textContent = "Connected as " + r.email; }
  catch (e) { $("setupMsg").className = "err"; $("setupMsg").textContent = e.message; }
});

// ---------- read saved pages (the receiver runs the AI pass) ----------
const logLine = (s) => { $("log").textContent = s; };

async function start() {
  const host = $("site").value.trim();
  if (!host) return;
  $("process").disabled = true; $("found").hidden = true; $("out").textContent = ""; logLine("Starting…");
  try {
    const r = await fetch(RECEIVER + "/process", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ host }) });
    const b = await r.json();
    if (!r.ok) throw new Error(b.error || "HTTP " + r.status);
    poll();
  } catch (e) { logLine(String(e.message).startsWith("Failed") ? "The receiver is not running. Start start-receiver.bat." : e.message); $("process").disabled = false; }
}
$("process").addEventListener("click", start);

async function poll() {
  clearTimeout(pollTimer);
  const host = $("site").value.trim();
  try {
    const j = await (await fetch(`${RECEIVER}/process-status?host=${encodeURIComponent(host)}`)).json();
    if (j.state === "running") { logLine((j.log || []).slice(-3).join("\n") || "Reading…"); $("process").disabled = true; pollTimer = setTimeout(poll, 1000); return; }
    $("process").disabled = false;
    if (j.state === "error") { logLine(j.log.slice(-2).join("\n")); return; }
    if (j.state === "done") { logLine((j.log || []).slice(-2).join("\n")); await show(j.result); }
  } catch { logLine("The receiver is not running. Start start-receiver.bat."); $("process").disabled = false; }
}

async function resume() { if ($("site").value) { const j = await fetch(`${RECEIVER}/process-status?host=${encodeURIComponent($("site").value)}`).then((r) => r.json()).catch(() => null); if (j && j.state === "running") { $("process").disabled = true; poll(); } } }

// ---------- choose and confirm ----------
const keyOf = (c, fields) => JSON.stringify(fields.map((f) => c[f] ?? null));
const SELLER = ["return_days", "return_from_delivery", "restocking_fee_percent"], MAKER = ["term_months", "start_rule"];

function describe(c, kind) {
  if (kind === "seller") return [c.return_days != null ? `${c.return_days}-day returns` : null, c.return_from_delivery ? "from delivery" : null, c.restocking_fee_percent != null ? `${c.restocking_fee_percent}% restocking fee` : null, c.conditions].filter(Boolean).join(", ");
  return [c.term_months != null ? `${c.term_months} months` : null, c.start_rule === "registration" ? "starts at registration" : null, c.conditions].filter(Boolean).join(", ");
}

function options(box, list, kind, fields, label) {
  box.textContent = "";
  if (!list.length) { box.append(el("small", {}, `No ${label} terms were found on the saved pages.`)); return; }
  const groups = new Map();
  list.forEach((c) => { const k = keyOf(c, fields); if (!groups.has(k)) groups.set(k, c); });
  box.append(el("h4", {}, label));
  const name = "pick_" + kind;
  [...groups.values()].forEach((c, i) => {
    const r = el("input", { type: "radio", name, value: String(i) });
    r.dataset.c = JSON.stringify(c);
    r.addEventListener("change", enable);
    if (groups.size === 1) r.checked = true;
    box.append(el("label", { className: "opt" }, r, " ", describe(c, kind), el("q", {}, `“${c.quote}” `), el("small", {}, c.source_url)));
  });
  const none = el("input", { type: "radio", name, value: "none" });
  none.addEventListener("change", enable);
  box.append(el("label", { className: "opt" }, none, " Do not update this"));
  if (groups.size > 1) box.append(el("small", { className: "err" }, "The pages disagree: choose one."));
}

function picked(kind) {
  const r = document.querySelector(`input[name=pick_${kind}]:checked`);
  return r && r.value !== "none" ? JSON.parse(r.dataset.c) : null;
}
function enable() {
  const sellerNeeded = document.querySelector("input[name=pick_seller]"), makerNeeded = document.querySelector("input[name=pick_manufacturer]");
  const decided = (n, e) => !e || document.querySelector(`input[name=${n}]:checked`);
  $("confirm").disabled = !($("party").value && decided("pick_seller", sellerNeeded) && decided("pick_manufacturer", makerNeeded) && (picked("seller") || picked("manufacturer")));
}

async function loadParties(q) {
  let host = $("site").value;
  try { if (tab && clean(new URL(tab.url).host) === host) host = new URL(tab.url).host; } catch { /* keep the folder name */ }
  let list = await api(`/parties?host=${encodeURIComponent(host)}` + (q ? `&q=${encodeURIComponent(q)}` : ""));
  if (!list.length && !q) {   // no store has this website yet: try the company name the pages gave
    const company = ((found && found.sources) || []).map((s) => s.company).find(Boolean);
    if (company) { $("partyq").value = company; list = await api(`/parties?host=${encodeURIComponent(host)}&q=${encodeURIComponent(company)}`); }
  }
  const sel = $("party"); sel.textContent = "";
  list.forEach((p) => sel.append(el("option", { value: p.id }, `${p.name}${p.hostMatches ? "  (site matches)" : ""}${p.isSeller ? "" : "  [brand only]"}`)));
  if (list.length && (list[0].hostMatches || list.length === 1)) sel.value = list[0].id;
  enable();
}

async function show(result) {
  found = result;
  $("found").hidden = false;
  options($("sellerBox"), result.seller, "seller", SELLER, "Return policy");
  options($("makerBox"), result.manufacturer, "manufacturer", MAKER, "Manufacturer warranty");
  try { await loadParties(""); } catch (e) { $("out").className = "err"; $("out").textContent = e.message; $("setup").open = true; }
  enable();
}
$("party").addEventListener("change", enable);
let qTimer; $("partyq").addEventListener("input", () => { clearTimeout(qTimer); qTimer = setTimeout(() => loadParties($("partyq").value.trim()).catch(() => {}), 300); });

$("confirm").addEventListener("click", async () => {
  $("confirm").disabled = true; $("out").className = ""; $("out").textContent = "Updating StuffIt…";
  const partyId = $("party").value, lines = [];
  const seller = picked("seller"), maker = picked("manufacturer");
  try {
    // One confirmation per source page: the evidence points at the page each value came from.
    const jobs = [];
    if (seller) jobs.push({ sourceUrl: seller.source_url, seller: { returnDays: seller.return_days, returnFromDelivery: seller.return_from_delivery, restockingFeePercent: seller.restocking_fee_percent, conditions: seller.conditions, quote: seller.quote } });
    if (maker) jobs.push({ sourceUrl: maker.source_url, manufacturer: { termMonths: maker.term_months, startRule: maker.start_rule === "registration" ? "registration" : maker.start_rule === "purchase_date" ? "purchaseDate" : null, conditions: maker.conditions, quote: maker.quote } });
    for (const j of jobs) {
      const r = await api("/confirm", { method: "POST", body: JSON.stringify({ partyId, ...j, note: $("note").value.trim() || null }) });
      if (r.websiteSet) lines.push(`Website set to ${r.website}`);
      r.results.forEach((x) => lines.push(`${r.partyName}: ${x.type} policy ${x.action}` + (x.changes.length ? " (" + x.changes.map((c) => `${c.field}: ${c.was ?? "none"} → ${c.now}`).join(", ") + ")" : "") + `, now ${x.band} (${Math.round(x.confidence * 100)}%)`));
    }
    $("out").className = "good"; $("out").textContent = lines.join("\n"); $("out").style.whiteSpace = "pre-wrap";
  } catch (e) { $("out").className = "err"; $("out").textContent = "Not updated: " + e.message; $("confirm").disabled = false; }
});
