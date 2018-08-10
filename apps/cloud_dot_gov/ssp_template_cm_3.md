id: ssp_template_cm_3
format: markdown
...
## Cloud Formation
## Cloud Checkr

### Part c

For changes related to the virtual infrastructure, 18F uses VisualOps and Cloud Checkr for real-time configuration changes which are documented, approved and tracked within GitHub. All Cloud Foundry configuration changes are documented, approved and tracked within 18F's GitHub site.
## Configuration Management Policy for 18F

### Part a

All Configuration Change control:
18F provisions its infrastructure with AWS CloudFormation, the AWS CloudFormation
template describes exactly what resources are provisioned and their settings.
Because these templates are text files, 18F can simply track differences in
these templates to track changes to its infrastructure, similar to the way
developers control revisions to source code.

18F uses version control systems with its cloud formation templates to know
exactly what changes were made, who made them, and when. If at any point 18F
needs to reverse changes to infrastructure, you can use a previous version of
a template.

18F uses GitHub for additional tracking and documenting of authorized changes
within the infrastructure and applications including Cloud Foundry platform as
a service. Within GitHub, a diff function is used to compare and contrast any
changes made to configurations of Cloud Foundry.

### Part b

18F reviews proposed configuration-controlled changes to all of its information
systems and infrastructure and approves or disapproves such changes with explicit
consideration for security impact analysis within the Virtual Private Cloud
environment. All reviews and approvals are conducted within 18Fs GitHub ticketing
and tracking system.

### Part c

18F uses the following methods to document configuration change decisions
associated with its information systems.  For changes related to the its
virtual infrastructure, 18F uses VisualOps and Cloud Checkr for real-time
configuration changes which are documented, approved and tracked within GitHub.
All Cloud Foundry configuration changes are documented, approved and tracked
within 18F's GitHub site.  All configuration changes related to applications
and websites hosted within the 18F AWS and Cloud Foundry environment are
requested by the systems owner and approved by cloud.gov operators within the 18F GitHub
tracking systems.

### Part d

When configuration changes have been approved through 18F's GitHub
ticketing and tracking system, the cloud.gov operators team implements approved configuration-controlled
changes to the information system and then provides a status of the changes
completed and closes out the ticket.

### Part e

Records of configuration-controlled
changes are retained for at least 1 year in accordance with the 18F Configuration
Management policy and utilizing the 18F GitHub site and S3 to store all changes
requested, approved, disapproved, implemented and pending.

### Part f

Audits for the virtual infrastructure and Cloud Foundry platform as a
service and applications are conducted by cloud.gov operators, ISSOs and Cloud Foundry
project manager of all configuration-controlled changes to the information
system.  These audits take place no less than once a month and are documented
in the GitHub ticketing and tracking system, per the 18F Configuration
management policy Section 3 which states

18F will conduct a monthly audit of information system which identifies and
eliminates unnecessary functions, ports, protocols, and/or services.

### Part g

18F coordinates
and provides oversight for configuration change control activities through its
GitHub tracking and ticketing systems and Slack communications channel which
is integrated with GitHub that convenes whenever there are significant and pending
changes to the 18F security, cloud infrastructure and applications.
