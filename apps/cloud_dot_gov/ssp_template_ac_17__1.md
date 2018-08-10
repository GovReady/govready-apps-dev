id: ssp_template_ac_17__1
format: markdown
...
## Cloud Checkr

Cloud Checkr provides a unified view of all infrastructure monitoring which captures all remote activities within 18F virtual infrastructure. The log files are organized by AWS Account ID, region, service name, date, and time. CloudTrail can be configured to aggregate log files from multiple regions into a single Amazon S3 bucket. From there, 18F Devops and SecOps teams view the logs files within Cloud Checkr to perform security analysis and detect user behavior patterns.
## ELKStack

The Cloud Controller authenticates every request with the Service Broker API using HTTP or HTTPS. The cloud.gov operators only uses the BOSH Command Line Interface (CLI) to log into the cloud.gov jumpbox using SSH as a remote connection. These remote connections are monitored by the cloud.gov Cloud Controller which send this data to the ELK logging and monitoring visualization tool stack.
