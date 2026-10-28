# StuffIt Page Saver

Saves the source of the page you are on (the rendered DOM, with its address, title and time in a comment at the top). One click, one page, nothing automatic.

**Load:** `chrome://extensions` > Developer mode > Load unpacked > this folder. Click the toolbar button or press Alt+Shift+S. The badge shows OK or ERR.

**Where it goes**
- If `receiver.py` is running (`python receiver.py`), into `OfficialDocs/<host>/pagesource/<time>_<title>.html` (PDFs go in `OfficialDocs/<host>/`). Pass a folder to put it elsewhere.
- Otherwise into `Downloads/StuffIt-pages/<host>/pagesource/`. Chrome only lets extensions write under Downloads.

**PDFs:** the same click also saves every PDF the page links to (checked to really be a PDF; a file already there with the same size is skipped), next to the page. On a tab that is itself a PDF, the click saves that file. The badge shows how many PDFs were saved (`+3`); orange means some failed (details in the extension's service-worker console). A PDF behind a script button rather than a link is not found.

**Permissions:** it can fetch from any http/https site, because the PDFs are often on another host. It acts only when you click.

## The note
The toolbar button (or Alt+Shift+S) opens a small box: "What caught your eye?". It is optional. Enter saves, Shift+Enter adds a line. The note is written into the saved page's header comment and is where the AI pass starts. Alt+Shift+Q saves at once with no box.

## The AI pass
`python analyze_pages.py` (set `ANTHROPIC_API_KEY` in the environment first; the key is only read from there). For each saved page that has not been read yet it writes `<page>.analysis.json` beside it, then rebuilds `OfficialDocs/<site>/REVIEW.md`:
- what kind of page it is, the company, and the products it names;
- warranty facts, each with the sentence it relied on. A fact whose sentence is not really on the page is dropped, as is any link the page does not contain;
- links worth opening (warranty PDFs, terms, registration, claims, extended plans), best first, marked `saved` when the PDF is already in the folder;
- what the page does not say.

It never fetches a link and never runs the page; you open what it points at and confirm. `--all` reads every page again; `--model` picks the model (default `claude-sonnet-5-5`). Each page costs a few cents.
