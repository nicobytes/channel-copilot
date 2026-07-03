6/18/26, 8:57 AM dotcms.freshdesk.com/helpdesk/tickets/37931/print
dotCMS #37931
Ticket Details
| Status       | Priority         | Source      | Type            |
| ------------ | ---------------- | ----------- | --------------- |
| Open         | High             | Portal      | Problem         |
| Group        | Agent            | Product     | Severity        |
| Support (T3) | Nicolas Molina   | dotCMS      | High            |
| Order        | Environment Type | Environment | dotCMS Version  |
|              | Live             | QA          | Current Release |
(dotEvergreen)
| Version  | Main Topic       | Related GitHub Issue | Github Issue Filed |
| -------- | ---------------- | -------------------- | ------------------ |
| Recently | Maintenance Type | Comment              | Aprx Total Hours   |
Upgraded/Updated
Yes
| Summary | Follow Up | AI Response |     |
| ------- | --------- | ----------- | --- |
by Arun Muthu on Wed, 17 Jun at 3:21 PM via Portal
@dotcms/experiments 1.0.0 – Next.js 15 Integration Issues and Documentation Clarification
Title
Environment
dotCMS QA Environment
@dotcms/experiments: 1.0.0
Next.js 15 (App Router)
@dotcms/react
Analytics App enabled
Experiment configured on page with DEFAULT and custom variants
Issue Summary
We are attempting to integrate A/B testing using @dotcms/experiments@1.0.0 in a Next.js 15 App Router
application.
While following the npm package documentation, we encountered multiple issues related to SDK usage,
documentation, and UVE/backoffice compatibility.
Documentation Clarification Needed
The npm documentation references:
import { DotExperimentsProvider } from "@dotcms/experiments";
https://dotcms.freshdesk.com/helpdesk/tickets/37931/print 1/6

6/18/26, 8:57 AM dotcms.freshdesk.com/helpdesk/tickets/37931/print
However, the package does not appear to export DotExperimentsProvider. The only public export available
is:
import { withExperiments } from "@dotcms/experiments";
Can you confirm the recommended integration pattern for Next.js 15 App Router applications?
Current Implementation
const DotLayoutWithExperiments = withExperiments(DotCMSLayoutBody, {
apiKey,
server,
redirectFn,
});
The wrapped component is rendered only when analytics configuration is available.
Issues Observed
1. UVE / Backoffice Editor Failure
When opening a page inside the dotCMS editor, the page fails to load and displays:
A client-side exception has occurred
2. Experiment API Error
Browser console shows:
GET /api/v1/experiments/DEFAULT 404 (Not Found)
3. Experiment Assignment
Console logs indicate:
No experiments assigned to the client
even though an experiment is configured on the page and variants exist.
Questions
1. Is withExperiments the recommended approach for Next.js 15 App Router?
2. Should the server configuration point directly to the dotCMS origin, or is using Azure Front Door/CDN
supported?
3. Is the SDK expected to function inside UVE/backoffice editor mode, or should experiment initialization
be disabled while editing?
4. What causes the SDK to request /api/v1/experiments/DEFAULT and return 404?
5. Can you provide a complete working example for Next.js 15 App Router using @dotcms/experiments
1.0.0?
Expected Behavior
Experiments should initialize successfully on published pages.
Pages should continue to function correctly inside the dotCMS editor.
SDK documentation should align with the actual exported API.
https://dotcms.freshdesk.com/helpdesk/tickets/37931/print 2/6

