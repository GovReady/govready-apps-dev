id: ssp_template_sc_7__3
format: markdown
...
## System and Communications Protection Policy for cloud.gov

18F limits the number of external network connections to the information system through the use of AWS network security groups which restrict types of network connections. AWS API authenticated service keys and managed SSH keys restrict PU access to the systems.

cloud.gov Cloud Foundry components run on AWS AMI that exist within AWS VPCs. In this configuration, the only access points visible on a public network are load balancers that map to one or more Cloud Foundry routers.
