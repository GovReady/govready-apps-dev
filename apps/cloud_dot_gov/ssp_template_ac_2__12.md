id: ssp_template_ac_2__12
format: markdown
...
## Cloud Checkr

### Part a

18F has implemented Cloud Checkr as a way to monitor information system accounts. CloudCheckr monitors the 18F AWS infrastructure and alerts the DevOps and SecOps when certain conditions are met. The CloudTrail Built-In Alerts allows 18F to monitor for a recommended predefined set of CloudTrail events.
These events include:
* Any security-related event
* CloudTrail disabled
* Credentials report generated
* EBS snapshot deleted
* EC2 instance terminated
* Failed login to AWS Management Console
* IAM access key created
* IAM access key deleted
* IAM password policy changed
* IAM policy assigned
* IAM policy modified
* Resource-based policy modified
* Role Assumed
* Root account access key created
* Root account used
* Security group assigned
* Security group modified
* Successful login to AWS Management Console
* Unauthorized access attempt

### Part b

Cloud Checkr reports atypical usage of information system accounts to designated 18F SecOps and Devops teams. Monitoring and intrusion information contained within Cloud Checkr and Cloudtrail logs are  sent to 18F security personnel. The  logs are protected from unauthorized access by limiting access to authorized privileged users only.
## ELKStack

### Part a

Information system account activities are monitored via ELK

### Part b

ELK reports atypical usage of information system accounts to designated Infrastructure and cloud.gov operators teams.
