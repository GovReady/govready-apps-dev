id: ssp_template_ia_2
format: markdown
...
## Authentication and Authorization Service (eNZi)

'Docker Enterprise Edition can be configured to identify and authenticate
users via it's integrated support for LDAP. Users and groups managed
within the organization's LDAP directory service (e.g. Active
Directory) can be synchronized to UCP and DTR on a regular interval. When a
user is removed from the LDAP-backed directory, that user becomes
inactive within UCP and DTR. In addition, UCP and DTR teams can be mapped to groups
synchronized via LDAP. When a user is added/removed to/from the LDAP
group, that same user is automatically added/removed to/from the UCP and DTR
team. Instructions for configuring LDAP integration can be found at
https://docs.docker.com/datacenter/ucp/2.0/guides/configuration/integrate-with-ldap/.'
