id: ssp_template_cm_7__5
format: markdown
...
## Docker Enterprise Edition (Engine)

'The organization is responsible for meeting the requirements of this
control. To assist with these requirements and in order to restrict
which Docker images can be used to deploy applications to CS Docker
Engine, the organization must define a list of allowed base Docker
images and make them available via Docker Trusted Registry. The
organization must also prevent users from being able to pull Docker
images from untrusted sources.'
## Universal Control Plane (UCP)

### Part a

'The organization is responsible for meeting the requirements of this
control. To assist with these requirements and in order to restrict
which Docker images can be used to deploy applications to Universal
Control Plane, the organization must define a list of allowed base
Docker images and make them available via Docker Trusted Registry. The
organization must also prevent users from being able to pull Docker
images from untrusted sources.'

### Part b

'The organization is responsible for meeting the requirements of this
control. To assist with these requirements, the organization can
configure its systems to ensure that only approved Docker images
stored in Docker Trusted Registry can be run on Universal Control
Plane. This can be accomplished by using Docker Content Trust to sign
Docker images, and configure UCP to enforce only signed images from
specific Teams at runtime. Additional information can be found at the
following resources:

- https://docs.docker.com/datacenter/ucp/2.1/guides/user/content-trust/'
## Docker Trusted Registry (DTR)

### Part a

'The organization is responsible for meeting the requirements of this
control. To assist with these requirements, the organization can
define a list of allowed base Docker images and make them available
via Docker Trusted Registry. The organization must also prevent users
from being able to pull Docker images from untrusted sources.'

### Part b

'The organization is responsible for meeting the requirements of this
control. To assist with these requirements, the organization can
configure its systems to ensure that only approved Docker images are
stored in Docker Trusted Registry. This can be accomplished by using
Docker Content Trust to sign Docker images which can subsequently be
stored in Docker Trusted Registry.'
