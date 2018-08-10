id: ssp_template_ia_2
format: markdown
...
## User Account and Authentication (UAA) Server

The UAA is the identity management service for Cloud Foundry. Its primary role is as an OAuth2 provider, issuing tokens for client applications to use when they act on behalf of Cloud Foundry users. In collaboration with the login server, it authenticates users with their Cloud Foundry credentials, and act as a Single Sign-On (SSO) service using those credentials (or others). It has endpoints for managing user accounts and for registering OAuth2 clients, as well as various other management functions.
All users have individually unique identifiers to access and authenticates  to the environment. Shared or group authenticators are not utilized, with the exception of a root administrative account. There are only two authorized users from the DevOps team who has access to the root administrative account.
## Identity and Access Management
## Identification and Authentication Policy for 18F

The cloud.gov platform delegates authentication to either the GSA enterprise system or GitHub for any administrator access.
