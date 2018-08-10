id: ssp_template_au_6
format: markdown
...
## Audit and Accountability Policy for 18F

### Part a

AWS Auditable Events:
DevOps and SecOps teams will conduct weekly manual and automated continuous
audits of authorized accounts and configurations. These audits will include
but are not limited to:

Administrative Accounts

* Virtual Private Cloud (VPC)
* Elastic Compute Cloud (EC2)
* Simple Storage Service (S3)
* Identity and Access Management (IAM)
* Elastic Block Store (EBS)

Cloud Foundry Auditable Events:
By default, Loggregator streams logs to a terminal. 18F will drain logs to
a third-party log management service such as ELK and AWS CloudTrail Cloud
Foundry logs are captured in multiple tables and log files. These will be
reviewed weekly and if discovery of anomalous audit log content which appears
to indicate a breach are handled according to the GSA Security Incident
Handling Guide: CIO IT Security 01-02 Revision 7 (August 18, 2009) requirements.

### Part b

When a credible source to the GSA Agency provides information that causes
reason to enhance audit activities, develop and implement an enhanced auditing
use-case that will adequately enhance auditing practices in a fashion necessary
per the identified threat and following the Incident Reporting Procedures in
GSA IT Security Procedural Guide 01-02 (04/07/2015), Incident Response. The GSA
Agency may also, through analysis pertaining to the GSA Agency environment
provide additional audit measures that will require an increase in review,
analysis, and reporting for a necessary.

Upon implementation, 18F will monitor information security news and alerts for
indications of a need to heighten information system security monitoring.
