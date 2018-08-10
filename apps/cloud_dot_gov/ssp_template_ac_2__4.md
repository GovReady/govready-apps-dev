id: ssp_template_ac_2__4
format: markdown
...
## User Account and Authentication (UAA) Server

All account activity is logged using the UAA system which can be reviewed for auditing purposes.
## Cloud Checkr

#TODO
18F has implemented CloudWatch for its system account monitoring. It monitors resources in near real-time, including EC2 instances, EBS volumes, Elastic Load Balancers, and RDS DB instances. Metrics such as CPU utilization, latency, and request counts are provided automatically for these AWS resources. It allows 18F to supply logs or custom application and system metrics, such as memory usage, transaction volumes, or error rates.

CloudTrail captures all IAM API calls from  command-line tools, the AWS SDK, and the AWS Management Console. Monitoring data is retained for two weeks, even if AWS resources have been terminated. This enables 18F to quickly look back at the metrics preceding an event of interest.

Metrics are accessed in either the EC2 tab or the CloudWatch tab of the AWS Management Console. SecOps personnel monitors the use of all infrastructure accounts through Cloud Checkr
## ELKStack

cloud.gov provides an audit trail through the bosh tasks command which shows all actions that an operator has taken with the platform. It also records an audit trail of all relevant API invocations of an app. The CLI command cf events returns this information.

ELK ( Logstash, Elasticsearch, Kibana) a front end component for loggregator is used to automatically audit all actions within the cloud.gov platform. By binding an instance of the service to, cloud.gov applications logs will be drained to a Logstash syslog receiver and stored in Elasticsearch to perform real-time data analytics with Kibana as the interface for search and visualization.
