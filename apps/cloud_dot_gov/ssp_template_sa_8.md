id: ssp_template_sa_8
format: markdown
...
## System and Services Acquisition Policy for 18F

cloud.gov uses the Cloud Foundry secure deployment best practices, which include the following:
  - Configure UAA clients and users using a standard BOSH manifest for Cloud Foundry
Development.
  - cloud.gov develops and maintains documentation on the baseline configuration
of the information system that include network topology, system architecture, application, web, and server components along with software standards.
  - Cloud Foundry protects the information system from security threats by minimizing
network surface area, applying security controls, isolating applications and data in containers, and encrypting connections.
  - It also implements role-based access controls, applying and enforcing permissions
to isolate user to their space.  Baseline configurations settings are reviewed on a continual basis to to comply with federal mandates and compliance standards.
  - cloud.gov documents changes to the baseline configuration in GitHub for review.
Part of this process includes a thorough security analysis of the proposed change prior to the configuration change being implemented on the operational system.
  - cloud.gov deploys with every application a standard set of tools for security
and monitoring of each application to identify security issues. For more details please refer to 18F Configuration Management Policy and security controls CM-2, CM-3, and CM-6.
