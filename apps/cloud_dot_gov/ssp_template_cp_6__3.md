id: ssp_template_cp_6__3
format: markdown
...
## Contingency Planning Policy for 18F

18F will identify it’s on premise locations from which there could be an accessibility issue, and devise contingency
operations for accessing its AWS resources from other locations.  18F will implement any failover to cloud.gov implementations
it has deployed in alternate AWS regions for public-facing systems, using services such as Amazon Route 53 DNS.

All Availability zones and Regions are accessible via the same means: AWS console and remote API calls can be made from
other networks across the public Internet, provided the appropriate credentials are supplied.
