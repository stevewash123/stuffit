# UAT re-check: Push 91, empty Name in "Replaced by the plan" (NEXT-REPORT-ADDITIONS)

- **Build tested:** API `bde7439`; UI Last-Modified **Fri, 13 Nov 2026 12:53:03 UTC (7:53 AM ET)** (Push 91, unchanged). Fresh page load, no new-version banner.
- **Scope:** `Bot Rules\NEXT-REPORT-ADDITIONS.md` (CC, 8:05 AM ET): re-check the Push 91 check 2 Fail with real typing.
- **Tester / account:** QA Controller, box browser, Alice ("P34-Alice Repairs"), 8:33–8:35 AM ET Nov 13 2026.
- **Test item:** "P91R UAT Replace Me" (Walmart/Vizio fixture, Electronics) with an Allstate warranty extension typed in. Deleted afterwards (plan cancelled with it). No replacement created. No new fixtures.

## Result: Pass. The Push 91 Fail is withdrawn (QA error)

| Test | Name before click | Button | Click |
|---|---|---|---|
| A: Ctrl+A, Backspace | `""` | `disabled: true`, pale teal | nothing happened, no message, nothing saved |
| B: Backspace per character | `""` | `disabled: true`, pale teal | nothing happened, no message, nothing saved |
| C: typed "P91R New" | `"P91R New"` | `disabled: false`, solid green | (closed without saving) |

Plan question answered ("Carry on with the replacement") in A and B. Other inputs at the time: rp-model `"V505-J09"`, rp-serial `""`, rp-on `"2026-11-13"`, Brand chip "Vizio" still selected. Values and the disabled state were read through browser automation (read-only); all typing was real key presses.

## Answers to CC's questions
1. **Disabled look and click:** yes, pale (disabled) look with `disabled: true`; a click does nothing (no error, no save).
2. **Earlier builds:** no earlier run tested an empty Name. Push 90 tested only the "Mark as returned" drawer; Push 34 checked only that the button stays disabled until the plan question is answered. Nothing to compare.
3. **Name contents:** empty string `""`.

**Correction to Push 91 report:** the Push 91 screenshot `push91/shots/02-name-cleared.png` also shows the button in its pale disabled look; the earlier "not disabled" call was a misjudgement by QA, not an app bug. Push 91 is therefore **4 Pass, 0 Fail, 1 Low** (future-date error stays after fixing the date), 1 Info (logo overlaps account label).

Screenshots: `/workspace/uat/push91b/shots/` (01-drawer-enabled, 02-A-cleared-disabled, 03-A-button-zoom, 04-B-cleared-disabled, 05-C-retyped-enabled).
