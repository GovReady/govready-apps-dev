id: ssp_template_ia_3
format: markdown
...
## Docker Enterprise Edition (Engine)

'In order for other CS Engine nodes to be able to join a cluster
managed by Universal Control Plane, they must be identified and
authenticated via either a manager or worker token. Use of the token
includes trust on first use mutual TLS.'
## Universal Control Plane (UCP)

'In order for nodes to join a Universal Control Plane cluster, they
must be identified and authenticated via either a manager or worker
token. Additional information can be found at the following resources:

- https://docs.docker.com/datacenter/ucp/2.1/guides/admin/configure/scale-your-cluster/'
## Docker Trusted Registry (DTR)

'Docker Trusted Registry replicas reside on Universal Control Plane
worker nodes. In order for UCP worker nodes to join a Universal
Control Plane cluster, they must be identified and authenticated via a
worker token. Additional Docker Trusted Registry replicas can only be
added after a UCP administrator user has authenticated in to the UCP
cluster and when mutual TLS authentication between the UCP worker and
manager nodes has been established. Reference documentation can be
found at
https://docs.docker.com/datacenter/dtr/2.1/guides/install/#/step-7-join-replicas-to-the-cluster.'
