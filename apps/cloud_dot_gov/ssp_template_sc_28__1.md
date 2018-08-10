id: ssp_template_sc_28__1
format: markdown
...
## System and Communications Protection Policy for cloud.gov

cloud.gov implements cryptographic mechanisms to prevent unauthorized disclosure and modification of all blobs created by BOSH and Cloud Foundry by implementing at-rest encryption and by checking file signatures.
## User Account and Authentication (UAA) Server

The Cloud Foundry platform as a service does NOT create, store or process any personally identifiable information (PII) or sensitive information as identified by parameter requirement 1.

Applications running on Cloud Foundry receive requests through the URLs configured for the application. HTTP requests arrive on ports 80 and 443. Additionally, Cloud Foundry requires a channel for TCP/WebSocket traffic. The default cf-release manifest assigns port: 4443 for TCP/WebSocket communications.
All traffic from the public internet to the Cloud Controller and UAA happens over HTTPS. Inside the boundary of the system, components communicate over a publish-subscribe (pub-sub) port: 4222 message bus, NATs

For stored data identified by parameter 2, the following cryptographic mechanisms are used to prevent unauthorized disclosure and modification of stored data.
Operators configure encryption of the identity store in the UAA. When users register an account with the Cloud Foundry platform, the UAA, acts as the user store and stores user passwords in the UAA database using bcrypt. Bcrypt is a blowfish encryption algorithm, which enables cloud foundry to store a secure hash of your users' passwords.
The Cloud Controller stores the configuration for an application in an encrypted database table. This configuration data includes user-specified environment variables and service credentials for any services bound to the app.
Application developers push their code using the Cloud Foundry API. Cloud Foundry secures each call to the CF API using the UAA and SSL
To combat spoofing Cloud Foundry network traffic rules help prevents the attack from accessing application containers. Cloud Foundry uses application isolation, operating system restrictions, and encrypted connections to further mitigate risk.
