id: ssp_template_sa_10
format: markdown
...
## System and Services Acquisition Policy for 18F

### Part a

Configuration and deployment of the cloud.gov platform is managed using the BOSH project. BOSH releases and deployment manifests are stored in GitHub; sensitive credentials are stored in Amazon S3 and are protected using both client- and server-side encryption.

### Part b

Changes to BOSH configuration are tracked in GitHub. Documentation is stored alongside deployment manifests and updated as configuration is changed; high-level documentation is also available at https://docs.cloud.gov.

### Part c

All proposed configuration changes are reviewed by members of the cloud.gov team. Proposed changes must pass unit, integration, and acceptance tests before being deployed.

### Part d

Configuration changes are made through pull requests in GitHub, which need to include documentation of all of the relevant context, as specified in 18F-wide policy here: https://github.com/18F/development-guide/tree/master/git_protocol#write-a-feature

### Part e

BOSH stemcell images and BOSH deployment artifacts are updated regularly, so that upstream security updates are applied.
