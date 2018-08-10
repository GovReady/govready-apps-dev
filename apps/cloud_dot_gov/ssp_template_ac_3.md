id: ssp_template_ac_3
format: markdown
...
## User Account and Authentication (UAA) Server

18F follows best practices by implementing the majority of the following:
  - Use RBAC model to restrict users’ access to only what is necessary to complete
their tasks.
  - Use a strong passphrase for both Cloud.gov user account and SSH keys.
  - Configure UAA clients and users using a BOSH manifest. Limit and manage these
clients and users as you would any other kind of privileged account. ## Application Security Groups
## Access Control Policies for 18F

18F information systems enforce approved authorizations for logical access to information and system resources in accordance with the 18F Access Control Policy Section 3 Access Enforcement which states:
  * 18F must enforce approved authorizations for logical access to its information
systems in accordance with all applicable federal and 18F policies.
  * 18F must provide access enforcement through the use of access control lists,
access control matrices, and cryptography to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, domains) in the information system.
  * 18F must employ access enforcement mechanisms at the application level, when
necessary, to provide increased information security for the organization. ## Identity and Access Management
