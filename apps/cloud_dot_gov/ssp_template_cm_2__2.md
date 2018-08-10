id: ssp_template_cm_2__2
format: markdown
...
## Configuration Management Policy for 18F

Configuration management at the AWS level is managed through CloudFormation automation templates, AWS Config and
VisualOps. 18F maintains baseline configurations for VPC, EBS, EC2 instances and AMIs. AWS Cloud Formation templates
help maintains a strict configuration management scheme of the cloud.gov. Because these templates are text files, 18F
can simply track differences in these templates to track changes to its infrastructure.

For cloud.gov, an operator initiates a new deployment using the BOSH CLI, the BOSH Director receives a version of the
deployment manifest and creates a new deployment using this manifest. Automated Configuration of cloud.gov platform
components is handled by the Concourse.ci, a continuous integration and deployment tool which utilizes the cloud.gov
customized Ubuntu stemcells and deployment manifest yaml files for its baseline configurations.
