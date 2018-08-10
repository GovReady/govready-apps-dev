id: ssp_template_sc_20
format: markdown
...
## System and Communications Protection Policy for cloud.gov

### Part a

cloud.gov inherits from AWS CSP Route 53 the ability to use DNS with HTTP Strict Transport Security (HSTS) to achieve data origin authentication and integrity verification artifacts, along with the authoritative name resolution data the system returns in response to external name/address resolution queries.

### Part b

By allowing endpoints to use Public Key Infrastructure (PKI) certificates containing unique domain identifiers that map with top-level registered domain, cloud.gov provides the means to indicate the security status of child zones and (if the child supports secure resolution services) to enable verification of a chain of trust among parent and child domains, when operating as part of a distributed, hierarchical namespace.