6/18/26, 8:57 AM dotcms.freshdesk.com/helpdesk/tickets/37931/print
Would like have call, to understand the issue and fix it in live working session
as this needs for business team to run AB testing
host www.lennoxcommercial.com index page
Comments
by Nathan Hildebrandt on Wed, 17 Jun at 3:38 PM as Private note
🚨
Triage flags
None — no Critical Care indicators. Priority: High, severity: High. FR SLA due 2026-06-18 14:21 UTC —
respond today.
Customer is requesting a live call to unblock A/B testing on the Lennox Commercial homepage
(lennoxcommercial.com). This is business-critical and ProServ-adjacent — loop in CSM/ProServ before
committing to a call format.
🔍
Research summary
Similar tickets: None found — this is the first ticket on @dotcms/experiments + Next.js 15 App
Router integration.
GitHub: Not searched — no specific exception class or PR to target from ticket alone.
Slack: No prior discussion found for this specific combination of issues. A Great Clips experiments
issue appeared in #support (Nov 2025) but was CSM-level, not SDK-level.
Core repo: Searched core-web/libs/sdk/experiments/src/. Key findings below.
Confidence: MEDIUM — SDK behavior is confirmed from source; root cause of the DEFAULT 404 and
UVE crash requires more info from the customer.
Code findings:
1. DotExperimentsProvider is NOT exported — src/index.ts only exports withExperiments. The npm
docs are stale. DotExperimentsProvider is an internal component wrapped by withExperiments. The
customer's current implementation using withExperiments is correct.
2. UVE editor detection IS implemented in the SDK — DotExperimentsProvider.tsx calls
getUVEState()?.mode from @dotcms/uve on init and skips experiment initialization when inside the
editor. useExperimentVariant.ts also checks UVE_MODE.EDIT before waiting for variants. The UVE crash
they're experiencing is likely because their Next.js setup is missing the UVE integration layer
(DotCMSPageEditor or equivalent) that sets up the UVE state — so getUVEState() returns
null/undefined, the guard doesn't fire, and the SDK tries to run inside the editor and crashes.
3. The /api/v1/experiments/DEFAULT 404 — The SDK itself calls
/api/v1/experiments/isUserIncluded, not /api/v1/experiments/DEFAULT. The DEFAULT call is almost
certainly coming from the dotCMS backoffice/UVE trying to look up an experiment result, where
something is resolving the page's default variant name ("DEFAULT" is a constant in the SDK:
EXPERIMENT_DEFAULT_VARIANT_NAME = 'DEFAULT') as an experiment ID instead of the actual experiment
UUID. We need the customer's experiment ID from their dotCMS backoffice to confirm.
https://dotcms.freshdesk.com/helpdesk/tickets/37931/print 3/6

