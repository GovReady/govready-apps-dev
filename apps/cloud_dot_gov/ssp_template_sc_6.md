id: ssp_template_sc_6
format: markdown
...
## System and Communications Protection Policy for cloud.gov

cloud.gov protects the availability of resources by allocating
volatile and non-volatile storage, bandwidth, and availability by using automated
AWS features such as Elastic Load Balancing and Auto Scaling technology at the
infrastructure layer and Cloud Foundry's application lifecycle manager components,
Cloud Controller and Droplet Execution Agent (DEA), at the application layers.

18F safeguards are in place if resources are reaching their limits with multiple sets of
resource monitoring tools:  Cloud Foundry's built-in health monitoring system, New Relic,
CloudWatch, and ELK, which combined provide real-time alerts and visibility into critical
systems and applications.
