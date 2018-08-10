id: ssp_template_si_2
format: markdown
...
## CI cloud.gov Concourse Pipeline

### Part b

Tests software and firmware updates related to flaw remediation for effectiveness and potential side effects before installation.

### Part c

Installs security-relevant software and firmware updates within 30 days release of updates of the release of the updates.

### Part d

18F incorporates flaw remediation into the its configuration management process. New versions of cloud.gov can easily recreated and deployed in the event of any system flaws.
## System and Information Integrity Policy for 18F

### Part a

18F identifies all system flaws related to cloud.gov, reports system flaws to information system owners, Authorizing officials, cloud.gov operators, and corrects information system flaws that affect cloud.gov.

### Part b

18F tests software updates against a staging environment for any updates, including those related to flaw remediation, for effectiveness and potential side effects before deploying the updates to production environment.
Cloud Foundry manages software vulnerability using releases and BOSH stemcells.
New Cloud Foundry releases are created with updates to address code issues, while new
stemcells are created with patches for the latest security fixes to address
any underlying operating system issues. New Cloud Foundry releases are located
at https://github.com/cloudfoundry/cf-release.

### Part c

Installs security-relevant software and firmware updates within [FedRAMP Assignment: Within 30 days of release of updates] of the release of the updates

### Part d

18F incorporates flaw remediation into the organizational configuration management process.

18F implements the release of Cloud Foundry and (or the software
developer/vendor in the case of software developed and maintained by a
vendor/contractor) promptly installs newly released security relevant
patches and tests patches, for effectiveness and potential
side effects on information systems before installation.
