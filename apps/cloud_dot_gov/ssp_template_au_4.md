id: ssp_template_au_4
format: markdown
...
## S3
## Audit and Accountability Policy for 18F

cloud.gov audit logs are stored within the elasticsearch component of
the ELK stack which is clusterd for redundancy and failover functions. This solutions
provide the capability to extend the audit storage capacity without the likelihood
of the capacity being exceeded. 18F plans to incorporate the use of the S3 cloud
service for greater storage capacity if needed.
