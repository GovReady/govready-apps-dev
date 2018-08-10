id: ssp_template_sc_13
format: markdown
...
## System and Communications Protection Policy for cloud.gov

cloud.gov inherits the control from the GovCloud package for the ELB SSL termination. See https://d0.awsstatic.com/whitepapers/compliance/AWS_Risk_and_Compliance_Whitepaper.pdf for further details.
## User Account and Authentication (UAA) Server

As for stored data the following cryptographic mechanisms are used to prevent unauthorized disclosure and modification of stored data.
Operators configure encryption of the identity store in the UAA. When users register an account with the Cloud Foundry platform, the UAA acts as the user store and stores user passwords in the UAA database using bcrypt, a blowfish encryption algorithm, which enables Cloud Foundry to store a secure hash of user passwords.
The Cloud Controller stores the configuration for an application in an encrypted database table. This configuration data includes user-specified environment variables and service credentials for any services bound to the app.
## SecureProxy

cloud.gov forces https using SecureProxy:

Applications running on Cloud Foundry receive requests through the URLs configured
for the application. HTTP requests arrive on ports 80 and 443. Additionally, Cloud
Foundry requires a channel for TCP/WebSocket traffic. The default cf-release manifest
assigns port 4443 for TCP/WebSocket communications.

All traffic from the public internet to the Cloud Controller and UAA happens over
HTTPS. Inside the boundary of the system, components communicate over publish-subscribe
(pub-sub) message bus, NATs on port 4222.

To combat spoofing Cloud Foundry network traffic rules help prevent the attack
from accessing application containers. Cloud Foundry uses application isolation,
operating system restrictions, and encrypted connections to further mitigate risk.

Application developers push their code using the Cloud Foundry API. Cloud Foundry
secures each call to the CF API using the UAA and SSL
