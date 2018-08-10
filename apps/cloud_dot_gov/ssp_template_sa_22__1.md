id: ssp_template_sa_22__1
format: markdown
...
## System and Services Acquisition Policy for 18F

18F will replace information system components when support for the components is no longer available from the developer, vendor, or manufacturer; and will provide justification and documented approval for the continued use of unsupported system components required to satisfy mission/business needs.

Cloud Foundry Platform as a Service system replacement:

A system and software inventory is run nightly, and the DevOps team reviews the inventory weekly to ensure that all software inventoried is accurate and currently supported. This process includes:

* Verify that the software license support expiration date is not within six months. 18F uses the open source version of Cloud Foundry which uses the open source Apache 2.0 license.
* Ensure that the software version is still supported.
* Refer to the vendor's support website to verify that support does not have an \u201CEnd of Life\u201D date of less than six months.

Since 18F is using the open source version of Cloud Foundry, an additional task will be issued to upgrade the Cloud Foundry suite to the latest versions. DevOps will review the GitHub cloudfoundry/cf-release repository for implementation of the updated version.
