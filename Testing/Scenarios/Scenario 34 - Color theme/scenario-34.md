# Scenario 34: Choose a color theme and light or dark

**Accounts:** Test1 (stevewash123.test@gmail.com), Test2 (stevewash123.tester2@gmail.com)
**Preconditions:** Both accounts exist (Scenario 25). Use the same browser profile for the whole plan (the choice is kept per device, in that browser). Start from a browser with no earlier StuffIt theme choice (a new private window, or cleared site data).
**Time:** 20 min
**Built per:** S9.8.2, first slice: three themes (teal, indigo, berry), Light / Dark / "Match my device", kept on this device. NOT built, so not planned: saving the choice to the profile so it follows the person to another device, and removing every literal colour from older pages (a few pages still use fixed colours, so a few elements may not follow the theme; record them rather than failing the plan). The contrast maths is covered by the unit tests; this plan covers what a person sees.
**Why this plan:** a theme change touches every screen, so it is checked on the pages people use, and it must survive reloads without a flash of the wrong colours.

| # | Persona | Action | Expected |
|---|---|---|---|
| 1 | Test1 | Sign in and open Settings, tab **Appearance** (`/settings/appearance`) | Heading "Appearance"; "Color theme" with Teal, Indigo and Berry (each with a swatch) and "Light or dark" with Light, Dark and "Match my device". Teal and one light/dark choice are selected. Record which. A note says the choice is kept on this device and not yet saved to the profile |
| 2 | Test1 | Pick **Indigo** | The whole page changes colour at once (header, buttons, links). No reload needed |
| 3 | Test1 | Visit Home, My Items, New Items, an item page and Settings | Every page uses Indigo. Record any element still showing teal or an out-of-place colour (page and element) |
| 4 | Test1 | Pick **Berry**, then **Teal** | Each applies at once; Teal looks as it did at the start |
| 5 | Test1 | Pick **Dark** | The app turns dark; text is readable everywhere you look (body text, form fields, badges, the notice and warning boxes). Record any unreadable text or a bright patch |
| 6 | Test1 | Pick **Light** | Back to light |
| 7 | Test1 | Pick **Match my device** | A line appears: "Using light because that is your device's setting." (or dark). It agrees with your device setting. If you can switch the device or browser between light and dark, do so and confirm the app follows; otherwise note "could not change device setting" |
| 8 | Test1 | Choose Berry and Dark, then reload the page | Opens in Berry and dark straight away. Watch the first moment of the load: no flash of the teal light look. Record whether any flash is visible |
| 9 | Test1 | Close the tab, open the site again in a new tab | Still Berry and dark |
| 10 | Test1 | Sign out | The sign-in page uses the saved theme (or the default; record which) |
| 11 | Test2 | Sign in as Test2 in the same browser | Test2 sees the same theme (it belongs to the device, not the account). Record the result |
| 12 | Test2 | In a private window (no earlier choice), sign in as Test2 | Default look: Teal, matching the device's light or dark. The earlier window's Berry does not appear |
| 13 | Test1 | Clear this site's stored data, then reload | The default theme returns; the page still works with nothing saved |
| 14 | Test1 | Look at Settings, Appearance on a phone-width window | The choices fit without sideways scrolling |
| 15 | Test1 | Open the Terms and Disclaimer pages (`/terms`, `/disclaimer`) while Berry and dark | They use the theme too and the text is readable |

Also record: any page where a colour clearly ignores the theme, any text hard to read in dark mode, and anything that flashes on load.
