6/30/26, 6:24 PM helpdesk.dotcms.com/helpdesk/tickets/37857/print
dotCMS #37857
Ticket Details
| Status       | Priority         | Source      | Type            |
| ------------ | ---------------- | ----------- | --------------- |
| On-Hold      | High             | Portal      | Problem         |
| Group        | Agent            | Product     | Severity        |
| Support (T3) | Daniel Silva     | dotCMS      | High            |
| Order        | Environment Type | Environment | dotCMS Version  |
|              | Live             | ALL         | Current Release |
(dotEvergreen)
| Version | Main Topic | Related GitHub Issue | Github Issue Filed |
| ------- | ---------- | -------------------- | ------------------ |
26.05.22-01
| Recently | Maintenance Type | Comment | Aprx Total Hours |
| -------- | ---------------- | ------- | ---------------- |
Upgraded/Updated
Yes
| Summary | Follow Up | AI Response |     |
| ------- | --------- | ----------- | --- |
by Glenn Gardner on Tue, 9 Jun at 7:03 PM via Portal
Intermittent Inability to Select/Edit Contentlets in Edit Mode
Content authors are intermittently unable to select, click, or edit specific contentlets located in the middle
sections of certain pages while working in Edit/Draft Mode.
Sometimes, only a single contentlet may remain selectable, even if the page contains 6–10 independent
contentlets. The rest of the contentlets become completely unresponsive to clicks.
This appears to be a structural, layout-rendering, or state-handling issue rather than a total page freeze, as
parts of the UI remain interactive.
Steps to Reproduce
1. Log into the dotCMS backend for the firstmac-dev.dotcms.cloud instance.
2. Navigate to the Pages tool and switch to the www.loans.com.au website instance.
3. Open any of the affected pages listed below.
4. Ensure the page editor is set to Edit Mode (Draft).
5. Attempt to click or select the contentlets located in the middle area of the screen.
examples of pages where contentlets aren't selectable:
https://helpdesk.dotcms.com/helpdesk/tickets/37857/print 1/6

6/30/26, 6:24 PM helpdesk.dotcms.com/helpdesk/tickets/37857/print
https://firstmac-dev.dotcms.cloud/dotAdmin/#/edit-page/content?url=%2Flanding-
pages%2Fhome%2Fbarebold-home-loan-refinance-search&language_id=1&host_id=da4f7456-bc3a-4404-
8d1e-406ba15e7fc9&mId=edit&mode=EDIT_MODE
https://firstmac-dev.dotcms.cloud/dotAdmin/#/edit-page/content?url=%2Fcaravan-
loans%2F&language_id=1&host_id=da4f7456-bc3a-4404-8d1e-
406ba15e7fc9&mId=edit&mode=EDIT_MODE
https://firstmac-dev.dotcms.cloud/dotAdmin/#/edit-page/content?
url=%2F&language_id=1&host_id=da4f7456-bc3a-4404-8d1e-
406ba15e7fc9&mId=edit&mode=EDIT_MODE
Temporary Workarounds
but users have reported inconsistent success with the following workarounds (none are 100% reliable):
Mode Toggling: Switching the page view from Edit Mode to Preview/Published Mode, and then toggling back
to Edit Mode sometimes restores selectability.
Hard Refresh: If mode toggling fails, doing a browser refresh (F5 / Ctrl + F5) occasionally forces the
container overlays to re-render correctly.
Comments
by Abdul Basit on Wed, 10 Jun at 4:36 AM as Outbound email
Hi Glenn,
Thank you for reaching out!
We are currently investigating this issue and will inform you of our findings as soon as we complete our
testing on our end.
Best regards,
Ticket URL: https://helpdesk.dotcms.com/helpdesk/tickets/37857
Syed Abdul Basit
Technical Support Engineer
abdul.basit@dotcms.com
dotcms.com
by Abdul Basit on Fri, 12 Jun at 9:47 AM as Outbound email
https://helpdesk.dotcms.com/helpdesk/tickets/37857/print 2/6

