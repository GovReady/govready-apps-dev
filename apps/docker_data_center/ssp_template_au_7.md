id: ssp_template_au_7
format: markdown
...
## Docker Enterprise Edition (Engine)

### Part a

'Docker Enterprise Edition can be configured with various logging
drivers to send audit events to an external logging stack. The logging
stack can subsequently be used to facilitate the audit reduction and
report generation requirements of this control. Additional information
can be found at the following resources:

- https://docs.docker.com/engine/admin/logging/overview/'

### Part b

'The underlying operating system chosen to support Docker Enterprise
Edition should be certified to ensure that logs are not altered during
generation and transmission to a remote logging stack.'
## Universal Control Plane (UCP)

### Part a

'Universal Control Plane can be configured to log data to a remote
logging stack. The logging stack can subsequently be used to
facilitate the audit reduction and report generation requirements of
this control. Additional information can be found at the following
resources:

- https://docs.docker.com/datacenter/ucp/2.1/guides/admin/configure/store-logs-in-an-external-system/'

### Part b

'The underlying operating system chosen to support Universal Control
Plane should be certified to ensure that logs are not altered during
generation and transmission to a remote logging stack.'
## Docker Trusted Registry (DTR)

### Part a

'Universal Control Plane can be configured to log data to a remote
logging stack, which in turn, sends the Docker Trusted Registry
backend container audit records to the remote logging stack. The
logging stack can subsequently be used to facilitate the audit
reduction and report generation requirements of this control.
Additional information can be found at the following resources:

- https://docs.docker.com/datacenter/ucp/2.1/guides/admin/configure/store-logs-in-an-external-system/'

### Part b

'The underlying operating system chosen to support Docker Trusted
Registry should be certified to ensure that logs are not altered
during generation and transmission to a remote logging stack.'
