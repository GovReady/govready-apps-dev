id: ssp_template_cm_8
format: markdown
...
## Configuration Management Policy for 18F

18F posts its current inventory of information systems on its dashboard
located at  https://18f.gsa.gov/dashboard/. Several sources are used to capture
complete inventories of the virtual infrastructure and its information systems
while providing the level of granularity deemed necessary for tracking and reporting.
The AWS Management Console, VisualOps, Cloud Checkr, Github, and Nexpose are used
to provide additional enumeration capabilities.

Cloud Checkr is currently deployed to facilitate asset management, along with
other operations activities, on a real-time ongoing basis. Components deployed
in the virtual infrastructure are accurately inventoried and can be filtered to
a specific informaton system groups as well as a group of web services or  those
components that are related to a spcecific informaton system.

The VisualOps Cloud management tool is used to provide a visual, real-time and
automated representation of the virtual infrastructure and applications within
the 18F environment. It also provides a global view of the 18F AWS account where
all regions and services can be seen in one place.

The 18F GitHub repository also is used to show a current lists of components
that make up the cloud.gov inventory. It is located at https://docs.cloud.gov/ops/repos/

Nexpose maintains an inventory of all assets scanned within the 18F virtual Private
Cloud. This includes all information system within the VPCs and components within
the cloud.gov platform as a service.

Bosh continuously maintains inventory of all instances and configuration

cloud.gov operators review and update the information system component inventory
on a monthly basis and updates the inventory of information system whenever installations,
removals, and other changes are made. 18F will verify that all components within
the authorized boundary of the information system are either inventoried as part
of the system or recognized by another system as a component within that systems
inventory.
