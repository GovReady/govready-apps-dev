id: ssp_template_ac_5
format: markdown
...
## Access Control Policies for 18F

### Part a

18F implements Identity and Access Management (IAM)
roles and individual user accounts for separation of duties at the AWS layer.
For Cloud Foundry access, cloud.gov uses UAA role based access controls (RBAC) to
maintain separation of duties.

### Part b

18F documents separation of duties of AWS and Cloud Foundry users.  All AWS IAM
users, groups and roles can be viewed within the AWS console. IAM users reports
are generated to show all separation of duties. Cloud Checkr also generates
a report of all IAM users within the 18F AWS environment.

### Part c

cloud.gov defines roles at each layer of the system. Authorization to each
of those roles is defined within the documentation of the setup and maintenance
of the layers.
## Identity and Access Management
## Cloud Controller
