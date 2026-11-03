# Scenario 48: One item, four layers: what the page says and whether it is true

**DEFERRED until implemented: S3.4.13, S3.4.12, S3.4.18 (and the S3.4.2 open UAT items).** Do not run before then. Steps that need a not-yet-built screen say what to look for and will fail on build 982952c.

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts clean. Test1 has "UAT Fridge" ($900, Best Buy, today, paid with the Chase Freedom Unlimited card) and a Geek Squad plan on it (2 years, $99, starts at purchase). Clock offset 0.
**Time:** 45 min
**Built per:** S3.4.13 (item page stack), S3.4.12 (front door), S3.4.18 (form safety). Retests UAT FS-31 steps 2, 4, 14, 15, 17, 18 and FS-40 step 6.
**Why this plan:** the open UAT items all come down to the page saying something untrue about a plan; this locks in the truth at every clock position.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Open UAT Fridge | Return window, maker warranty (if the brand is known), card extension and the protection plan, each with dates. The plan card shows company, name, status, dates, what it adds in one line, service fee, claim phone/site as tap targets, contract number with copy |
| 2 | Test1 | Read the one-line stack explanation | "Your Chase card adds 12 months to the maker's warranty; the Geek Squad plan runs <start> to <end>." The card is "Card extended warranty", the plan "Protection plan" |
| 3 | Test1 | Check which is first | The coverage that applies today is "Try this first"; the plan is "Backup" while the maker's warranty runs |
| 4 | Test1 | Clock to the day the maker's warranty ends | The plan becomes the one to try first; the card extension still counts until its end |
| 5 | Test1 | End the plan today (End this plan, confirm) | Confirmation names the item count and date. Plan is Ended on the plan page **and** the item (not "Ends today"); the item's badge and Next to end ignore it; the list excludes it from the running total and shows its own cost consistently |
| 6 | Test1 | Clock +1 day | Same state; no reminder about the ended plan |
| 7 | Test1 | Create a plan with nothing filled and Save | Each required field marked with its own message; focus on the first; no raw "validation errors" banner |
| 8 | Test1 | End date before start | Message on the field with a suggested fix; nothing saved |
| 9 | Test1 | Read a contract (reader on), then press Cancel | "Keep editing / Leave without saving" |
| 10 | Test1 | Read a document with the website printed as www.example.com/x | Offered as https://www.example.com/x to accept, not rejected |
| 11 | Test1 | Update from a newer document where only the fee changed | Only the fee is listed (old, new, quote); unchanged fields are not listed or ticked; if nothing differs the page says so |
| 12 | Test1 | Find the plan from the Home tile, a My Items filter "Has a protection plan", and a search by contract number | All three work; the Home tile counts running plans and those ending within 60 days |
| 13 | Test1 | Phone width, keyboard open: repeat the add and the error cases | No overlap, no horizontal scroll, errors beside the field |
| 14 | Test2 | Open Test1's plan or item addresses | Not found |

Also record: any place where the plan's badge, the item's badge and the totals disagree at any clock position.