6/30/26, 6:24 PM helpdesk.dotcms.com/helpdesk/tickets/37857/print
Hi Glenn,
I am still investigating this issue and will provide you with an update shortly regarding this matter.
Thank you for your understanding.
Ticket URL: https://helpdesk.dotcms.com/helpdesk/tickets/37857
Syed Abdul Basit
Technical Support Engineer
abdul.basit@dotcms.com
dotcms.com
by Abdul Basit on Fri, 12 Jun at 10:41 AM as Private note
https://dotcms.slack.com/archives/C08F8NZRK9S/p1781183701709499
by Glenn Gardner on Sun, 14 Jun at 6:53 PM as Incoming email
Hi,
Lets go with option 1. Thank you!
by Rafael Velazco on Mon, 15 Jun at 12:24 PM as Outbound email
Hi Glenn,
Thanks for reporting this issue and helping us improve dotCMS.
Weʼve logged it for our engineering team and created a linked GitHub issue for visibility:
https://github.com/dotCMS/core/issues/36167
Please confirm how youʼd like us to proceed:
Option 1: Keep this ticket on hold — weʼll update you once the fix is released.
Option 2:Close this ticket now — youʼll track updates directly through GitHub and your CSM.
Our development teams work in 2-week sprint cycles. Each issue moves through:
Triage & Evaluation – Review and prioritization
Fix Development & Testing – Implementation and validation
Release / Backporting – Deployment to supported versions
https://helpdesk.dotcms.com/helpdesk/tickets/37857/print 3/6

6/30/26, 6:24 PM helpdesk.dotcms.com/helpdesk/tickets/37857/print
Because fixes are released in planned sprints, timelines vary. If the issue becomes business-critical, please
reach out to your CSM to discuss prioritization.
Please let us know your preference — whether to keep this ticket on hold or close it now.
Thank you for your patience and understanding as we work to resolve this.
Ticket URL: https://helpdesk.dotcms.com/helpdesk/tickets/37857
by Abdul Basit on Fri, 19 Jun at 4:16 AM as Outbound email
Hi Glenn,
I am following up on this case to see if you have had a chance to review our last email and if you have any
updates or questions regarding this case.
If we do not hear back within the next three business days, we will mark this case as solved.
Please feel free to contact me if you need any more help.
Ticket URL: https://helpdesk.dotcms.com/helpdesk/tickets/37857
Syed Abdul Basit
Technical Support Engineer
abdul.basit@dotcms.com
dotcms.com
by Abdul Basit on Mon, 22 Jun at 4:35 AM as Outbound email
Hi Glenn,
I am following up on this case to see if you have had a chance to review our last email and if you have any
updates or questions regarding this case.
If we do not hear back within the next three business days, we will mark this case as solved.
Please feel free to contact me if you need any more help.
Ticket URL: https://helpdesk.dotcms.com/helpdesk/tickets/37857
Thanks,
https://helpdesk.dotcms.com/helpdesk/tickets/37857/print 4/6

6/30/26, 6:24 PM helpdesk.dotcms.com/helpdesk/tickets/37857/print
Syed Abdul Basit
Technical Support Engineer
abdul.basit@dotcms.com
dotcms.com
by Abdul Basit on Thu, 25 Jun at 4:42 AM as Outbound email
Hi Glenn,
I am following up on this case to see if you have had a chance to review our last email and if you have any
updates or questions regarding this case.
If we do not hear back within the next three business days, we will mark this case as solved.
Please feel free to contact me if you need any more help.
Thanks,
Ticket URL: https://helpdesk.dotcms.com/helpdesk/tickets/37857
Syed Abdul Basit
Technical Support Engineer
abdul.basit@dotcms.com
dotcms.com
by Glenn Gardner on Thu, 25 Jun at 6:22 PM as Public note
Hi Abdul,
may we get an update on when would this bug be fixed? - UVE: Unable to edit page when document.write
re-executes inline scripts and throws 'already declared…
by Neeha Kethi on Thu, 25 Jun at 11:20 PM as Outbound email
Hi Glenn,
Thanks for reaching out.
Weʼve set the status to “On Hold” while Engineering reviews the linked GitHub issue.
You can expect our subsequent follow-up on the next Maintenance Sprint planning Day, or sooner if the fix is
included in an upcoming release.
At this time, we canʼt confirm any ETA on when it will be included in a sprint or release, but weʼll keep you
https://helpdesk.dotcms.com/helpdesk/tickets/37857/print 5/6

6/30/26, 6:24 PM helpdesk.dotcms.com/helpdesk/tickets/37857/print
informed as soon as that changes.
If youʼd like to increase the priority, please get in touch with your CSM.
Thank you for your patience and understanding.
Ticket URL: https://helpdesk.dotcms.com/helpdesk/tickets/37857
Thanks
**For any site outage—even if reported during regular support hours—please call our Critical Care
line at 1-800-509-1676 to ensure continued support after hours.**
Neeha Sri Product Support Lead
neeha.kethi@dotcms.com
dotcms.com
by Monica Patel on Tue, 30 Jun at 11:53 AM as Private note
Neeha KethiDaniel Silva
Do we have a workaround for the customer? This is a pretty urgent need for them as this issue is significantly
impacting their operations, as their content team is currently unable to perform necessary page updates
across our websites. They also have a major content update scheduled for this week and this bug poses a
big challenge to their timeline.
https://helpdesk.dotcms.com/helpdesk/tickets/37857/print 6/6
