id: ssp_template_au_11
format: markdown
...
## Docker Enterprise Edition (Engine)

'The organization will be responsible for meeting the requirements of
this control. To assist with these requirements, Docker Enterprise
Edition can be configured to use a logging driver that stores data in
a location for the duration specified by this control. Additional
information can be found at the following resources:

- https://docs.docker.com/engine/admin/logging/overview/'
## Universal Control Plane (UCP)

'The organization will be responsible for meeting the requirements of
this control. To assist with these requirements, Universal Control
Plane can be configured to send logs to a remote logging stack.
Additional information can be found at the following resources:

- https://docs.docker.com/datacenter/ucp/2.1/guides/admin/configure/store-logs-in-an-external-system/

This logging stack can subsequently be configured retain logs for the
duration required by this control.'
## Docker Trusted Registry (DTR)

'The organization will be responsible for meeting the requirements of
this control. To assist with these requirements, Docker Trusted
Registry resides as an Application on a Universal Control Plane
cluster, and as such, can be configured to send logs to a remote
logging stack. Additional information can be found at the following
resources:

- https://docs.docker.com/datacenter/ucp/2.1/guides/admin/configure/store-logs-in-an-external-system/

This logging stack can subsequently be configured to retain logs for
the duration required by this control.'
