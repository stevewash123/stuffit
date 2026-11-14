# Push 98: a negative refund is refused in words (small fix, repeated Info from the Push 90 and 92 reports)

UI only (API unchanged at bde7439). Push 97 (the Cancel this plan sheet split) passed (5 Pass, 1 not tested). In "Mark as returned", a negative refund used to show the server's raw text ("The field RefundAmount must be between 0 and 100000000."). The item page now checks it first and says, in the drawer: "The refund can't be less than zero. Leave it empty if the money has not come back yet." Nothing is sent to the server in that case.

## What to check (item page, Mark as returned)
1. Enter a refund of -50 and press Mark returned: the red message above appears in the drawer and nothing is saved. Change the amount to a valid number (or empty): the message goes away (Push 92) and saving works as before.
2. Zero and empty refunds, and everything else about the drawer, behave as before.
