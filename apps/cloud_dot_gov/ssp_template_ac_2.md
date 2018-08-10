id: ssp_template_ac_2
format: markdown
...
## User Account and Authentication (UAA) Server

### Part j

User accounts will be monitored monthly and accounts will be disabled after 90 days of inactivity; this will be a manual review process every 30 days, but the disablement will be automatic. A manual review of all user accounts will be conducted on an annual basis

### Part k

Cloud Foundry utilizes role based access controls (RBAC) for group membership within the platform and does not issue shared/group account credentials.
## Cloud Checkr

### Part j

User accounts will be monitored monthly and accounts will be disabled after 90 days of inactivity; this will be a manual review process every 30 days. 18F is in the process of automating this account management process through the use of implementing AWS OSQuery to trigger alerts when user accounts are inactive of a 90-day period.
## Access Control Policies for 18F

### Part a

The 18F Program identifies and selects the following types of
information system accounts to support organizational missions/business functions:

### Part b

18F has established designated DevOps personnel as the assigned
account managers for all information system accounts relating to the infrastructure
and the cloud.gov platform.
System Owners, whose web applications and/or websites
reside on the cloud.gov platform, have the responsibility to assign an account
manager for their information systems.

### Part c

18F establishes conditions
for group and role membership within the cloud.gov platform and its virtual
environment.
Conditions for groups and roles membership are based on an established
need to manage and access the virtual infrastructure and cloud.gov environments.
The user must meet the following conditions in order for the System Owner / Project
Manager to approve a group membership request:
  * The user’s assigned role is required to access a particular group.
  * The user has the requirements and understanding to assume permissions associated with the group.
  * The user has completed the security role-based training.
  * The user complies with any other group-specific conditions created by the system owner.
Once conditions have been met, the System Owner / Project Manager will request access within
GitHub, 18F’s tracking and ticketing system. Once approved, the 18F DevOps group
completes the request for group and role membership within its infrastructure
and cloud.gov platform.

### Part d

The 18F Program Office specifies authorized
users of the information system, group and role membership, and access authorizations
(i.e., privileges) and other attributes (as required) for each account. System
Owners / Project Managers provide the details of what type of access is needed
for an authorized authorized user.
All accounts will be documented within their
respective information systems, detailing their group and role membership, and
access authorizations. This documentation will be exported by DevOps and archived
for up to a year from the date of account creation by the managing 18F project
lead and cloud.gov Technical Point of Contact (Operating Environment) in accordance
with best business and security practices.

### Part e

18F requires approvals by the project lead and system owners for requests to create information system
accounts. All accounts will be documented within the GitHub ticketing and tracking
system with their respective information systems, detailing their group, role
membership, and access authorizations.

### Part f

User account establishment,
activation, modification, disablement or removal requires approval by the managing
\ project lead and cloud.gov Information System Technical Point of Contact.
Accounts will be created, enabled, modified, disabled, and removed from AWS in accordance
with 18F policies, guidelines and established by the project lead and DevOps.

### Part g

18F monitors the use of all information system accounts within
its environment.

### Part h

18F notifies its DevOps account managers when accounts are no longer required, users are terminated or transferred, and when
individual’s information system usage or need-to-know changes within the cloud.gov
platform and virtual private cloud infrastructure.
The Project Manager or Information
System Owner will be notified when accounts have been terminated, disabled or
transferred based on the access request submitted via GitHub.  Notification
will be sent via email or the GitHub ticketing and tracking system when changes
to user and system access occur.

### Part i

18F authorizes access to its
information systems based on a valid access authorization from System Owners
and DevOps, intended system usage within the network environment, and other
attributes as required by the organization or associated missions/business functions.
This is documented within section 3 of the 18F Access Control Policy: Access
Management.
User and system access is provided only to those with an established
need to access and manage the virtual private cloud and cloud.gov environments.
* User group membership is restricted to the least privilege necessary for the user to accomplish their assigned duties.
* All user accounts are issued only to those who have gained approval by 18F DevOps.
Once approved, the DevOps team creates the user account and adds it to the appropriate role and organization
within its information systems.
18F grants access to the information system
based on:
  * A valid need-to-know/need-to-share that is determined by assigned official duties and satisfying all personnel security criteria.
  * Intended system usage.
18F requires proper identification for requests to establish information
system accounts, and it approves all such requests based on organizational or mission/business
function attributes.

### Part j

18F reviews user and system accounts for compliance with account management requirements at least on an annual basis.
\ Currently, system and user accounts are being monitored manually on a monthly
basis and programmatically on a continuous basis.

### Part k

18F establishes a process for reissuing shared/group account credentials when individuals are
removed from the group. 18F uses its GitHub tracking and ticketing system
for requests to reissue and remove individuals from group memberships within
its environment.
## Identity and Access Management
## Cloud Controller
## ELKStack

### Part g

The UAA API interface is used to monitor privileged/non privileged user accounts within the cloud.gov It lists Cloud Foundry instance users. By default it returns information about each user account including GUID, name, permission groups, activity status, and metadata.

18F uses the ELK stack to provide a visual way to monitor all user and system accounts within cloud.gov by interfacing with cloud.gov API calls to its internal system components (i.e. Loggregator, Cloud Controller, DEA, Warden, Metrics Collector)
