id: ssp_template_au_2
format: markdown
...
## Docker Enterprise Edition (Engine)

### Part a

'Both Universal Control Plane and Docker Trusted Registry backend
service containers, all of which reside on Docker Enterprise Edition,
log all of the event types indicated by this control (as explained by
their component narratives). These and other application containers
that reside on Docker Enterprise Edition can be configured to log data
via an appropriate Docker logging driver. Instructions for configuring
logging drivers can be found at the following resource:

- https://docs.docker.com/engine/admin/logging/overview/'
## Universal Control Plane (UCP)

### Part a

'All of the event types indicated by this control are logged by the
backend ucp-controller service within Universal Control Plane. In
addition, each container created on a Universal Control Plane cluster
logs event data. Supporting documentation for configuring UCP logging
can be referenced at the following resources:

- https://docs.docker.com/datacenter/ucp/2.1/guides/admin/configure/store-logs-in-an-external-system/'
## Docker Trusted Registry (DTR)

### Part a

'All of the event types indicated by this control are logged by a
combination of the backend ucp-controller service within Universal
Control Plane and the backend services that make up Docker Trusted
Registry. Additional documentation can be found at the following resource:

- https://docs.docker.com/datacenter/dtr/2.2/guides/admin/monitor-and-troubleshoot/'
