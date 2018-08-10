id: ssp_template_si_3
format: markdown
...
## System and Information Integrity Policy for 18F

### Part a

cloud.gov employs ClamAV at information system entry and exit points to detect and eradicate malicious code

### Part b

18F updates ClamAV whenever new releases are available in accordance with organizational configuration management policy and procedures

### Part c

18F configures ClamAV in cloud.gov to provide the following :

  1. Real-time scans of cloud.gov applied on either a daily or weekly schedule for file reads and writes

  2. Upon malicious code detection ClamAV identifies the virus in the file and quarantines it.  Once the virus is quarantined, ClamAV sends a notification to cloud.gov operators through Riemann

### Part d

cloud.gov addresses the receipt of false positives during malicious code detection and eradication and the resulting potential impact on the availability of the information system.
