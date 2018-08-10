id: ssp_template_cp_6
format: markdown
...
## Contingency Planning Policy for 18F

### Part a

cloud.gov will leverage the AWS IaaS for its Alternate storage site capabilities. This implementation employs the use of
multiple Availability Zones within one AWS Region, which constitute a built-in alternate storage site capability for data
stored in Amazon S3 and Amazon RDS databases.  S3 uses multiple availability zones by default, and RDS databases deployed
by this package are replicated across multiple availability zones.

### Part b

Through leveraging the AWS infrastructure as a service 18F ensures that the alternate storage site provides information
security safeguards equivalent to that of the primary site for Cloud.Gov.  The multiple AWS availability zones employed
by Amazon S3 storage and Amazon RDS replication provide identical security safeguards.
