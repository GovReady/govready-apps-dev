id: ssp_template_cm_5__3
format: markdown
...
## Docker Enterprise Edition (Engine)

'Before installing Docker Enterprise Edition, ensure that your
supporting Linux operating system''s packager manager supports package
signature verification and that it is enabled. It is also required
that you import the Docker public key for CS packages so as to
retrieve the validated and signed package from Docker, Inc. Refer to
your Linux OS documentation for instructions on completing the above
steps.

In addition, Docker Content Trust is a capability provided by CS
Docker Engine that enforces client-side signing and verification of
Docker image tags. It provides the ability to use digital signatures
for data sent to and received from Docker Trusted Registry and the
public Docker Store. These signatures allow client-side verification
of the integrity and publisher of specific image tags. When enabling
Docker Content Trust in Docker Enterprise Edition you can enforce the
use of signed Docker images. Additional information can be found at
the following resources:

- https://docs.docker.com/engine/security/trust/content_trust/'
## Universal Control Plane (UCP)

'Docker Content Trust is a capability provided by Docker Enterprise Edition
that enforces client-side signing and verification of Docker image
tags. It provides the ability to use digital signatures for data sent
to and received from Docker Trusted Registry and the public Docker
Store. These signatures allow client-side verification of the
integrity and publisher of specific image tags. All Universal Control
Plane Docker images are officially signed and verified by Docker, Inc.

When configuring Universal Control Plane, you should enforce
applications to only use Docker images signed by trusted UCP users
within your organization. Additional information can be found at the following resources:

- https://docs.docker.com/datacenter/ucp/2.1/guides/user/content-trust/
- https://docs.docker.com/datacenter/ucp/2.1/guides/user/content-trust/manage-trusted-repositories/
- https://docs.docker.com/datacenter/ucp/2.1/guides/user/content-trust/continuous-integration/'
## Docker Trusted Registry (DTR)

'Docker Content Trust is a capability provided by Docker Enterprise
Edition that enforces client-side signing and verification of Docker
image tags. It provides the ability to use digital signatures for data
sent to and received from Docker Trusted Registry and the public
Docker Store. These signatures allow client-side verification of the
integrity and publisher of specific image tags. All Docker Trusted
Registry Docker images are officially signed and verified by Docker,
Inc.

When installing Docker Trusted Registry, you should enable Docker
Content Trust and subsequently pull the the signed DTR image tag.
Additional information can be found at teh following resources:

- https://docs.docker.com/engine/security/trust/content_trust/
- https://docs.docker.com/datacenter/ucp/2.1/guides/user/content-trust/manage-trusted-repositories/'
