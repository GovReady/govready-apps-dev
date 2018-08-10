id: ssp_template_ac_6__9
format: markdown
...
## Cloud Checkr

All privileged user account activity and API calls to cloud.gov are
audited by CloudTrail and monitored by CloudWatch. CloudTrail provides a log of
all requests for AWS resources within the 18F AWS account. For each event recorded,
18F can see what service was accessed, what action was performed, any parameters
for the action, and who made the request. Cloudtrail also shows whether it was
as the AWS root account user or an IAM user, or whether it was with temporary
security credentials for a role or federated user.
## Access Control Policies for 18F

* Privileged access to the information system is using an audit trail through
the BOSH tasks command. This command shows all actions that an operator has
taken with the platform. Additionally, all logging activity is forwarded to
CloudWatch Logs.
* ELK (Logstash, Elasticsearch, Kibana) is used to collect, manage and display
all user activity within the cloud.gov platform.
## ELKStack

The ELK (elasticsearch, Logstash, Kibana) is used to collect, manage and display all auditing of privileged functions within the cloud.gov platform.
