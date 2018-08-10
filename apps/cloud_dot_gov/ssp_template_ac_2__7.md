id: ssp_template_ac_2__7
format: markdown
...
## User Account and Authentication (UAA) Server

### Part b

UAA centralizes all role assignment and all user management activity is logged and monitored.
## Cloud Checkr

### Part b

18F monitors all privileged role assignments to the VPS through the IAM console, CloudTrail audit logs and Cloud Watch alerts. 18F uses Cloud Checkr to provide centralized monitoring and alerting within its VPC.
## Access Control Policies for 18F

### Part a

cloud.gov UAA allows the creation of limited privileged accounts.
Roles are created by the administrators on a need by need basis.
Cloud Foundry roles are granularly granted depending on the requirements
of each organization within the platform.

### Part c

18F removes users from privileged access rights when privileged role assignments are no longer appropriate or have been requested by the system owner and program manager. Removal of access is sent to the DevOps team through a change request within the GitHub ticketing system.
## ELKStack

### Part b

18F monitors all privileged access API calls through the Cloud Foundry command line interface and BOSH command line interface within cloud.gov. These API calls are monitored through ELK.
