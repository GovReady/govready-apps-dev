id: ssp_template_sc_5
format: markdown
...
## System and Communications Protection Policy for cloud.gov

Refer to the 18F policy statement for the types of denial of service (DoS) to protect our systems against. Policy https://github.com/18f/compliance-docs/blob/master/SC-Policy.md

cloud.gov limits the effects of Volume Based and Protocol DoS type attacks by utilizing the following groups of technical measures:

18F administrative staff maintains hardened Amazon Managed Images (AMI) and Cloud Foundry custom buildpacks with the latest patches and updates.

Buildpacks provide framework and runtime support for applications that are deployed on cloud.gov.  The AMI and custom buildpacks are maintained and secured within 18F's software repository, GitHub.

cloud.gov also uses AWS's IaaS services with well-formed Virtual Private Cloud (VPC) firewall rules to reduce the attack surface, while service resiliency is maintained by utilizing AWS Availability Zones, Elastic Load Balancing, and Auto Scaling services.

Cloud Foundry's security components limit the effects of an attack at the Application Layer. It limits DoS attacks on this layer through resource starvation and reduction of the attack surface even further with well-formed application security groups which control the traffic flowing from hosted applications.

These tools combined with SOC staffing are responsible for maintaining system security.
