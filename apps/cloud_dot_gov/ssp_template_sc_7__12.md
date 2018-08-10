id: ssp_template_sc_7__12
format: markdown
...
## System and Communications Protection Policy for cloud.gov

### Part b

Host-based boundary protection for application services hosted on cloud.gov are provided by CF components.

Cloud Foundry Application Security Groups (ASGs) control the traffic flowing out of applications. Each CF application uses a dedicated Linux container, and each container includes a dedicated virtual network interface. Application security groups are a collection of ‘allow’ rules that can be made with global or application specific assignments enabling access to be set on individual application requirements. These requirements are added through whitelisting, and whitelisting is layered on top of a series of container-centric lock-downs, allowing limited access to other applications and services.
