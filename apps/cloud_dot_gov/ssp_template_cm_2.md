id: ssp_template_cm_2
format: markdown
...
## Cloud Formation
## BOSH
## Configuration Management Policy for 18F

For AWS Baseline Configurations:

AWS Cloud Formation templates, CIS Level 1 benchmarks and any GSA/18F benchmarks such as hardening guidelines
and baselines are the approved baseline for all changes to the infrastructure and simplify provisioning and management
on AWS. They provide an automated method to assess the status of an operational infrastructure against an approved
baseline.

Windows and Linux instances are based on the standard AWS AMI images in accordance with GSA configuration requirements.

For cloud.gov Baseline Configurations:

cloud.gov utilizes customized Ubuntu stemcells and deployment manifest yaml files for its baseline configurations.
The list of the configuration settings can be found at the following site https://docs.cloud.gov/ops/repos/

A stemcell is a versioned Operating System image wrapped with IaaS specific packaging. A typical stemcell contains
a bare minimum OS skeleton with a few common utilities pre-installed, a BOSH Agent, and a few configuration files
to securely configure the OS by default. With AWS, official stemcells are published as AMIs that can be used in the
18F AWS account. Stemcells do not contain any specific information about any software that will be installed once
that stemcell becomes a specialized machine in the cluster; nor do they contain any sensitive information which
would make them unable to be shared with other BOSH users.  The deployment manifest is a YAML file that defines
the components and properties of the deployment.

Note: Additional OS/Device-specific industry standards and guidance may also be used whenever appropriate. It is
understood that when industry standards are adopted they may need to be adapted for the specific implementation
and if/where this has occurred it should be mentioned/referenced. 18F ensures that the most current, relevant
OS/Device-specific industry standards and guidance is maintained where appropriate to support cloud.gov configurations.
These best practice updates are captured during the annual review of the CM Policy which also incorporates 18 procedures.
