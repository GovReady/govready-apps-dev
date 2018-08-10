id: ssp_template_au_2
format: markdown
...
## Audit and Accountability Policy for 18F

### Part b

Audit logs will be made available to organizations for mutual support in
response to security breaches, system and user access, incident reporting and
continuous monitoring. 18F will generate and distribute audit reports, provide
customized dashboard access for audited events, and send audit log data to SIEM
and log analysis systems from its audit logging and metrics tools for the
cloud.gov platform and virtual infrastructure as needed.

### Part c

18F retains audit logs according to NARA retention standards to provide support
for after-the-fact investigations of security incidents and to meet regulatory
and organizational information retention requirements. The log management
framework will provide the capability to retain logs for 90 days online and
one-year offline, with sufficient capacity as to mitigate the risk of exceeding
storage space.

Specific Policies, Procedures, Points of Contact, and Guidance will be established
between 18F and other agencies to support after-the-fact investigations, by the
18F Project Lead.
## Loggregator
## Cloud Checkr

### Part d

18F has implemented Cloudtrail and Cloudwatch for its account and system  monitoring. It provides visibility into user activity by recording API calls made on an AWS account. CloudTrail captures and records important information about each API call for the list of auditable events:
* User - the IAM user name of the person who was interacting with your AWS account.
* IP Address - the IP Address where the interactions originated from.
* Event Name - the type of interaction that occurred.
* Service - the AWS Service that was interacted with.
* Time - the date and time that the event occurred.
* Region - the AWS Region(s) where the interactions occurred.
* Resource ID - the resource ID from the event.
## ELKStack

### Part a

cloud.gov provides an audit trail through the bosh tasks command. This command shows all actions that an operator has taken with the platform. Additionally, operators can redirect Cloud Foundry component logs to a Logstash syslog server using the `syslog_daemon_config` property in the `metron_agent` job of cf-release.

For end users, cloud.gov records an audit trail of all relevant API invocations of and app. The CLI command cf events returns this information.
