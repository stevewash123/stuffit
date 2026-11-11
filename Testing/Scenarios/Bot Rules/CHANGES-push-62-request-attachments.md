# Push 62: photos and papers on a service request (2026-11-10)

API and UI. No migration (a new kind of document owner only). Story S3.4.8.

| Change | What to check |
|---|---|
| **Attach a photo or paper to a request** | On a plan's "Asking for service" card, each request has **Attach a photo or paper**. Choose one or several files (a photo of the broken part, the company's email saved as a PDF, the technician's invoice). They go up one after another and the request lists them with their sizes. The file picker offers images and PDFs |
| **View** | **View** opens the file in a new tab |
| **Remove** | **Remove** asks first ("Remove this file? ... This cannot be undone."), then the file is gone from the request |
| A wrong kind of file is refused with a message | Try a `.txt` file: "Use a PDF, JPEG, PNG, WebP or HEIC file." Nothing is attached |
| The files go when the request or the plan goes | Remove a request that has files: its files are deleted (opening one by its old address gives not found). Delete a plan: the files of all its requests go too |
| One person's files are theirs | A file cannot be attached to another plan's or another account's request |
| **The export has them** | Settings > Privacy & data > Prepare my download: the zip has `files/plans/<plan name>_<id>/requests/<date>_<what broke>_<id>/<file>` for each attached file, beside the plan's own contract files |

## Not built yet (do not report)
- Joining requests to Money recovered, the claim wizard offer on a denial, the phone-insurance cost view, the three-layer explanation, a person adding their own plan type, receipt-to-plan-type matching, a seeded provider list.
