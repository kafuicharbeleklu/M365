# FIX-098 - Move page3 bookmark click handling onto cards to avoid native ctrl-click hover

## Summary
- Moved the bookmark action for the main interactive KPI cards on page 3 onto the cards themselves.
- Moved the transparent bookmark buttons behind the cards so they no longer capture hover first.
- Applied the same change to the 3 action cards on page 3.

## Why
- Screenshot review showed the native Desktop helper `CTRL+click here to follow` instead of the intended custom tooltip.
- This happens when the transparent `actionButton` overlay captures hover before the card tooltip can render.
- A second screenshot confirmed that cards without such overlay still showed the expected custom tooltip.

## Scope
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/*/visual.json`

## Validation
- Static validation only in source.
- Manual validation required in Power BI Desktop:
  - Hover on interactive page 3 cards should now show the custom tooltip instead of the native `CTRL+click` helper.
  - Clicking the same cards should still apply the expected bookmark/filter action.
