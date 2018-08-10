id: ssp_template_ia_2__8
format: markdown
...
## User Account and Authentication (UAA) Server

Cloud.gov a limit of 5 consecutive invalid logon attempts by a user during a 15 minute period
Automatically; locks the account/node for 20 minutes when the maximum number of unsuccessful attempts is exceeded
Account log out is set to 15 minutes of inactivity.
## Identification and Authentication Policy for 18F

cloud.gov implements UAA which has session tokens and CSRF prevention that prevents replay attacks.
## JumpBox

Access keys and user accounts can be revoked using IAM. Sessions terminate after 10 minutes.
