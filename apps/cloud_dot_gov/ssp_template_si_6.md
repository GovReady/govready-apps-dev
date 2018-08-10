id: ssp_template_si_6
format: markdown
...
## System and Information Integrity Policy for 18F

### Part a

cloud.gov verifies the correct operation of services that detect malicious code, viruses, file integrity, network traffic, and security compliance of the OS using a contious integration tool called concourse.  
concourse is a contious integration tool that auotmates the build of security services in cloud.gov.

### Part b

Performs this verification on daily basis using concourse pipelines

### Part c

concourse notifies cloud.gov operators of failed security verification tests

### Part d

In the event the a service does not operate correctly, monit will attempt to restart the service upon failure.  If the system is unresponsive then Bosh will restart the server in order to correct the operation of the service.
