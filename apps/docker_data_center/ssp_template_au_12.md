id: ssp_template_au_12
format: markdown
...
## Docker Enterprise Edition (Engine)

### Part a

'Both Universal Control Plane and Docker Trusted Registry backend
service containers, all of which reside on Docker Enterprise Edition,
log all of the event types indicated by this AU-2 a. These and other
application containers that reside on Docker Enterprise Edition can be
configured to log data via an appropriate Docker logging driver.
Additional information can be found at the following resources:

- https://docs.docker.com/engine/admin/logging/overview/

The underlying Linux operating system supporting Docker Enterprise
Edition can be configured to audit Docker-specific events with the
auditd daemon. Refer to the specific Linux distribution in use for
instructions on configuring this service.'

### Part b

'Using auditd on the Linux operating system supporting CS Docker
Engine, the organization can configure audit rules to select which
Docker-specific events are to be audited. Refer to the specific Linux
distribution in use for instructions on configuring this service.'
## Universal Control Plane (UCP)

### Part a

'All of the event types indicated by AU-2 a. are logged by the backend
ucp-controller service within Universal Control Plane. In addition,
each container created on a Universal Control Plane cluster logs event
data. Additional information can be found at the following resources:

- https://docs.docker.com/datacenter/ucp/2.1/guides/admin/configure/store-logs-in-an-external-system/

The underlying Linux operating system supporting UCP can be configured
to audit Docker-specific events with the auditd daemon. Refer to the
specific Linux distribution in use for instructions on configuring
this service.'

### Part b

'Using auditd on the Linux operating system supporting UCP, the
organization can configure audit rules to select which Docker-specific
events are to be audited. Refer to the specific Linux distribution in
use for instructions on configuring this service.'
## Docker Trusted Registry (DTR)

### Part a

'All of the event types indicated by AU-2 a. are logged by a
combination of the backend services within Universal Control Plane and
Docker Trusted Registry. Additional information can be found at the
following resources:

- https://docs.docker.com/datacenter/dtr/2.1/guides/monitor-troubleshoot/

The underlying Linux operating system supporting DTR can be configured
to audit Docker-specific events with the auditd daemon. Refer to the
specific Linux distribution in use for instructions on configuring
this service.'

### Part b

'Using auditd on the Linux operating system supporting DTR, the
organization can configure audit rules to select which Docker-specific
events are to be audited. Refer to the specific Linux distribution in
use for instructions on configuring this service.'
