# What changed in push 13: the product is now WarrantyCat, plus Plan and billing (2026-11-04)

For GrokBot. API `f2fd92a`, UI `52098e3`. No migration. Check `/api/version` shows `f2fd92a` before you start.

| Change | What you should see | Your row |
|---|---|---|
| **New name: WarrantyCat** | Every place that said **WarrantyBank** now says **WarrantyCat**: browser tab titles ("Home · WarrantyCat", "Sign in · WarrantyCat"), the installed-app name, the footer, the welcome and install pages, the Terms, Privacy and Disclaimer pages, the Share page ("choose WarrantyCat"), and the app-password steps for Google and Apple mail | New row: search every page you visit for "WarrantyBank" and "StuffIt"; report any that remain |
| **Emails** | Sender display name and subjects use WarrantyCat: "Confirm your email to start with WarrantyCat", "Reset your WarrantyCat password", "You already have a WarrantyCat account", the daily digest button "Open WarrantyCat". The sender address (noreply@stuff.microsaasbuilders.com) is **unchanged** and the Render sender name may still read WarrantyBank until it is edited in the dashboard | Sign-up and reset emails in Scenario 25 |
| **Authenticator label** | The two-step setup for an administrator shows the issuer **WarrantyCat** (otpauth label). Codes from an authenticator set up earlier keep working | Scenario 28 |
| **Data export** | The README inside the export says "WarrantyCat data export" | Scenario 25 export step |
| **Plan and billing tab** (S1.2.2) | Account > Plan and billing has a **Manage membership** button that goes to Stripe's customer portal. The monthly and yearly plans show switched off as "coming soon" | New check: open the tab, confirm the button and the two disabled plans; do not complete anything on Stripe |

## Decided, do not report
- **Still says StuffIt:** the browser-storage keys (`stuffit.*`), the folder and repo names, the sender domain `stuff.microsaasbuilders.com`, and the older UAT results and scenario files. Only user-facing text was renamed.
- **No logo yet:** the Rocky cat is not in the app. The favicon and app icons are plain teal "WC" placeholders until the logo work is finished. The earlier shield logos were retired (the name WarrantyBank is dropped).
- **Sharing rule:** the planning documents now say uploads are shared with redaction, a preview, an off switch and withdraw (S6.1.6), but none of that is built. Do not look for a sharing setting or a redaction preview.
