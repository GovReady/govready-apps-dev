id: ssp_template_ac_17__4
format: markdown
...
## Amazon Virtual Private Cloud
## Access Control Policies for 18F

### Part a

18F authorizes the execution of privileged commands and access to security-relevant information via remote access only for monitoring, managing, and troubleshooting the 18F virtual infrastructure and cloud.gov platform. This authorization is only given to specific members of the DevOps and SecOps teams. All other members are excluded from this type of access.
## JumpBox

18F authorizes the execution of privileged commands and access to security-relevant information via remote access only for monitoring, managing, and troubleshooting  the 18F virtual infrastructure and cloud.gov platform. This authorization is only given to specific members of the DevOps and SecOps teams. All other members are excluded from this type of access.

Since the cloud.gov platform resides within the 18F virtual infrastructure, 18F DevOps must use the SSH remote access method to troubleshoot issues and update services that are only resolved by logging into the cloud.gov jumpboxes. The jumpbox itself a virtual machine deployed within the cloud.gov virtual private cloud. It is the only access point for designated DevOps members to run privileged commands that affect the entire platform. No other privileged remote access is available to the information system.
