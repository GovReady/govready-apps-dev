id: ssp_template_ca_7
format: markdown
...
## Security Assessment and Authorization Policy for 18F

### Part a

The organization-defined metrics are collected by a combination of AWS CloudWatch (in real time, CPU Utilization, Disk IO, Network In/Out), application logging policy (see AU-2) and a vulnerability scanner.

### Part b

AWS CloudWatch Metrics (CPU Utilization, Disk IO, Network In/Out) are collected in real time. Other metrics are collected in frequencies ranging between 5 minutes and 1 hour. Host vulnerability scans are run daily.

### Part c

Compliance with security controls that can be tested from the operating system level (eg. presence of configuration settings, etc) are monitored and automatically corrected as part of configuration management. Non-automated security processes are handled by the cloud.gov operations team.

### Part d

See CA-7(c)

### Part e

See CA-7(c)

### Part f

Response actions will use the mitigation strategy defined in RA-5(d).

### Part g

Reporting of the security status of the system will be provided by the cloud.gov team according to the Federal and FedRAMP requirements on a monthly basis.
