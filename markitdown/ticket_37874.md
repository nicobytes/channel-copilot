6/18/26, 9:02 AM dotcms.freshdesk.com/helpdesk/tickets/37874/print
dotCMS #37874
Ticket Details
| Status       | Priority         | Source               | Type                           |
| ------------ | ---------------- | -------------------- | ------------------------------ |
| Open         | Medium           | Portal               | Incident                       |
| Group        | Agent            | Product              | Severity                       |
| Support (T1) | Neeha Kethi      | dotCMS               | Medium                         |
| Order        | Environment Type | Environment          | dotCMS Version                 |
|              | Live             | Authoring            | Current Release (dotEvergreen) |
| Version      | Main Topic       | Related GitHub Issue | Github Issue Filed             |
Recently Upgraded/Updated Maintenance Type Comment Aprx Total Hours
Yes
| Summary | Follow Up | AI Response |     |
| ------- | --------- | ----------- | --- |
by Sherlyn Alanís on Thu, 11 Jun at 6:49 PM via Portal
Card Carousel Content Not Displaying in Editor (Draft & Preview)
Hello Team,
Our client has reported an issue in the editor where content from the "Card Carousel" content type is not being displayed in either Draft or Preview mode.
This component is typically used across the model index pages, for example:
/modelos/creta-2026/index
As background, a few weeks ago we noticed a similar behavior with the "Hero Carousel" component, which was also not loading in the editor. After a maintenance
window, the issue appeared to be resolved.
Could you please help us investigate this behavior? We find it noteworthy that both cases involve carousel components, so we are wondering if there could be a
related underlying issue.
Please let us know if you need any additional information from our side.
Thank you for your support.
Best regards,
Sherlyn
Comments
by Syed Saad on Fri, 12 Jun at 2:53 AM as Outbound email
Hi Sherlyn,
Thank you for getting in touch. I'm currently examining this in your authoring environment and will inform you of my findings as soon as I can.
Ticket URL: https://helpdesk.dotcms.com/helpdesk/tickets/37874
Thanks

**For any site outage—even if reported during regular support hours—please call our Critical Care line at 1-800-509-1676 to ensure continued support
after hours.**
https://dotcms.freshdesk.com/helpdesk/tickets/37874/print 1/3

6/18/26, 9:02 AM dotcms.freshdesk.com/helpdesk/tickets/37874/print
Syed Saad Jawed Technical support engineer
syed.saad@dotcms.com
dotcms.com
by Syed Saad on Fri, 12 Jun at 9:44 AM as Private note
some of the errors i see in the front end
by Syed Saad on Fri, 12 Jun at 9:48 AM as Private note
[12/06/26 13:45:48:510 UTC] ERROR model.Contentlet: Found Tag with id [54fdda88-6c1c-4f33-aee0-af26ad3571c4] related with Conten
by Neeha Kethi on Wed, 17 Jun at 5:26 PM as Private note
Investigation notes — Card Carousel blank in editor (Draft & Preview)
ROOT CAUSE (confirmed): Front-end theme issue, NOT a content/index/backend or dotCMS core bug. The Card Carousel slider (jQuery Slick) is initialized in the
theme module /components/cardCarousel/js/cardCarousel.js only inside a one-time $(document).ready() handler (ccLoadCarousel() → .slick({...})). In the UVE
editor the page content is rendered/re-rendered dynamically (dot-uve.js), so that one-shot init never runs against the carousel's final DOM. Slick never initializes
(no slick-initialized/slick-loading class), and the .cc-wrapper stays in its pre-init visibility:hidden state → blank area in Draft/Preview. On the published site
the script runs at page load, so it renders fine.
WHY REINDEX DIDN'T HELP: The content is fully intact. This is purely a client-side init-timing issue, so reindex/cache-flush has no effect.
EVIDENCE (verified in customer's authoring env, read-only):
• Page render API (/api/v1/page/json|render) for /modelos/creta-2026/index: Card Carousel container returns 1 contentlet — "Hyundai SmartSense™" (inode
0c0182a9-…, identifier 86271b7d-…) — in BOTH WORKING and LIVE, same version (no divergent draft).
• Server renders the full carousel HTML in EDIT_MODE too: 5 cc-slide cards present (edit HTML 9,997 chars vs live 9,172). Content is NOT missing in the editor
markup.
• In the editor iframe: .cc-wrapper is 4,843px tall, opacity 1, 5 slides laid out, but computed visibility:hidden; all ancestors visible. Carousel has neither slick-
initialized nor slick-loading — Slick never ran.
• Forcing visibility:visible at runtime (not saved) revealed the cards (rendered as static stacked cards since Slick isn't initialized) — proves content present +
display/init gate.
• cardCarousel.js loads fine in the editor (HTTP 200, valid JS MIME) — not a 404/MIME/module-load problem. The module's init is the issue: const cardCarousel =
function($){ $(document).ready(function(){ ccLoadCarousel(); }); … }.
RE: customer's question about a shared underlying issue (Hero Carousel): Yes — same root cause. Hero Carousel renders in the editor now; it was
"resolved after a maintenance window," almost certainly because its init was made UVE-aware. CardCarousel still uses the plain one-shot $(document).ready(). The
diff between heroCarousel.js and cardCarousel.js init is the fix.
RECOMMENDED FIX (customer theme code):
1. Make the init idempotent: $('.cc-wrapper …').not('.slick-initialized').slick({...}).
2. Re-run it when UVE re-renders — hook dot-uve.js content-render event or attach a MutationObserver on the page body that (re)initializes new/un-initialized .cc-
wrapper carousels. Keep $(document).ready for the live site.
3. Mirror the HeroCarousel init pattern (already works in the editor).
https://dotcms.freshdesk.com/helpdesk/tickets/37874/print 2/3

6/18/26, 9:02 AM dotcms.freshdesk.com/helpdesk/tickets/37874/print
4. Safety net: don't leave .cc-wrapper permanently hidden if Slick fails to init (degrade to visible static cards).
5. Verify in UVE Draft AND Preview for both Card and Hero.
OWNERSHIP / ESCALATION: Fix is in the customer's custom theme (cardCarousel.js) — no dotCMS core GitHub issue warranted. No T2/T3/Cloud Eng
escalation needed.
NOISE (ruled out): The model.Contentlet: Found Tag … without an associated Field var name log is a non-fatal orphaned tag_inode log (Contentlet.java:1561),
unrelated to the blank render. The /dA/83cfc410c8/1140w/ 404 is a stray image-variant request, also unrelated.
Investigation performed read-only via the page API and editor DOM inspection; no changes made to content or environment.
by Neeha Kethi on Wed, 17 Jun at 5:27 PM as Private note
https://dotcms.slack.com/archives/C08F8NZRK9S/p1781731632634909
by Neeha Kethi on Wed, 17 Jun at 6:36 PM as Outbound email
Hi Sherlyn,
We appreciate your patience as we investigated this matter.
We now have some insights into the issue and believe it may be related to your own JavaScript files rather than to dotCMS.
We are verifying this with our front-end developers to ensure accuracy on our part. We will update you as soon as we receive their feedback and provide further
details about the issue.
Ticket URL: https://helpdesk.dotcms.com/helpdesk/tickets/37874
Thanks
**For any site outage—even if reported during regular support hours—please call our Critical Care line at 1-800-509-1676 to ensure continued support
after hours.**
Neeha Sri Product Support Lead
neeha.kethi@dotcms.com
dotcms.com
https://dotcms.freshdesk.com/helpdesk/tickets/37874/print 3/3
