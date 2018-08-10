id: ssp_template_au_3__1
format: markdown
...
## Audit and Accountability Policy for 18F

The Cloud.Gov information system generates audit records containing the following additional information:
session, connection, transaction, or activity duration; for client-server transactions, the number of bytes received
and bytes sent; additional informational messages to diagnose or identify the event; characteristics that describe or
identify the object or resource being acted upon.

Cloudtrail can generate a subset of audit records containing additional information within the AWS infrastructure.

EC2:
- Security Groups, Security Group Rules, Key Pairs, AMIs, Spot Instances, Reserved Instance, Instances, Volumes,
Snapshots, Placement Groups, Elastic Load Balancers (including attaching or detaching instances to them),
Network Interfaces, Elastic IPs
IAM:
  - Account Aliases, Account Summaries, Access Keys, MFA Devices, Policies, Password Policies, Groups, Users
S3:
  - Bucket Logging, Logging Target Bucket, Bucket Logging Prefix, Bucket Website Enabled, Bucket Website Index Document,
  Bucket Website Error Document, Bucket Notifications Enabled, Public Buckets, Bucket Notifications, Bucket Lifecycle Rules,
  Bucket Permissions

Cloud.Gov can generate additional audit information such as
- remote_addr, remote_user, request_status, bytes_sent, http_referer, http_user_agent, gzip_ratio
## Loggregator
