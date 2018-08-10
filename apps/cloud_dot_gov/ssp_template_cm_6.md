id: ssp_template_cm_6
format: markdown
...
## Configuration Management Policy for 18F

### Part a

18F uses established and documents configuration settings
for its information technology products employed within the Cloud Foundry platform
that reflect the most restrictive mode consistent with operational requirements.
18F follows industry best practices and guidance provided in NIST Special Publication
800-70, Security Configuration Checklist Program for IT Products

Infrastructure documented configuration settings:
cloud.gov operators maintain the
baseline configuration for VPC, EBS and AMIs.  Best practices, FISMA compliant
AMIs, and hardened cloud formation templates are utilized as there are no benchmarks
available. 18F uses the following approved FISMA ready baselines located at
https://github.com/fisma-ready

Cloud Foundry documented configuration settings:
18F follows Cloud Foundry best practices for configuring and implementing the
platform as a service. Configuration settings are documented within the deployment
manifest on the GitHub and Cloud Foundry websites. The following are approved
baseline configuration settings related to the Cloud Foundry platform as a service.
All documented configuration settings  related to Cloud Foundry are located
at https://docs.18f.gov/ops/repos/.

### Part b

18F Implements the configuration
settings based on its documented process and practices. cloud.gov operators implement the
configuration benchmarks identified in Part a, maintains the baseline configuration
for all cloud infrastructure and Cloud Foundry components and is responsible
for ensuring all systems are configured in accordance with applicable hardening
guides.

### Part c

cloud.gov operators document any exceptions to established baseline
configurations for all of 18F's virtual infrastructure and information systems.
18F maintains exception documents which detail specific items from the established
configuration settings which cannot be applied to instances due to operational
requirements.

### Part d

18F Monitors and controls changes to the configuration
settings in accordance with its documented configuration management policy and
procedures.

All Configuration Change Control:
cloud.gov operators and 18F system owners maintain the baseline configurations within
18F Virtual Private Cloud. Configuration will be reviewed in real-time using
automated methods and at least quarterly to ensure no unauthorized changes
were made to the baseline configuration.

Internal vulnerability scans are performed at least on a quarterly basis in the
event that no enhancements or upgrades are performed.
