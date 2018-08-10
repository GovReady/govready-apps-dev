id: ssp_template_au_3
format: markdown
...
## Docker Enterprise Edition (Engine)

'Both Universal Control Plane and Docker Trusted Registry are
pre-configured to take advantage of Docker Enterprise Edition''s
built-in logging mechanisms. A sample audit event recorded by Docker
Enterprise Edition has been provided below:

{"level":"info","license_key":"123456789123456789123456789","msg":"eNZi:Password
based auth
suceeded","remote_addr":"192.168.33.1:55905","time":"2016-11-09T22:41:01Z","type":"auth
ok","username":"dockeruser"}

Additional documentation can be referenced at the following resource:

- https://docs.docker.com/engine/admin/logging/overview/'
## Universal Control Plane (UCP)

'Universal Control Plane generates all of the audit record information
indicated by this control. A sample audit event has been provided
below:

{"level":"info","license_key":"123456789123456789123456789","msg":"eNZi:Password
based auth
suceeded","remote_addr":"192.168.33.1:55905","time":"2016-11-09T22:41:01Z","type":"auth
ok","username":"dockeruser"}'
## Docker Trusted Registry (DTR)

'Docker Trusted Registry generates all of the audit record information
indicated by this control. A sample audit event has been provided
below:

{"level":"info","license_key":"123456789123456789123456789","msg":"eNZi:Password
based auth
suceeded","remote_addr":"192.168.33.1:55905","time":"2016-11-09T22:41:01Z","type":"auth
ok","username":"dockeruser"}'
## Authentication and Authorization Service (eNZi)

'Docker Enterprise Edition generates all of the audit record
information indicated by this control. A sample audit event has been
provided below:

{"level":"info","license_key":"123456789123456789123456789","msg":"eNZi:Password
based auth
suceeded","remote_addr":"192.168.33.1:55905","time":"2016-11-09T22:41:01Z","type":"auth
ok","username":"dockeruser"}'