6/18/26, 8:57 AM dotcms.freshdesk.com/helpdesk/tickets/37931/print
4. CDN/Azure Front Door — The server config should point to the dotCMS origin directly. CDN layers
can cache or strip headers that the experiments API depends on.
📝
Draft first response
Hi Arun,
Thank you for the thorough write-up — this level of detail makes it much easier for us to dig in quickly.
We've reviewed the SDK source and have some clear answers for you, along with a few questions to help us
nail down the remaining issues.
1. withExperiments is the correct API
You're doing the right thing. withExperiments is the only public export from @dotcms/experiments@1.0.0 —
the DotExperimentsProvider referenced in the npm docs is an internal component that withExperiments
wraps. The docs are out of sync with the package, and we'll flag that for the team. Your current
implementation is the supported pattern.
2. UVE/editor crash
The SDK does have built-in editor detection — it calls getUVEState() from @dotcms/uve and skips experiment
initialization when inside the editor. The crash you're seeing suggests the UVE state isn't being set up before
the experiments SDK initializes. In a Next.js App Router setup, this typically means the UVE integration
layer (the component that establishes the editor context) needs to wrap or run before withExperiments
renders. Could you share how you've integrated @dotcms/uve in your layout — specifically whether you're
using DotCMSPageEditor or a similar editor wrapper, and where it sits relative to the experiments-wrapped
component?
3. GET /api/v1/experiments/DEFAULT — 404
The SDK itself calls /api/v1/experiments/isUserIncluded, not /api/v1/experiments/DEFAULT. The DEFAULT
path you're seeing in the browser console is coming from somewhere else — likely the dotCMS backoffice UI
trying to fetch an experiment by ID, where "DEFAULT" (the SDK's internal name for the default variant) is
being used instead of the experiment's actual UUID. To help us identify the source: what is the name and
status of the experiment you've configured in your dotCMS backoffice? Is it in "Running" status?
4. No experiments assigned to the client
This is expected when the experiment isn't in "Running" status, or when the Analytics/CubeJS layer hasn't
recorded a session for the client yet. Confirming the experiment status will clarify this.
5. Azure Front Door / CDN as the server value
We recommend pointing the server config directly to your dotCMS origin rather than through Azure Front
Door. CDN layers can cache or interfere with the experiments API responses, which are session-specific and
should not be cached.
Regarding a live call:
We'd be glad to help set that up — let us connect you with the right person on our team who can join a
working session. We'll follow up shortly on scheduling.
We're actively looking into this and will keep you updated as we have more.
Best regards,
Nathan
dotCMS Support
https://dotcms.freshdesk.com/helpdesk/tickets/37931/print 4/6

6/18/26, 8:57 AM dotcms.freshdesk.com/helpdesk/tickets/37931/print
⚠
Agent notes
Confirm experiment is in "Running" status in backoffice before sending — if it's not Running, "no
experiments assigned" and the 404 may both resolve once it's started.
Ask ProServ/CSM before committing to the call — this is a lennoxcommercial.com integration which
may be a ProServ engagement.
The npm docs discrepancy (DotExperimentsProvider export) should be filed internally — flag to the
Scout/SDK team.
by Nathan Hildebrandt on Wed, 17 Jun at 3:57 PM as Outbound email
Hi Arun,
Thanks for the detailed information, I have reached out to our T3 team who should be able to assist you with
these Next.js questions in regards to Experiments. They will reach out as soon as they have any information
to share.
Ticket URL: https://helpdesk.dotcms.com/helpdesk/tickets/37931
Thanks,
**For any site outage—even if reported during regular support hours—please call our Critical Care
line at 1-800-509-1676 to ensure continued support after hours.**
Nathan Hildebrandt
Product Support Specialist
nathan.hildebrandt@dotcms.com
dotcms.com
by Nicolas Molina on Wed, 17 Jun at 4:36 PM as Outbound email
Hi Arun,
Thank you for the detailed write-up — it gives us a clear picture of what's happening and makes it much easier to
dig in.
I've reviewed the SDK source and can already confirm a few things:
@dotcms/experiments
1. is the correct API. It's the only public export in —
withExperiments @dotcms/experiments@1.0.0
is an internal component that wraps. The npm docs referencing
DotExperimentsProvider withExperiments
it are out of date, and we're correcting that on our side. Your current implementation pattern is the supported
one.
https://dotcms.freshdesk.com/helpdesk/tickets/37931/print 5/6

6/18/26, 8:57 AM dotcms.freshdesk.com/helpdesk/tickets/37931/print
2. The UVE/editor crash and the 404 are on our radar. The SDK itself only calls
/api/v1/experiments/DEFAULT
, so the request is coming from elsewhere, and we've
/api/v1/experiments/isUserIncluded DEFAULT
identified the likely source. We're reproducing both issues on a Next.js 15 App Router setup to confirm the root
cause.
I'm actively working on this now and will be putting together a complete, working Next.js 15 App Router example for
as part of it.
@dotcms/experiments
To help us nail down the remaining details, could you confirm:
The name and status of the experiment configured on the page — specifically, is it in Running status?
How you've integrated in your layout (which editor wrapper you use and where it sits relative to
@dotcms/uve
the experiments-wrapped component).
Whether your server config points directly to your dotCMS origin or goes through Azure Front Door/CDN. We
recommend pointing directly to the origin, since CDN layers can cache or strip headers the experiments API
depends on.
I'll keep you posted as I make progress. We're also happy to set up a working session — we'll follow up shortly on
scheduling.
Best regards, Nicolas Molina
by Arun Muthu on Thu, 18 Jun at 6:02 AM as Incoming email
Hi Team,
Move to site www.lennoxcommercial.com in dotCMS backoffice , index page and variant name = HomeNew
Page url would be: www.lennoxqa.com/commercial
Attaching code snippet: Page.tsx on experiment usage
Server config pointed to azure app server url, where has to be pointed? To instance url https://lennox-
test.dotcms.cloud ?
Regards,
Arun
https://dotcms.freshdesk.com/helpdesk/tickets/37931/print 6/6
