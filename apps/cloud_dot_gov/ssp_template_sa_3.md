id: ssp_template_sa_3
format: markdown
...
## System and Services Acquisition Policy for 18F

### Part a

18F practices the Scrumban process when developing new features or fixing existing issues, including security fixes and enhancements for cloud.gov.  Each feature or issue is assigned to a card in the system, where it goes through a process of being identified, prioritized, explored, delivered, and finally demonstrated. Each card is reviewed by the team as a whole throughout its lifecycle to identify any security risks or concerns, which are recorded on the card as "acceptance criteria" that must be addressed before development is complete.

Once development is complete, a team member submits the code to our version control system as a "pull request", where at least one other team member further reviews it before merging it into the code base.  The team then deploys new features into our staging area where they undergo further security review and stakeholder acceptance testing, as well as automated acceptance tests.

### Part b

The cloud.gov operations team is broken into several sub-teams with different areas of responsibility and expertise.   Security is a foremost concern for members of all teams.  The cloud.gov operations team is primarily focused on implementing security policies at the platform level.

### Part c

Each member of the cloud.gov operations team has the necessary security background to properly handle sensitive data, such as security keys and certificates, and to evaluate the security implications associated with configuration changes. The cloud.gov operations team controls access to cloud.gov and its components through the access control tools appropriate for its components, including AWS security groups, Cloud Foundry roles, and GitHub team membership.

### Part d

The cloud.gov operations team continually monitors the configurations of the various components of cloud.gov to ensure they meet the requirements for protecting sensitive data.
