# Push 47: re-adding a repair order keeps "added by you" rows (2026-11-09)

Fix for the push 46 Medium. Re-adding an order already in history replaces only the entries the rules kept; jobs added by hand ("added by you") stay. Ticking the same left-out job again does not duplicate it. The card now says "jobs you added by hand stay". The no-odometer card no longer says "Its odometer reading can still be kept".

Check: P46-01 add oil + tires + wipers, then re-read and Add with nothing ticked: oil only replaced, tires and wipers still there, still "added by you".
Not changed: the three Low notes (picker names, picker reset on retick).
