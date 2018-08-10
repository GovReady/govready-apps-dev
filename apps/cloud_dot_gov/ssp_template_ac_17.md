id: ssp_template_ac_17
format: markdown
...
## Access Control Policies for 18F

### Part a

cloud.gov has a distributed administrator, operator, and management team. All remote actions are
allowed.

### Part b

AWS Security Groups are implemented to ensure that only users that have been granted access can
perform administrative actions.
## JumpBox

cloud.gov remote access is not available outside of the 18F environment. 18F DevOps personnel are the only group who connects to information system remotely using SSH (22) through the jump box (bastion Host) to execute BOSH CLI commands. The JumpBox is a virtual machine (VM) that acts as a single access point for the BOSH Director and deployed VMs. For resilience there are at least 2 jump boxes. Allowing access through jump boxes and disabling direct access to the other VMs is a common security measure 18F incorporates.

The jumbox only serves as a means to execute BOSH CLI commands for the platform. It cannot access any applications or websites hosted on top of the platform.

JumpBoxes are logged in in the same way an EC2 instances is logged into. The system has both a firewall and user ssh key logins.

The 18F Access Control Policy Section 3 - Remote Access states:

* 18F shall define, document and enforce requirements, usage restrictions and implementation guidance for each allowed remote access method.
* Remote and Virtual Private Network (VPN) access shall require multi-factor authentication.
* Access shall be authorized before a connection may be established.
* 18F shall monitor for unauthorized remote access and shall take appropriate action if unauthorized access is discovered.
* Remote access shall employ cryptography to protect session confidentiality and integrity.
* Remote access shall be routed through a limited number of managed access control points.
* Privileged commands and access to security-relevant information via remote access shall only be permitted as described in the System Security Plan (SSP).
