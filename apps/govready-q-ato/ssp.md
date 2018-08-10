id: ssp
format: markdown
title: System Security Plan
...
<style type="text/css" scoped>
    h2 { border-bottom:1px solid #888; }
    h3 { border-bottom: 0.5px solid #aaa; }
    h4 { margin-top: 15px; font-weight: bold; font-size: 1em; }
    blockquote { color: #666; font-size:0.8em; margin: 0 10px; }
    .notice {color: red; font-size:3.0em; text-align:center; transform: scaleY(.85);
    font-weight: bold;}
    table, th, td { border: 1px solid #888; }
    th, td { padding: 15px; text-align: left;}
</style>


{# BEGIN CONTROLS #}


## AC - Access Control


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-1 Access Control Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    An access control policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the access control policy and the associated
           access controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     access control policy and procedures;
c.   Review and update the current access control:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the access control procedures implement the access control policy and controls;
     and
e.   Develop, document, and implement remediation actions for violations of the access control
     policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2 Account Management

<blockquote>a.   Define and document the types of system accounts allowed for use within the system in
     support of organizational missions and business functions;




b.   Assign account managers for system accounts;
c.   Establish conditions for group and role membership;
d.   Specify authorized users of the system, group and role membership, and access authorizations
     (i.e., privileges) and other attributes (as required) for each account;
e.   Require approvals by [Assignment: organization-defined personnel or roles] for requests to
     create system accounts;
f.   Create, enable, modify, disable, and remove system accounts in accordance with [Assignment: organization-defined policy, procedures, and conditions];
g.   Monitor the use of system accounts;
h.   Notify account managers within [Assignment: organization-defined time-period for each situation]:
     1.   When accounts are no longer required;
     2.   When users are terminated or transferred; and
     3.   When individual system usage or need-to-know changes for an individual;
i.   Authorize access to the system based on:
     1.   A valid access authorization;
     2.   Intended system usage; and
     3.   Other attributes as required by the organization or associated missions and business
          functions;
j.   Review accounts for compliance with account management requirements [Assignment: organization-defined frequency];
k.   Establish a process for reissuing shared/group account credentials (if deployed) when
     individuals are removed from the group; and
l.   Align account management processes with personnel termination and transfer processes.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(1) Automated System Account Management

<blockquote>Employ automated mechanisms to support the management of system accounts.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(2) Removal of Temporary and Emergency Accounts

<blockquote>Automatically [Selection: remove; disable] temporary and emergency accounts after [Assignment: organization-defined time-period for each type of account].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(3) Disable Accounts

<blockquote>Automatically disable accounts when the accounts:
(a)   Have expired;
(b) Are no longer associated to a user;
(c)   Are in violation of organizational policy;
(d) Are no longer used by applications, services, or the system; and
(e)   Have been inactive for [Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(4) Automated Audit Actions

<blockquote>Automatically audit account creation, modification, enabling, disabling, and removal actions, and
notify [Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(5) Inactivity Logout

<blockquote>Require that users log out when [Assignment: organization-defined time-period of expected inactivity or description of when to log out].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(6) Dynamic Privilege Management

<blockquote>Implement the following dynamic privilege management capabilities: [Assignment: organization-defined list of dynamic privilege management capabilities].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(7) Role-Based Schemes

<blockquote>(a)   Establish and administer privileged user accounts in accordance with a role-based access
      scheme that organizes allowed system access and privileges into roles;
(b) Monitor privileged role assignments; and
(c)   Revoke access when privileged role assignments are no longer appropriate.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(8) Dynamic Account Management

<blockquote>Create, activate, manage, and deactivate [Assignment: organization-defined system accounts]
dynamically.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(9) Restrictions on Use of Shared and Group Accounts

<blockquote>Only permit the use of shared and group accounts that meet [Assignment: organization-defined conditions for establishing shared and group accounts].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(10) Shared and Group Account Credential Change

<blockquote>Change shared and group account credentials when members leave the group.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(11) Usage Conditions

<blockquote>Enforce [Assignment: organization-defined circumstances and/or usage conditions] for
[Assignment: organization-defined system accounts].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(12) Account Monitoring for Atypical Usage

<blockquote>(a)   Monitor system accounts for [Assignment: organization-defined atypical usage]; and
(b) Report atypical usage of system accounts to [Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(13) Disable Accounts for High-Risk Individuals

<blockquote>Disable accounts of users posing a significant risk within [Assignment: organization-defined time-period] of discovery of the risk.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(14) Prohibit Specific Account Types

<blockquote>Prohibit the creation and use of [Selection (one or more): shared; guest; anonymous; temporary; emergency] accounts for access to [Assignment: organization-defined information types].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_2_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-2(15) Attribute-Based Schemes

<blockquote>(a)   Establish and administer privileged user accounts in accordance with an attribute-based
      access scheme that specifies allowed system access and privileges based on attributes;
(b) Monitor privileged attribute-based assignments;
(c)   Monitor changes to attributes; and
(d) Revoke access when privileged attribute-based assignments are no longer appropriate.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_2_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3 Access Enforcement

<blockquote>       Enforce approved authorizations for logical access to information and system resources in

accordance with applicable access control policies.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3(2) Dual Authorization

<blockquote></blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3(3) Mandatory Access Control

<blockquote>components;</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3(4) Discretionary Access Control

<blockquote>Enforce [Assignment: organization-defined discretionary access control policy] over defined
subjects and objects where the policy specifies that a subject that has been granted access to
information can do one or more of the following:
(a)   Pass the information to any other subjects or objects;
(b) Grant its privileges to other subjects;
(c)   Change security attributes on subjects, objects, the system, or the system’s components;
(d) Choose the security attributes to be associated with newly created or revised objects; or
(e)   Change the rules governing access control.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3(5) Security-Relevant Information

<blockquote>Prevent access to [Assignment: organization-defined security-relevant information] except during
secure, non-operable system states.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3(7) Role-Based Access Control

<blockquote>Enforce a role-based access control policy over defined subjects and objects and control access
based upon [Assignment: organization-defined roles and users authorized to assume such roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3(8) Revocation of Access Authorizations

<blockquote>Enforce the revocation of access authorizations resulting from changes to the security attributes
of subjects and objects based on [Assignment: organization-defined rules governing the timing of revocations of access authorizations].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3(9) Controlled Release

<blockquote>Release information outside of the established system boundary only if:
(a)   The receiving [Assignment: organization-defined system or system component] provides
      [Assignment: organization-defined security safeguards]; and
(b) [Assignment: organization-defined security safeguards] are used to validate the
    appropriateness of the information designated for release.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3(10) Audited Override of Access Control Mechanisms

<blockquote>Employ an audited override of automated access control mechanisms under [Assignment: organization-defined conditions] by [Assignment: organization-defined roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3(11) Restrict Access to Specific Information

<blockquote>Restrict direct access to data repositories containing [Assignment: organization-defined information types].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3(12) Assert and Enforce Application Access

<blockquote>(a)   Require applications to assert, as part of the installation process, the access needed to the
      following system applications and functions: [Assignment: organization-defined
system applications and functions]; and (b) Provide an enforcement mechanism to prevent other-than-asserted access.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_3_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-3(13) Attribute-Based Access Control

<blockquote>Enforce attribute-based access control policy over defined subjects and objects and control
access based upon [Assignment: organization-defined attributes to assume access permissions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_3_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4 Information Flow Enforcement

<blockquote>Enforce approved authorizations for controlling the flow of information within the system
and between interconnected systems based on [Assignment: organization-defined information flow control policies].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(1) Object Security Attributes

<blockquote>Use [Assignment: organization-defined security attributes] associated with [Assignment: organization-defined information, source, and destination objects] to enforce [Assignment: organization-defined information flow control policies] as a basis for flow control decisions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(2) Processing Domains

<blockquote>Use protected processing domains to enforce [Assignment: organization-defined information flow control policies] as a basis for flow control decisions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(3) Dynamic Information Flow Control

<blockquote>Enforce dynamic information flow control based on [Assignment: organization-defined policies].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(4) Flow Control of Encrypted Information

<blockquote>Prevent encrypted information from bypassing [Assignment: organization-defined flow control mechanisms] by [Selection (one or more): decrypting the information; blocking the flow of the encrypted information; terminating communications sessions attempting to pass encrypted information; &lt;2&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(5) Embedded Data Types

<blockquote>Enforce [Assignment: organization-defined limitations] on embedding data types within other data
types.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(6) Metadata

<blockquote>Enforce information flow control based on [Assignment: organization-defined metadata].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(7) One-Way Flow Mechanisms

<blockquote>Enforce [Assignment: organization-defined one-way information flows] using hardware
mechanisms.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(8) Security Policy Filters

<blockquote>Enforce information flow control using [Assignment: organization-defined security policy filters] as
a basis for flow control decisions for [Assignment: organization-defined information flows].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(9) Human Reviews

<blockquote>Enforce the use of human reviews for [Assignment: organization-defined information flows] under
the following conditions: [Assignment: organization-defined conditions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(10) Enable and Disable Security Policy Filters

<blockquote>Provide the capability for privileged administrators to enable and disable [Assignment: organization-defined security policy filters] under the following conditions: [Assignment: organization-defined conditions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(11) Configuration of Security Policy Filters

<blockquote>Provide the capability for privileged administrators to configure [Assignment: organization-defined security policy filters] to support different security policies.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(12) Data Type Identifiers

<blockquote>When transferring information between different security domains, use [Assignment: organization-defined data type identifiers] to validate data essential for information flow decisions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(13) Decomposition Into Policy-Relevant Subcomponents

<blockquote>When transferring information between different security domains, decompose information into
[Assignment: organization-defined policy-relevant subcomponents] for submission to policy
enforcement mechanisms.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(14) Security Policy Filter Constraints

<blockquote>When transferring information between different security domains, implement [Assignment: organization-defined security policy filters] requiring fully enumerated formats that restrict data
structure and content.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(15) Detection of Unsanctioned Information

<blockquote>When transferring information between different security domains, examine the information for the
presence of [Assignment: organized-defined unsanctioned information] and prohibit the transfer of
such information in accordance with the [Assignment: organization-defined security policy].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_17_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(17) Domain Authentication

<blockquote>Uniquely identify and authenticate source and destination points by [Selection (one or more): organization, system, application, service, individual] for information transfer.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_17_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_19_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(19) Validation of Metadata

<blockquote>When transferring information between different security domains, apply the same security policy
filtering to metadata as it applies to data payloads.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_19_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_20_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(20) Approved Solutions

<blockquote>Employ [Assignment: organization-defined solutions in approved configurations] to control the
flow of [Assignment: organization-defined information] across security domains.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_20_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_21_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(21) Physical and Logical Separation of Information Flows

<blockquote>Separate information flows logically or physically using [Assignment: organization-defined mechanisms and/or techniques] to accomplish [Assignment: organization-defined required separations by types of information].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_21_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_4_22_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-4(22) Access Only

<blockquote>Provide access from a single device to computing platforms, applications, or data residing on
multiple different security domains, while preventing any information flow between the different
security domains.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_4_22_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-5 Separation of Duties

<blockquote>a.    Separate [Assignment: organization-defined duties of individuals];
b.    Document separation of duties of individuals; and
c.    Define system access authorizations to support separation of duties.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-6 Least Privilege

<blockquote>Employ the principle of least privilege, allowing only authorized accesses for users (or
processes acting on behalf of users) which are necessary to accomplish assigned tasks in
accordance with organizational missions and business functions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_6_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-6(1) Authorize Access to Security Functions

<blockquote>Explicitly authorize access to [Assignment: organization-defined security functions (deployed in hardware, software, and firmware) and security-relevant information].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_6_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_6_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-6(2) Non-Privileged Access for Nonsecurity Functions

<blockquote>Require that users of system accounts, or roles, with access to [Assignment: organization-defined security functions or security-relevant information], use non-privileged accounts or roles, when
accessing nonsecurity functions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_6_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_6_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-6(3) Network Access to Privileged Commands

<blockquote>Authorize network access to [Assignment: organization-defined privileged commands] only for
[Assignment: organization-defined compelling operational needs] and document the rationale for
such access in the security plan for the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_6_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_6_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-6(4) Separate Processing Domains

<blockquote>Provide separate processing domains to enable finer-grained allocation of user privileges.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_6_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_6_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-6(5) Privileged Accounts

<blockquote>Restrict privileged accounts on the system to [Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_6_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_6_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-6(6) Privileged Access by Non-Organizational Users

<blockquote>Prohibit privileged access to the system by non-organizational users.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_6_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_6_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-6(7) Review of User Privileges

<blockquote>(a)   Review [Assignment: organization-defined frequency] the privileges assigned to [Assignment: organization-defined roles or classes of users] to validate the need for such privileges; and
(b) Reassign or remove privileges, if necessary, to correctly reflect organizational mission and
    business needs.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_6_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_6_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-6(8) Privilege Levels for Code Execution

<blockquote>Prevent the following software from executing at higher privilege levels than users executing the
software: [Assignment: organization-defined software].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_6_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_6_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-6(9) Auditing Use of Privileged Functions

<blockquote>Audit the execution of privileged functions.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_6_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_6_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-6(10) Prohibit Non-Privileged Users From Executing Privileged Functions

<blockquote>Prevent non-privileged users from executing privileged functions.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_6_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-7 Unsuccessful Logon Attempts

<blockquote>a.    Enforce a limit of [Assignment: organization-defined number] consecutive invalid logon
      attempts by a user during a [Assignment: organization-defined time-period];
and b.    Automatically [Selection (one or more): lock the account/node for an &lt;3&gt;; lock the account/node until released by an administrator; delay next logon prompt per &lt;4&gt;; take &lt;5&gt;] when the maximum number of unsuccessful
      attempts is exceeded.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_7_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-7(2) Purge or Wipe Mobile Device

<blockquote>Purge or wipe information from [Assignment: organization-defined mobile devices] based on
[Assignment: organization-defined purging or wiping requirements and techniques] after
[Assignment: organization-defined number] consecutive, unsuccessful device logon attempts.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_7_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_7_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-7(3) Biometric Attempt Limiting

<blockquote>Limit the number of unsuccessful biometric logon attempts to [Assignment: organization-defined number].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_7_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_7_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-7(4) Use of Alternate Factor

<blockquote>Allow the use of one or more additional authentication factors after the number of organization-
defined consecutive invalid logon attempts have been exceeded.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_7_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-8 System Use Notification

<blockquote>a.    Display [Assignment: organization-defined system use notification message or banner] to
      users before granting access to the system that provides privacy and security
notices
      consistent with applicable laws, Executive Orders, directives, policies,
regulations, standards,
      and guidelines and state that:
      1.   Users are accessing a U.S. Government system;
      2.   System usage may be monitored, recorded, and subject to audit;
      3.   Unauthorized use of the system is prohibited and subject to criminal
and civil penalties;
           and
      4.   Use of the system indicates consent to monitoring and recording;
b.    Retain the notification message or banner on the screen until users acknowledge the usage
      conditions and take explicit actions to log on to or further access the
system; and c.    For publicly accessible systems:
      1.   Display system use information [Assignment: organization-defined conditions],
before
           granting further access to the publicly accessible system;
      2.   Display references, if any, to monitoring, recording, or auditing that
are consistent with
           privacy accommodations for such systems that generally prohibit those
activities; and
      3.   Include a description of the authorized uses of the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-9 Previous Logon (Access) Notification

<blockquote>Notify the user, upon successful logon (access) to the system, of the date and time of the
last logon (access).
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_9_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-9(1) Unsuccessful Logons

<blockquote>Notify the user, upon successful logon/access, of the number of unsuccessful logon/access
attempts since the last successful logon/access.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_9_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_9_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-9(2) Successful and Unsuccessful Logons

<blockquote>Notify the user, upon successful logon/access, of the number of [Selection: successful logons/accesses; unsuccessful logon/access attempts; both] during [Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_9_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_9_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-9(3) Notification of Account Changes

<blockquote>Notify the user, upon successful logon/access, of changes to [Assignment: organization-defined security-related characteristics/parameters of the user’s account] during [Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_9_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_9_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-9(4) Additional Logon Information

<blockquote>Notify the user, upon successful logon/access, of the following additional information:
[Assignment: organization-defined information to be included in addition to the date and time of the last logon/access].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_9_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-10 Concurrent Session Control

<blockquote>Limit the number of concurrent sessions for each [Assignment: organization-defined account and/or account type] to [Assignment: organization-defined number].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-11 Device Lock

<blockquote>a.    Prevent further access to the system by initiating a device lock after [Assignment: organization-defined time-period] of inactivity or upon receiving a request from a user; and
b.    Retain the device lock until the user reestablishes access using established identification and
      authentication procedures.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_11_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-11(1) Pattern-Hiding Displays

<blockquote>Conceal, via the device lock, information previously visible on the display with a publicly viewable
image.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_11_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_11_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-11(2) Require User-Initiated Lock

<blockquote>Require the user to initiate a device lock before leaving the system unattended.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_11_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-12 Session Termination

<blockquote>Automatically terminate a user session after [Assignment: organization-defined conditions or trigger events requiring session disconnect].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_12_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-12(1) User-Initiated Logouts

<blockquote>Provide a logout capability for user-initiated communications sessions whenever authentication is
used to gain access to [Assignment: organization-defined information resources].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_12_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_12_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-12(2) Termination Message

<blockquote>Display an explicit logout message to users indicating the reliable termination of authenticated
communications sessions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_12_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_12_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-12(3) Timeout Warning Message

<blockquote>Display an explicit message to users indicating that the session is about to end.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_12_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-14 Permitted Actions without Identification or Authentication

<blockquote>a.    Identify [Assignment: organization-defined user actions] that can be performed on the system
      without identification or authentication consistent with organizational missions and business
      functions; and
b.    Document and provide supporting rationale in the security plan for the system, user actions
      not requiring identification or authentication.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16 Security and Privacy Attributes

<blockquote>a.    Provide the means to associate [Assignment: organization-defined types of security and privacy attributes] having [Assignment: organization-defined security and privacy attribute values] with information in storage, in process, and/or in transmission;
b.    Ensure that the security and privacy attribute associations are made and retained with the
      information;
c.    Establish the permitted [Assignment: organization-defined security attributes] for
      [Assignment: organization-defined systems]; and
d.    Determine the permitted [Assignment: organization-defined values or ranges] for each of the
      established security and privacy attributes.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16(1) Dynamic Attribute Association

<blockquote>Dynamically associate security and privacy attributes with [Assignment: organization-defined subjects and objects] in accordance with [Assignment: organization-defined security and privacy policies] as information is created and combined.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16(2) Attribute Value Changes by Authorized Individuals

<blockquote>Provide authorized individuals (or processes acting on behalf of individuals) the capability to
define or change the value of associated security and privacy attributes.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16(3) Maintenance of Attribute Associations by System

<blockquote>Maintain the association and integrity of [Assignment: organization-defined security and privacy attributes] to [Assignment: organization-defined subjects and objects].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16(4) Association of Attributes by Authorized Individuals

<blockquote>Provide the capability to associate [Assignment: organization-defined security and privacy attributes] with [Assignment: organization-defined subjects and objects] by authorized individuals
(or processes acting on behalf of individuals).
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16(5) Attribute Displays for Output Devices

<blockquote>Display security and privacy attributes in human-readable form on each object that the system
transmits to output devices to identify [Assignment: organization-identified special dissemination, handling, or distribution instructions] using [Assignment: organization-identified human-readable, standard naming conventions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16(6) Maintenance of Attribute Association by Organization

<blockquote>Require personnel to associate, and maintain the association of [Assignment: organization-defined security and privacy attributes] with [Assignment: organization-defined subjects and objects] in
accordance with [Assignment: organization-defined security and privacy policies].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16(7) Consistent Attribute Interpretation

<blockquote>Provide a consistent interpretation of security and privacy attributes transmitted between
distributed system components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16(8) Association Techniques and Technologies

<blockquote>Implement [Assignment: organization-defined techniques and technologies] with [Assignment: organization-defined level of assurance] in associating security and privacy attributes to
information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16(9) Attribute Reassignment

<blockquote>Reassign security and privacy attributes associated with information only via re-grading
mechanisms validated using [Assignment: organization-defined techniques or procedures].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16(10) Attribute Configuration by Authorized Individuals

<blockquote>Provide authorized individuals the capability to define or change the type and value of security and
privacy attributes available for association with subjects and objects.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_16_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-16(11) Audit Changes

<blockquote>Audit changes to security and privacy attributes.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_16_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_17_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-17 Remote Access

<blockquote>a.    Establish and document usage restrictions, configuration/connection requirements, and
      implementation guidance for each type of remote access allowed; and
b.    Authorize remote access to the system prior to allowing such connections.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_17_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_17_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-17(1) Automated Monitoring and Control

<blockquote>Monitor and control remote access methods.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_17_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_17_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-17(2) Protection of Confidentiality and Integrity Using Encryption

<blockquote>Implement cryptographic mechanisms to protect the confidentiality and integrity of remote access
sessions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_17_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_17_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-17(3) Managed Access Control Points

<blockquote>Route all remote accesses through [Assignment: organization-defined number] managed network
access control points.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_17_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_17_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-17(4) Privileged Commands and Access

<blockquote>(a)   Authorize the execution of privileged commands and access to security-relevant information
      via remote access only for [Assignment: organization-defined needs]; and
(b) Document the rationale for such access in the security plan for the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_17_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_17_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-17(6) Protection of Information

<blockquote>Protect information about remote access mechanisms from unauthorized use and disclosure.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_17_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_17_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-17(9) Disconnect or Disable Access

<blockquote>Provide the capability to expeditiously disconnect or disable remote access to the system within
[Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_17_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_18_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-18 Wireless Access

<blockquote>a.    Establish usage restrictions, configuration/connection requirements, and implementation
      guidance for wireless access; and



b.    Authorize wireless access to the system prior to allowing such connections.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_18_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_18_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-18(1) Authentication and Encryption

<blockquote>Protect wireless access to the system using authentication of [Selection (one or more): users; devices] and encryption.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_18_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_18_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-18(3) Disable Wireless Networking

<blockquote>Disable, when not intended for use, wireless networking capabilities internally embedded within
system components prior to issuance and deployment.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_18_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_18_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-18(4) Restrict Configurations by Users

<blockquote>Identify and explicitly authorize users allowed to independently configure wireless networking
capabilities.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_18_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_18_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-18(5) Antennas and Transmission Power Levels

<blockquote>Select radio antennas and calibrate transmission power levels to reduce the probability that
signals from wireless access points can be received outside of organization-controlled boundaries.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_18_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_19_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-19 Access Control for Mobile Devices

<blockquote>a.    Establish usage restrictions, configuration requirements, connection requirements, and
      implementation guidance for organization-controlled mobile devices;
b.    Authorize the connection of mobile devices to organizational systems; and
c.    Protect and control mobile devices when outside of controlled areas.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_19_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_19_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-19(4) Restrictions for Classified Information

<blockquote>             random reviews and inspections by [Assignment: organization-defined
security officials],
             and if classified information is found, the incident handling policy
is followed. (c)   Restrict the connection of classified mobile devices to classified systems in accordance with
      [Assignment: organization-defined security policies].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_19_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_19_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-19(5) Full Device and Container-Based Encryption

<blockquote>Employ [Selection: full-device encryption; container encryption] to protect the confidentiality and
integrity of information on [Assignment: organization-defined mobile devices].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_19_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_20_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-20 Use of External Systems

<blockquote>Establish terms and conditions, consistent with any trust relationships established with
other organizations owning, operating, and/or maintaining external systems, allowing authorized
individuals to:
a.    Access the system from external systems; and
b.    Process, store, or transmit organization-controlled information using external systems.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_20_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_20_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-20(1) Limits on Authorized Use

<blockquote>Permit authorized individuals to use an external system to access the system or to process, store,
or transmit organization-controlled information only after:
(a)   Verification of the implementation of required security and privacy controls on the external
      system as specified in the organization’s security and privacy policies and security and
      privacy plans; or
(b) Retention of approved system connection or processing agreements with the organizational
    entity hosting the external system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_20_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_20_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-20(2) Portable Storage Devices

<blockquote>[Selection: Restrict the use of organization-controlled portable storage devices by authorized individuals on external systems using the following &lt;1&gt;; Prohibit the use of organization-controlled portable storage devices by authorized individuals on external systems].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_20_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_20_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-20(3) Non-Organizationally Owned Systems and Components

<blockquote>[Selection: Restrict the use of non-organizationally owned systems or system components to process, store, or transmit organizational information using the following &lt;1&gt;; Prohibit the use of non-organizationally owned systems or system components to process, store, or transmit organizational information].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_20_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_20_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-20(4) Network Accessible Storage Devices

<blockquote>Prohibit the use of [Assignment: organization-defined network accessible storage devices] in
external systems.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_20_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_21_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-21 Information Sharing

<blockquote>a.    Facilitate information sharing by enabling authorized users to determine whether access
      authorizations assigned to the sharing partner match the access restrictions
and privacy
      authorizations on the information for [Assignment: organization-defined
information sharing circumstances where user discretion is required]; and b.    Employ [Assignment: organization-defined automated mechanisms or manual processes] to
      assist users in making information sharing and collaboration decisions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_21_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_21_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-21(1) Automated Decision Support

<blockquote>Enforce information-sharing decisions by authorized users based on access authorizations of
sharing partners and access restrictions on information to be shared.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_21_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_21_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-21(2) Information Search and Retrieval

<blockquote>Implement information search and retrieval services that enforce [Assignment: organization-defined information sharing restrictions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_21_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_22_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-22 Publicly Accessible Content

<blockquote>a.    Designate individuals authorized to post information onto a publicly accessible system;
b.    Train authorized individuals to ensure that publicly accessible information does not contain
      nonpublic information;
c.    Review the proposed content of information prior to posting onto the publicly accessible
      system to ensure that nonpublic information is not included; and
d.    Review the content on the publicly accessible system for nonpublic information [Assignment: organization-defined frequency] and remove such information, if discovered.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_22_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_23_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-23 Data Mining Protection

<blockquote>Employ [Assignment: organization-defined data mining prevention and detection techniques] for [Assignment: organization-defined data storage objects] to detect and protect
against unauthorized data mining.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_23_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_24_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-24 Access Control Decisions

<blockquote>Establish procedures to ensure [Assignment: organization-defined access control decisions] are applied to each access request prior to access enforcement.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_24_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_24_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-24(1) Transmit Access Authorization Information

<blockquote>Transmit [Assignment: organization-defined access authorization information] using [Assignment: organization-defined security safeguards] to [Assignment: organization-defined systems] that
enforce access control decisions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_24_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_24_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-24(2) no User or Process Identity

<blockquote>Enforce access control decisions based on [Assignment: organization-defined security attributes]
that do not include the identity of the user or process acting on behalf of the user.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_24_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ac_25_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AC-25 Reference Monitor

<blockquote>Implement a reference monitor for [Assignment: organization-defined access control policies] that is tamperproof, always invoked, and small enough to be subject to analysis and
testing, the completeness of which can be assured.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ac_25_impl|safe}}
{% endif %}
{% endfor %}

## AT - Awareness and Training


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-1 Awareness and Training Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A security and privacy awareness and training policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives,
regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the security and privacy
awareness and
           training policy and the associated security and privacy awareness and
training controls; b.   Designate an [Assignment: organization-defined senior management official] to manage the
     security and privacy awareness and training policy and procedures;
c.   Review and update the current security and privacy awareness and training:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the security and privacy awareness and training procedures implement the
     security and privacy awareness and training policy and controls; and
e.   Develop, document, and implement remediation actions for violations of the awareness and
     training policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-2 Awareness Training

<blockquote>       Provide basic security and privacy awareness training to system users (including

managers, senior executives, and contractors):
a.   As part of initial training for new users;
b.   When required by system changes; and



c.    [Assignment: organization-defined frequency] thereafter.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_2_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-2(1) Practical Exercises

<blockquote>Include practical exercises in awareness training that simulate security and privacy incidents.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_2_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_2_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-2(2) Insider Threat

<blockquote>Include awareness training on recognizing and reporting potential indicators of insider threat.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_2_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_2_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-2(3) Social Engineering and Mining

<blockquote>Include awareness training on recognizing and reporting potential and actual instances of social
engineering and social mining.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_2_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-3 Role-Based Training

<blockquote>Provide role-based security and privacy training to personnel with the following roles and
responsibilities: [Assignment: organization-defined roles and responsibilities]:
a.    Before authorizing access to the system or performing assigned duties;
b.    When required by system changes; and
c.    [Assignment: organization-defined frequency] thereafter.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-3(1) Environmental Controls

<blockquote>Provide [Assignment: organization-defined personnel or roles] with initial and [Assignment: organization-defined frequency] training in the employment and operation of environmental
controls.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-3(2) Physical Security Controls

<blockquote>Provide [Assignment: organization-defined personnel or roles] with initial and [Assignment: organization-defined frequency] training in the employment and operation of physical security
controls.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-3(3) Practical Exercises

<blockquote>Include practical exercises in security and privacy training that reinforce training objectives.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_3_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-3(4) Suspicious Communications and Anomalous System Behavior

<blockquote>Provide training to personnel on [Assignment: organization-defined indicators of malicious code]
to recognize suspicious communications and anomalous behavior in organizational systems.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_3_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_3_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-3(5) Personally Identifiable Information Processing

<blockquote>Provide personnel who process personally identifiable information with initial and [Assignment: organization-defined frequency] training on:
(a)   Organizational authority for collecting personally identifiable information;
(b) Authorized uses of personally identifiable information;
(c)   Content of System of Records Notices;
(d) Authorized sharing of personally identifiable information with external parties; and
(e)   Consequences of unauthorized use or sharing of personally identifiable information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_3_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_at_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AT-4 Training Records

<blockquote>a.    Document and monitor individual system security and privacy training activities including
      basic security and privacy awareness training and specific role-based system security and
      privacy training; and
b.    Retain individual training records for [Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_at_4_impl|safe}}
{% endif %}
{% endfor %}

## AU - Audit and Accountability


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-1 Audit and Accountability Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    An audit and accountability policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the audit and accountability policy and the
           associated audit and accountability controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     audit and accountability policy and procedures;
c.   Review and update the current audit and accountability:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the audit and accountability procedures implement the audit and accountability
     policy and controls; and
e.   Develop, document, and implement remediation actions for violations of the audit and
     accountability policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-2 Audit Events

<blockquote>a.   Verify that the system can audit the following event types: [Assignment: organization-defined auditable event types];





b.    Coordinate the security audit function with other organizational entities requiring audit-
      related information to enhance mutual support and to help guide the selection of auditable
      event types;
c.    Provide a rationale for why the auditable event types are deemed to be adequate to support
      after-the-fact investigations of security and privacy incidents; and
d.    Specify that the following event types are to be audited within the system: [Assignment: organization-defined audited events (the subset of the auditable events defined in AU-2 a.) along with the frequency of (or situation requiring) auditing for each identified event].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_2_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-2(3) Reviews and Updates

<blockquote>Review and update the audited events [Assignment: organization-defined frequency].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_2_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-3 Content of Audit Records

<blockquote>The system generates audit records containing information that establishes what type of
event occurred, when the event occurred, where the event occurred, the source of the event, the
outcome of the event, and the identity of any individuals or subjects associated with the event.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-3(1) Additional Audit Information

<blockquote>Generate audit records containing the following additional information: [Assignment: organization-defined additional, more detailed information].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-3(2) Centralized Management of Planned Audit Record Content

<blockquote>Provide centralized management and configuration of the content to be captured in audit records
generated by [Assignment: organization-defined system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-3(3) Limit Personally Identifiable Information Elements

<blockquote>Limit personally identifiable information contained in audit records to the following elements
identified in the privacy risk assessment: [Assignment: organization-defined elements].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-4 Audit Storage Capacity

<blockquote>Allocate audit record storage capacity to accommodate [Assignment: organization-defined audit record retention requirements].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-4(1) Transfer to Alternate Storage

<blockquote>Off-load audit records [Assignment: organization-defined frequency] onto a different system or
media than the system being audited.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-5 Response to Audit Processing Failures

<blockquote>a.    Alert [Assignment: organization-defined personnel or roles] in the event of an audit
      processing failure within [Assignment: organization-defined time-period]; and
b.    Take the following additional actions: [Assignment: organization-defined actions to be taken].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_5_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-5(1) Audit Storage Capacity

<blockquote>Provide a warning to [Assignment: organization-defined personnel, roles, and/or locations] within
[Assignment: organization-defined time-period] when allocated audit record storage volume
reaches [Assignment: organization-defined percentage] of repository maximum audit record
storage capacity.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_5_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_5_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-5(2) Real-Time Alerts

<blockquote>Provide an alert in [Assignment: organization-defined real-time-period] to [Assignment: organization-defined personnel, roles, and/or locations] when the following audit failure events
occur: [Assignment: organization-defined audit failure events requiring real-time alerts].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_5_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_5_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-5(3) Configurable Traffic Volume Thresholds

<blockquote>Enforce configurable network communications traffic volume thresholds reflecting limits on
auditing capacity and [Selection: rejects; delays] network traffic above those thresholds.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_5_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_5_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-5(4) Shutdown on Failure

<blockquote>Invoke a [Selection: full system shutdown; partial system shutdown; degraded operational mode with limited mission/business functionality available] in the event of [Assignment: organization-defined audit failures], unless an alternate audit capability exists.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_5_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-6 Audit Review, Analysis, and Reporting

<blockquote>a.    Review and analyze system audit records [Assignment: organization-defined frequency] for
      indications of [Assignment: organization-defined inappropriate or unusual
activity]; b.    Report findings to [Assignment: organization-defined personnel or roles]; and
c.    Adjust the level of audit review, analysis, and reporting within the system when there is a
      change in risk based on law enforcement information, intelligence information,
or other
      credible sources of information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_6_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-6(1) Automated Process Integration

<blockquote>Employ automated mechanisms to integrate audit review, analysis, and reporting processes to
support organizational processes for investigation and response to suspicious activities.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_6_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_6_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-6(3) Correlate Audit Repositories

<blockquote>Analyze and correlate audit records across different repositories to gain organization-wide
situational awareness.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_6_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_6_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-6(4) Central Review and Analysis

<blockquote>Provide and implement the capability to centrally review and analyze audit records from multiple
components within the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_6_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_6_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-6(5) Integrated Analysis of Audit Records

<blockquote>Integrate analysis of audit records with analysis of [Selection (one or more): vulnerability scanning information; performance data; system monitoring information; &lt;1&gt;] to further enhance the ability to identify
inappropriate or unusual activity.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_6_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_6_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-6(6) Correlation With Physical Monitoring

<blockquote>Correlate information from audit records with information obtained from monitoring physical
access to further enhance the ability to identify suspicious, inappropriate, unusual, or malevolent
activity.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_6_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_6_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-6(7) Permitted Actions

<blockquote>Specify the permitted actions for each [Selection (one or more): system process; role; user]
associated with the review, analysis, and reporting of audit information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_6_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_6_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-6(8) Full Text Analysis of Privileged Commands

<blockquote>Perform a full text analysis of audited privileged commands in a physically distinct component or
subsystem of the system, or other system that is dedicated to that analysis.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_6_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_6_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-6(9) Correlation With Information From Nontechnical Sources

<blockquote>Correlate information from nontechnical sources with audit information to enhance organization-
wide situational awareness.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_6_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-7 Audit Reduction and Report Generation

<blockquote>Provide and implement an audit reduction and report generation capability that:
a.    Supports on-demand audit review, analysis, and reporting requirements and after-the-fact
      investigations of security incidents; and
b.    Does not alter the original content or time ordering of audit records.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_7_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-7(1) Automatic Processing

<blockquote>Provide and implement the capability to process audit records for events of interest based on
[Assignment: organization-defined audit fields within audit records].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_7_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_7_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-7(2) Automatic Sort and Search

<blockquote>Provide and implement the capability to sort and search audit records for events of interest based
on the content of [Assignment: organization-defined audit fields within audit records].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_7_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-8 Time Stamps

<blockquote>a.    Use internal system clocks to generate time stamps for audit records; and
b.    Record time stamps for audit records that can be mapped to Coordinated Universal Time or
      Greenwich Mean Time and meets [Assignment: organization-defined granularity of time measurement].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_8_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-8(1) Synchronization With Authoritative Time Source

<blockquote>(a)   Compare the internal system clocks [Assignment: organization-defined frequency] with
      [Assignment: organization-defined authoritative time source]; and
(b) Synchronize the internal system clocks to the authoritative time source when the time
    difference is greater than [Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_8_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_8_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-8(2) Secondary Authoritative Time Source

<blockquote>(a)   Identify a secondary authoritative time source that is in a different geographic region than the
      primary authoritative time source; and
(b) Synchronize the internal system clocks to the secondary authoritative time source if the
    primary authoritative time source is unavailable.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_8_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-9 Protection of Audit Information

<blockquote>Protect audit information and audit tools from unauthorized access, modification, and
deletion.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_9_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-9(1) Hardware Write-Once Media

<blockquote>Write audit trails to hardware-enforced, write-once media.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_9_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_9_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-9(2) Store on Separate Physical Systems or Components

<blockquote>Store audit records [Assignment: organization-defined frequency] in a repository that is part of a
physically different system or system component than the system or component being audited.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_9_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_9_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-9(3) Cryptographic Protection

<blockquote>Implement cryptographic mechanisms to protect the integrity of audit information and audit tools.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_9_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_9_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-9(4) Access by Subset of Privileged Users

<blockquote>Authorize access to management of audit functionality to only [Assignment: organization-defined subset of privileged users].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_9_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_9_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-9(5) Dual Authorization

<blockquote>Enforce dual authorization for [Selection (one or more): movement; deletion] of [Assignment: organization-defined audit information].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_9_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_9_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-9(6) Read-Only Access

<blockquote>Authorize read-only access to audit information to [Assignment: organization-defined subset of privileged users].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_9_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_9_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-9(7) Store on Component With Different Operating System

<blockquote>Store audit information on a component running a different operating system than the system or
component being audited.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_9_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-10 Non-repudiation

<blockquote>Protect against an individual (or process acting on behalf of an individual) falsely denying
having performed [Assignment: organization-defined actions to be covered by non-repudiation].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_10_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-10(1) Association of Identities

<blockquote>(a)   Bind the identity of the information producer with the information to [Assignment: organization-defined strength of binding]; and
(b) Provide the means for authorized individuals to determine the identity of the producer of the
    information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_10_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_10_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-10(2) Validate Binding of Information Producer Identity

<blockquote>(a)   Validate the binding of the information producer identity to the information at [Assignment: organization-defined frequency]; and
(b) Perform [Assignment: organization-defined actions] in the event of a validation error.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_10_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_10_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-10(3) Chain of Custody

<blockquote>Maintain reviewer or releaser identity and credentials within the established chain of custody for all
information reviewed or released.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_10_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_10_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-10(4) Validate Binding of Information Reviewer Identity

<blockquote>(a)   Validate the binding of the information reviewer identity to the information at the transfer or
      release points prior to release or transfer between [Assignment: organization-defined
security domains]; and (b) Perform [Assignment: organization-defined actions] in the event of a validation error.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_10_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-11 Audit Record Retention

<blockquote>Retain audit records for [Assignment: organization-defined time-period consistent with records retention policy] to provide support for after-the-fact investigations of security and
privacy incidents and to meet regulatory and organizational information retention requirements.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_11_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-11(1) Long-Term Retrieval Capability

<blockquote>Employ [Assignment: organization-defined measures] to ensure that long-term audit records
generated by the system can be retrieved.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_11_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-12 Audit Generation

<blockquote>a.    Provide audit record generation capability for the auditable event types in AU-2 a. at
      [Assignment: organization-defined system components];
b.    Allow [Assignment: organization-defined personnel or roles] to select which auditable event
      types are to be audited by specific components of the system; and
c.    Generate audit records for the event types defined in AU-2 d. with the content in AU-3.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_12_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-12(1) System-Wide and Time-Correlated Audit Trail

<blockquote>Compile audit records from [Assignment: organization-defined system components] into a system-
wide (logical or physical) audit trail that is time-correlated to within [Assignment: organization-defined level of tolerance for the relationship between time stamps of individual records in the audit trail].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_12_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_12_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-12(2) Standardized Formats

<blockquote>Produce a system-wide (logical or physical) audit trail composed of audit records in a standardized
format.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_12_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_12_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-12(3) Changes by Authorized Individuals

<blockquote>Provide and implement the capability for [Assignment: organization-defined individuals or roles] to
change the auditing to be performed on [Assignment: organization-defined system components]
based on [Assignment: organization-defined selectable event criteria] within [Assignment: organization-defined time thresholds].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_12_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_12_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-12(4) Query Parameter Audits of Personally Identifiable Information

<blockquote>Provide and implement the capability for auditing the parameters of user query events for data sets
containing personally identifiable information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_12_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-13 Monitoring for Information Disclosure

<blockquote>Monitor [Assignment: organization-defined open source information and/or information sites] [Assignment: organization-defined frequency] for evidence of unauthorized disclosure of
organizational information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_13_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-13(1) Use of Automated Tools

<blockquote>Employ automated mechanisms to determine if organizational information has been disclosed in
an unauthorized manner.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_13_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_13_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-13(2) Review of Monitored Sites

<blockquote>Review the open source information sites being monitored [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_13_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-14 Session Audit

<blockquote>Provide and implement the capability for authorized users to select a user session to
capture/record or view/hear.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_14_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-14(1) System Start-Up

<blockquote>Initiate session audits automatically at system start-up.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_14_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_14_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-14(2) Capture and Record Content

<blockquote>Provide and implement the capability for authorized users to capture, record, and log content
related to a user session.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_14_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_14_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-14(3) Remote Viewing and Listening

<blockquote>Provide and implement the capability for authorized users to remotely view and hear content
related to an established user session in real time.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_14_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-15 Alternate Audit Capability

<blockquote>Provide an alternate audit capability in the event of a failure in primary audit capability
that implements [Assignment: organization-defined alternate audit functionality].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-16 Cross-Organizational Auditing

<blockquote>Employ [Assignment: organization-defined methods] for coordinating [Assignment: organization-defined audit information] among external organizations when audit information is
transmitted across organizational boundaries.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_16_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-16(1) Identity Preservation

<blockquote>Require that the identity of individuals is preserved in cross-organizational audit trails.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_16_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_au_16_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### AU-16(2) Sharing of Audit Information

<blockquote>Provide cross-organizational audit information to [Assignment: organization-defined organizations] based on [Assignment: organization-defined cross-organizational sharing agreements].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_au_16_2_impl|safe}}
{% endif %}
{% endfor %}

## CA - Assessment, Authorization, and Monitoring


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-1 Assessment, Authorization, and Monitoring Policies and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A security and privacy assessment, authorization, and monitoring policy
that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives,
regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the security and privacy
assessment,
           authorization, and monitoring policy and the associated security and
privacy assessment,
           authorization, and monitoring controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     security and privacy assessment, authorization, and monitoring policy and
procedures; c.   Review and update the current security and privacy assessment, authorization, and
     monitoring:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the security and privacy assessment, authorization, and monitoring procedures
     implement the security and privacy assessment, authorization, and monitoring
policy and
     controls; and
e.   Develop, document, and implement remediation actions for violations of security and privacy
     assessment, authorization, and monitoring policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-2 Assessments

<blockquote>a.    Develop a security and privacy assessment plan that describes the scope of the assessment
      including:
      1.   Security and privacy controls and control enhancements under assessment;
      2.   Assessment procedures to be used to determine control effectiveness;
and
      3.   Assessment environment, assessment team, and assessment roles and responsibilities;
b.    Ensure the assessment plan is reviewed and approved by the authorizing official or designated
      representative prior to conducting the assessment;
c.    Assess the security and privacy controls in the system and its environment of operation
      [Assignment: organization-defined frequency] to determine the extent to
which the controls
      are implemented correctly, operating as intended, and producing the desired
outcome with
      respect to meeting established security and privacy requirements;
d.    Produce a security and privacy assessment report that document the results of the assessment;
      and
e.    Provide the results of the security and privacy control assessment to [Assignment: organization-defined individuals or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_2_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-2(1) Independent Assessors

<blockquote>Employ independent assessors or assessment teams to conduct security and privacy control
assessments.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_2_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_2_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-2(2) Specialized Assessments

<blockquote>Include as part of security and privacy control assessments, [Assignment: organization-defined frequency], [Selection: announced; unannounced], [Selection (one or more): in-depth monitoring; vulnerability scanning; malicious user testing; insider threat assessment; performance and load testing; &lt;2&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_2_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_2_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-2(3) External Organizations

<blockquote>Accept the results of security and privacy control assessments of [Assignment: organization-defined system] performed by [Assignment: organization-defined external organization] when the
assessment meets [Assignment: organization-defined requirements].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_2_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-3 System Interconnections

<blockquote>a.    Authorize connections from the system to other systems using Interconnection Security
      Agreements;
b.    Document, for each interconnection, the interface characteristics, security and privacy
      requirements, and the nature of the information communicated; and
c.    Review and update Interconnection Security Agreements [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-3(1) Unclassified National Security System Connections

<blockquote>Prohibit the direct connection of an [Assignment: organization-defined unclassified, national security system] to an external network without the use of [Assignment: organization-defined boundary protection device].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-3(2) Classified National Security System Connections

<blockquote>Prohibit the direct connection of a classified, national security system to an external network
without the use of [Assignment: organization-defined boundary protection device].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-3(3) Unclassified Non-National Security System Connections

<blockquote>Prohibit the direct connection of an [Assignment: organization-defined unclassified, non-national security system] to an external network without the use of [Assignment; organization-defined boundary protection device].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_3_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-3(4) Connections to Public Networks

<blockquote>Prohibit the direct connection of an [Assignment: organization-defined system] to a public
network.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_3_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_3_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-3(5) Restrictions on External System Connections

<blockquote>Employ a deny-all, permit-by-exception policy for allowing [Assignment: organization-defined systems] to connect to external systems.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_3_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_3_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-3(6) Secondary and Tertiary Connections

<blockquote>(a)   Identify secondary and tertiary connections to the interconnected systems; and
(b) Take measures to ensure that connections are severed when security and privacy controls on
    identified secondary and tertiary systems cannot be verified or validated.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_3_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-5 Plan of Action and Milestones

<blockquote>a.   Develop a plan of action and milestones for the system to document the planned remedial
     actions of the organization to correct weaknesses or deficiencies noted during the assessment
     of the controls and to reduce or eliminate known vulnerabilities in the system; and
b.   Update existing plan of action and milestones [Assignment: organization-defined frequency]
     based on the findings from control assessments, impact analyses, and continuous monitoring
     activities.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_5_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-5(1) Automation Support for Accuracy and Currency

<blockquote>Employ automated mechanisms to ensure that the plan of action and milestones for the system is
accurate, up to date, and readily available.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_5_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-6 Authorization

<blockquote>a.    Assign a senior-level executive or manager as the authorizing official for the system and for
      any common controls inherited by the system;
b.    Ensure that the authorizing official, before commencing operations:
      1.   Authorizes the system for processing; and
      2.   Authorizes the common controls inherited by the system; and
c.    Update the authorizations [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_6_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-6(1) Joint Authorization — Same Organization

<blockquote>Employ a joint authorization process for the system that includes multiple authorizing officials
from the same organization conducting the authorization.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_6_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_6_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-6(2) Joint Authorization — Different Organizations

<blockquote>Employ a joint authorization process for the system that includes multiple authorizing officials with
at least one authorizing official from an organization external to the organization conducting the
authorization.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_6_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-7 Continuous Monitoring

<blockquote>Develop a security and privacy continuous monitoring strategy and implement security
and privacy continuous monitoring programs that include:
 a.   Establishing the following security and privacy metrics to be monitored:
[Assignment: organization-defined metrics];
 b.   Establishing [Assignment: organization-defined frequencies] for monitoring
and
      [Assignment: organization-defined frequencies] for ongoing assessment of
security and
      privacy control effectiveness;
 c.   Ongoing security and privacy control assessments in accordance with the
organizational
      continuous monitoring strategy;
 d.   Ongoing security and privacy status monitoring of organization-defined metrics
in
      accordance with the organizational continuous monitoring strategy;
 e.   Correlation and analysis of security- and privacy-related information generated
by security
      and privacy control assessments and monitoring;
 f.   Response actions to address results of the analysis of security- and privacy-related
      information; and
 g.   Reporting the security and privacy status of the organization and organizational
systems to
      [Assignment: organization-defined personnel or roles] [Assignment: organization-defined
frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_7_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-7(1) Independent Assessment

<blockquote>Employ independent assessors or assessment teams to monitor the security and privacy controls
in the system on an ongoing basis.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_7_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_7_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-7(3) Trend Analyses

<blockquote>Employ trend analyses to determine if security and privacy control implementations, the frequency
of continuous monitoring activities, and the types of activities used in the continuous monitoring
process need to be modified based on empirical data.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_7_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_7_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-7(4) Risk Monitoring

<blockquote>Ensure risk monitoring is an integral part of the continuous monitoring strategy that includes the
following:
(a)   Effectiveness monitoring;
(b) Compliance monitoring; and
(c)   Change monitoring.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_7_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-8 Penetration Testing

<blockquote>Conduct penetration testing [Assignment: organization-defined frequency] on
[Assignment: organization-defined systems or system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_8_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-8(1) Independent Penetration Agent or Team

<blockquote>Employ an independent penetration agent or penetration team to perform penetration testing on
the system or system components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_8_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_8_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-8(2) Red Team Exercises

<blockquote>Employ [Assignment: organization-defined red team exercises] to simulate attempts by
adversaries to compromise organizational systems in accordance with applicable rules of
engagement.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_8_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_8_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-8(3) Facility Penetration Testing

<blockquote>Employ a penetration testing process that includes [Assignment: organization-defined frequency]
[Selection: announced; unannounced] attempts to bypass or circumvent controls associated with
physical access points to the facility.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_8_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-9 Internal System Connections

<blockquote>a.    Authorize internal connections of [Assignment: organization-defined system components or classes of components] to the system; and
b.    Document, for each internal connection, the interface characteristics, security and privacy
      requirements, and the nature of the information communicated.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ca_9_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CA-9(1) Compliance Checks

<blockquote>Perform security and privacy compliance checks on constituent system components prior to the
establishment of the internal connection.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ca_9_1_impl|safe}}
{% endif %}
{% endfor %}

## CM - Configuration Management


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-1 Configuration Management Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A configuration management policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the configuration management policy and
           the associated configuration management controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage
     configuration management policy and procedures;
c.   Review and update the current configuration management:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the configuration management procedures implement the configuration
     management policy and controls; and
e.   Develop, document, and implement remediation actions for violations of the configuration
     management policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-2 Baseline Configuration

<blockquote>a.   Develop, document, and maintain under configuration control, a current baseline
     configuration of the system; and
b.   Review and update the baseline configuration of the system:




      1.   [Assignment: organization-defined frequency];
      2.   When required due to [Assignment organization-defined circumstances]; and
      3.   When system components are installed or upgraded.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_2_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-2(2) Automation Support for Accuracy and Currency

<blockquote>Employ automated mechanisms to maintain an up-to-date, complete, accurate, and readily
available baseline configuration of the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_2_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_2_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-2(3) Retention of Previous Configurations

<blockquote>Retain [Assignment: organization-defined previous versions of baseline configurations of the system] to support rollback.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_2_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_2_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-2(6) Development and Test Environments

<blockquote>Maintain a baseline configuration for system development and test environments that is managed
separately from the operational baseline configuration.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_2_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_2_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-2(7) Configure Systems and Components for High-Risk Areas

<blockquote>(a)   Issue [Assignment: organization-defined systems or system components] with [Assignment: organization-defined configurations] to individuals traveling to locations that the organization
      deems to be of significant risk; and
(b) Apply [Assignment: organization-defined security safeguards] to the components when the
    individuals return from travel.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_2_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-3 Configuration Change Control

<blockquote>a.    Determine the types of changes to the system that are configuration-controlled;
b.    Review proposed configuration-controlled changes to the system and approve or disapprove
      such changes with explicit consideration for security impact analyses;
c.    Document configuration change decisions associated with the system;
d.    Implement approved configuration-controlled changes to the system;
e.    Retain records of configuration-controlled changes to the system for [Assignment: organization-defined time-period];
f.    Monitor and review activities associated with configuration-controlled changes to the system;
      and
g.    Coordinate and provide oversight for configuration change control activities through
      [Assignment: organization-defined configuration change control element]
that convenes
      [Selection (one or more): &lt;3&gt;; &lt;4&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-3(1) Automated Documentation, Notification, and Prohibition of Changes

<blockquote>Employ automated mechanisms to:
(a)   Document proposed changes to the system;
(b) Notify [Assignment: organized-defined approval authorities] of proposed changes to the
    system and request change approval;
(c)   Highlight proposed changes to the system that have not been approved or disapproved by
      [Assignment: organization-defined time-period];
(d) Prohibit changes to the system until designated approvals are received;
(e)   Document all changes to the system; and
(f)   Notify [Assignment: organization-defined personnel] when approved changes to the system
      are completed.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-3(2) Testing, Validation, and Documentation of Changes

<blockquote>Test, validate, and document changes to the system before fully implementing the changes on the
system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-3(3) Automated Change Implementation

<blockquote>Employ automated mechanisms to implement changes to the current system baseline and deploy
the updated baseline across the installed base.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_3_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-3(4) Security Representative

<blockquote>Require an [Assignment: organization-defined information security representative] to be a member
of the [Assignment: organization-defined configuration change control element].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_3_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_3_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-3(5) Automated Security Response

<blockquote>Implement [Assignment: organization-defined security responses] automatically if baseline
configurations are changed in an unauthorized manner.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_3_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_3_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-3(6) Cryptography Management

<blockquote>Ensure that cryptographic mechanisms used to provide [Assignment: organization-defined security safeguards] are under configuration management.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_3_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-4 Security and Privacy Impact Analyses

<blockquote>Analyze changes to the system to determine potential security and privacy impacts prior to
change implementation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-4(1) Separate Test Environments

<blockquote>Analyze changes to the system in a separate test environment before implementation in an
operational environment, looking for security and privacy impacts due to flaws, weaknesses,
incompatibility, or intentional malice.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_4_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-4(2) Verification of Security and Privacy Functions

<blockquote>Check the security and privacy functions after system changes, to verify that the functions are
implemented correctly, operating as intended, and producing the desired outcome with regard to
meeting the security and privacy requirements for the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_4_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-5 Access Restrictions for Change

<blockquote>Define, document, approve, and enforce physical and logical access restrictions associated
with changes to the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_5_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-5(1) Automated Access Enforcement and Auditing

<blockquote>(a)   Enforce access restrictions; and
(b) Generate audit records of the enforcement actions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_5_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_5_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-5(2) Review System Changes

<blockquote>Review system changes [Assignment: organization-defined frequency] and [Assignment: organization-defined circumstances] to determine whether unauthorized changes have occurred.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_5_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_5_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-5(3) Signed Components

<blockquote>Prevent the installation of [Assignment: organization-defined software and firmware components]
without verification that the component has been digitally signed using a certificate that is
recognized and approved by the organization.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_5_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_5_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-5(4) Dual Authorization

<blockquote>Enforce dual authorization for implementing changes to [Assignment: organization-defined system components and system-level information].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_5_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_5_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-5(5) Privilege Limitation for Production and Operation

<blockquote>(a)   Limit privileges to change system components and system-related information within a
      production or operational environment; and
(b) Review and reevaluate privileges [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_5_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_5_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-5(6) Limit Library Privileges

<blockquote>Limit privileges to change software resident within software libraries.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_5_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-6 Configuration Settings

<blockquote>a.    Establish and document configuration settings for components employed within the system
      using [Assignment: organization-defined common secure configurations] that
reflect the most
      restrictive mode consistent with operational requirements;
b.    Implement the configuration settings;
c.    Identify, document, and approve any deviations from established configuration settings for
      [Assignment: organization-defined system components] based on [Assignment:
organization-defined operational requirements]; and d.    Monitor and control changes to the configuration settings in accordance with organizational
      policies and procedures.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_6_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-6(1) Automated Management, Application, and Verification

<blockquote>Employ automated mechanisms to centrally manage, apply, and verify configuration settings for
[Assignment: organization-defined system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_6_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_6_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-6(2) Respond to Unauthorized Changes

<blockquote>Employ [Assignment: organization-defined security safeguards] to respond to unauthorized
changes to [Assignment: organization-defined configuration settings].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_6_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-7 Least Functionality

<blockquote>a.    Configure the system to provide only essential capabilities; and
b.    Prohibit or restrict the use of the following functions, ports, protocols, and/or services:
      [Assignment: organization-defined prohibited or restricted functions, ports, protocols, and/or services].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_7_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-7(1) Periodic Review

<blockquote>(a)   Review the system [Assignment: organization-defined frequency] to identify unnecessary
      and/or nonsecure functions, ports, protocols, and services; and
(b) Disable [Assignment: organization-defined functions, ports, protocols, and services within the system deemed to be unnecessary and/or nonsecure].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_7_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_7_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-7(2) Prevent Program Execution

<blockquote>Prevent program execution in accordance with [Selection (one or more): &lt;1&gt;; rules authorizing the terms and conditions of software program usage].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_7_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_7_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-7(3) Registration Compliance

<blockquote>Ensure compliance with [Assignment: organization-defined registration requirements for functions, ports, protocols, and services].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_7_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_7_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-7(4) Unauthorized Software — Blacklisting

<blockquote>(a)   Identify [Assignment: organization-defined software programs not authorized to execute on the system];
(b) Employ an allow-all, deny-by-exception policy to prohibit the execution of unauthorized
    software programs on the system; and
(c)   Review and update the list of unauthorized software programs [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_7_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_7_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-7(5) Authorized Software — Whitelisting

<blockquote>(a)   Identify [Assignment: organization-defined software programs authorized to execute on the system];
(b) Employ a deny-all, permit-by-exception policy to allow the execution of authorized software
    programs on the system; and
(c)   Review and update the list of authorized software programs [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_7_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-8 System Component Inventory

<blockquote>a.    Develop and document an inventory of system components that:
      1.   Accurately reflects the current system;
      2.   Includes all components within the authorization boundary of the system;
      3.   Is at the level of granularity deemed necessary for tracking and reporting;
and
      4.   Includes [Assignment: organization-defined information deemed necessary
to achieve effective system component accountability]; and b.    Review and update the system component inventory [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_8_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-8(1) Updates During Installation and Removal

<blockquote>Update the inventory of system components as an integral part of component installations,
removals, and system updates.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_8_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_8_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-8(2) Automated Maintenance

<blockquote>Employ automated mechanisms to help maintain an up-to-date, complete, accurate, and readily
available inventory of system components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_8_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_8_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-8(3) Automated Unauthorized Component Detection

<blockquote>(a)   Employ automated mechanisms [Assignment: organization-defined frequency] to detect the
      presence of unauthorized hardware, software, and firmware components within
the system;
      and
(b) Take the following actions when unauthorized components are detected: [Selection (one or more): disable network access by such components; isolate the components; notify &lt;2&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_8_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_8_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-8(4) Accountability Information

<blockquote>Includes in the system component inventory information, a means for identifying by [Selection (one or more): name; position; role], individuals responsible and accountable for administering
those components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_8_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_8_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-8(5) no Duplicate Accounting of Components

<blockquote>(a)   Verify that all components within the authorization boundary of the system are not duplicated
      in other system component inventories; or
(b) If a centralized component inventory is used, verify components are not assigned to multiple
    systems.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_8_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_8_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-8(6) Assessed Configurations and Approved Deviations

<blockquote>Include assessed component configurations and any approved deviations to current deployed
configurations in the system component inventory.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_8_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_8_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-8(7) Centralized Repository

<blockquote>Provide a centralized repository for the inventory of system components.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_8_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_8_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-8(8) Automated Location Tracking

<blockquote>Employ automated mechanisms to support tracking of system components by geographic
location.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_8_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_8_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-8(9) Assignment of Components to Systems

<blockquote>(a)   Assign [Assignment: organization-defined acquired system components] to a system; and
(b) Receive an acknowledgement from [Assignment: organization-defined personnel or roles] of
    this assignment.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_8_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_8_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-8(10) Data Action Mapping

<blockquote>Develop and document a system map of data actions that process personally identifiable
information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_8_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-9 Configuration Management Plan

<blockquote>Develop, document, and implement a configuration management plan for the system that:
a.    Addresses roles, responsibilities, and configuration management processes and procedures;
b.    Establishes a process for identifying configuration items throughout the system development
      life cycle and for managing the configuration of the configuration items;
c.    Defines the configuration items for the system and places the configuration items under
      configuration management;
d.    Is reviewed and approved by [Assignment: organization-defined personnel or roles]; and
e.    Protects the configuration management plan from unauthorized disclosure and modification.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_9_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-9(1) Assignment of Responsibility

<blockquote>Assign responsibility for developing the configuration management process to organizational
personnel that are not directly involved in system development.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_9_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-10 Software Usage Restrictions

<blockquote>a.    Use software and associated documentation in accordance with contract agreements and
      copyright laws;
b.    Track the use of software and associated documentation protected by quantity licenses to
      control copying and distribution; and
c.    Control and document the use of peer-to-peer file sharing technology to ensure that this
      capability is not used for the unauthorized distribution, display, performance, or reproduction
      of copyrighted work.
                     Software license tracking can be accomplished by manual methods or
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_10_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-10(1) Open Source Software

<blockquote>Establish the following restrictions on the use of open source software: [Assignment: organization-defined restrictions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_10_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-11 User-Installed Software

<blockquote>a.    Establish [Assignment: organization-defined policies] governing the installation of software
      by users;
b.    Enforce software installation policies through the following methods: [Assignment: organization-defined methods]; and
c.    Monitor policy compliance at [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_11_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-11(2) Software Installation With Privileged Status

<blockquote>Allow user installation of software only with explicit privileged status.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_11_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-12 Information Location

<blockquote>a.    Identify the location of [Assignment: organization-defined information] and the specific
      system components on which the information resides;
b.    Identify and document the users who have access to the system and system components where
      the information resides; and
c.    Document changes to the location (i.e., system or system components) where the information
      resides.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cm_12_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CM-12(1) Automated Tools to Support Information Location

<blockquote>Use automated tools to identify [Assignment: organization-defined information by information type] on [Assignment: organization-defined system components] to ensure adequate security and
privacy controls are in place to protect organizational information and individual privacy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cm_12_1_impl|safe}}
{% endif %}
{% endfor %}

## CP - Contingency Planning


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-1 Contingency Planning Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A contingency planning policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the contingency planning policy and the
           associated contingency planning controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     contingency planning policy and procedures;
c.   Review and update the current contingency planning:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the contingency planning procedures implement the contingency planning policy
     and controls; and
e.   Develop, document, and implement remediation actions for violations of the contingency
     planning policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-2 Contingency Plan

<blockquote>a.   Develop a contingency plan for the system that:
     1.    Identifies essential missions and business functions and associated contingency
           requirements;




      2.   Provides recovery objectives, restoration priorities, and metrics;
      3.   Addresses contingency roles, responsibilities, assigned individuals with contact
           information;
      4.   Addresses maintaining essential missions and business functions despite a system
           disruption, compromise, or failure;
      5.   Addresses eventual, full system restoration without deterioration of the security and
           privacy controls originally planned and implemented; and
      6.   Is reviewed and approved by [Assignment: organization-defined personnel or roles];
b.    Distributes copies of the contingency plan to [Assignment: organization-defined key contingency personnel (identified by name and/or by role) and organizational elements];
c.    Coordinates contingency planning activities with incident handling activities;
d.    Reviews the contingency plan for the system [Assignment: organization-defined frequency];
e.    Updates the contingency plan to address changes to the organization, system, or environment
      of operation and problems encountered during contingency plan implementation, execution,
      or testing;
f.    Communicates contingency plan changes to [Assignment: organization-defined key contingency personnel (identified by name and/or by role) and organizational elements]; and
g.    Protects the contingency plan from unauthorized disclosure and modification.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_2_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-2(1) Coordinate With Related Plans

<blockquote>Coordinate contingency plan development with organizational elements responsible for related
plans.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_2_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_2_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-2(2) Capacity Planning

<blockquote>Conduct capacity planning so that necessary capacity for information processing,
telecommunications, and environmental support exists during contingency operations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_2_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_2_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-2(3) Resume Essential Missions and Business Functions

<blockquote>Plan for the resumption of essential missions and business functions within [Assignment: organization-defined time-period] of contingency plan activation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_2_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_2_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-2(4) Resume All Missions and Business Functions

<blockquote>Plan for the resumption of all missions and business functions within [Assignment: organization-defined time-period] of contingency plan activation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_2_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_2_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-2(5) Continue Essential Missions and Business Functions

<blockquote>Plan for the continuance of essential missions and business functions with little or no loss of
operational continuity and sustains that continuity until full system restoration at primary
processing and/or storage sites.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_2_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_2_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-2(6) Alternate Processing and Storage Sites

<blockquote>Plan for the transfer of essential missions and business functions to alternate processing and/or
storage sites with little or no loss of operational continuity and sustain that continuity through
system restoration to primary processing and/or storage sites.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_2_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_2_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-2(7) Coordinate With External Service Providers

<blockquote>Coordinate the contingency plan with the contingency plans of external service providers to
ensure that contingency requirements can be satisfied.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_2_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_2_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-2(8) Identify Critical Assets

<blockquote>Identify critical system assets supporting essential missions and business functions.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_2_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-3 Contingency Training

<blockquote>Provide contingency training to system users consistent with assigned roles and
responsibilities:
a.    Within [Assignment: organization-defined time-period] of assuming a contingency role or
      responsibility;
b.    When required by system changes; and
c.    [Assignment: organization-defined frequency] thereafter.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-3(1) Simulated Events

<blockquote>Incorporate simulated events into contingency training to facilitate effective response by personnel
in crisis situations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-3(2) Automated Training Environments

<blockquote>Employ automated mechanisms to provide a more thorough and realistic contingency training
environment.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-4 Contingency Plan Testing

<blockquote>a.    Test the contingency plan for the system [Assignment: organization-defined frequency] using
      [Assignment: organization-defined tests] to determine the effectiveness of the plan and the
      organizational readiness to execute the plan;
b.    Review the contingency plan test results; and
c.    Initiate corrective actions, if needed.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-4(1) Coordinate With Related Plans

<blockquote>Coordinate contingency plan testing with organizational elements responsible for related plans.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_4_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-4(2) Alternate Processing Site

<blockquote>Test the contingency plan at the alternate processing site:
(a)   To familiarize contingency personnel with the facility and available resources; and
(b) To evaluate the capabilities of the alternate processing site to support contingency
    operations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_4_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_4_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-4(3) Automated Testing

<blockquote>Employ automated mechanisms to more thoroughly and effectively test the contingency plan.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_4_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_4_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-4(4) Full Recovery and Reconstitution

<blockquote>Include a full recovery and reconstitution of the system to a known state as part of contingency
plan testing.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_4_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-6 Alternate Storage Site

<blockquote>a.    Establish an alternate storage site including necessary agreements to permit the storage and
      retrieval of system backup information; and
b.    Ensure that the alternate storage site provides security controls equivalent to that of the
      primary site.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_6_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-6(1) Separation From Primary Site

<blockquote>Identify an alternate storage site that is separated from the primary storage site to reduce
susceptibility to the same threats.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_6_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_6_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-6(2) Recovery Time and Recovery Point Objectives

<blockquote>Configure the alternate storage site to facilitate recovery operations in accordance with recovery
time and recovery point objectives.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_6_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_6_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-6(3) Accessibility

<blockquote>Identify potential accessibility problems to the alternate storage site in the event of an area-wide
disruption or disaster and outlines explicit mitigation actions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_6_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-7 Alternate Processing Site

<blockquote>a.    Establish an alternate processing site including necessary agreements to permit the transfer
      and resumption of [Assignment: organization-defined system operations] for
essential
      missions and business functions within [Assignment: organization-defined
time-period consistent with recovery time and recovery point objectives] when the primary processing
      capabilities are unavailable;
b.    Make available at the alternate processing site, the equipment and supplies required to transfer
      and resume operations or put contracts in place to support delivery to the
site within the
      organization-defined time-period for transfer and resumption; and
c.    Provide information security and privacy safeguards at the alternate processing site that are
      equivalent to those at the primary site.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_7_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-7(1) Separation From Primary Site

<blockquote>Identify an alternate processing site that is separated from the primary processing site to reduce
susceptibility to the same threats.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_7_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_7_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-7(2) Accessibility

<blockquote>Identify potential accessibility problems to the alternate processing site in the event of an area-
wide disruption or disaster and outlines explicit mitigation actions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_7_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_7_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-7(3) Priority of Service

<blockquote>Develop alternate processing site agreements that contain priority-of-service provisions in
accordance with organizational availability requirements (including recovery time objectives).
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_7_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_7_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-7(4) Preparation for Use

<blockquote>Prepare the alternate processing site so that the site is ready to be used as the operational site
supporting essential missions and business functions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_7_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_7_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-7(6) Inability to Return to Primary Site

<blockquote>Plan and prepare for circumstances that preclude returning to the primary processing site.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_7_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-8 Telecommunications Services

<blockquote>Establish alternate telecommunications services including necessary agreements to permit
the resumption of [Assignment: organization-defined system operations] for essential missions and
business functions within [Assignment: organization-defined time-period] when the primary
telecommunications capabilities are unavailable at either the primary or alternate processing or
storage sites.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_8_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-8(1) Priority of Service Provisions

<blockquote>(a)   Develop primary and alternate telecommunications service agreements that contain priority-
      of-service provisions in accordance with organizational availability requirements (including
      recovery time objectives); and
(b) Request Telecommunications Service Priority for all telecommunications services used for
    national security emergency preparedness if the primary and/or alternate telecommunications
    services are provided by a common carrier.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_8_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_8_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-8(2) Single Points of Failure

<blockquote>Obtain alternate telecommunications services to reduce the likelihood of sharing a single point of
failure with primary telecommunications services.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_8_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_8_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-8(3) Separation of Primary and Alternate Providers

<blockquote>Obtain alternate telecommunications services from providers that are separated from primary
service providers to reduce susceptibility to the same threats.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_8_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_8_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-8(4) Provider Contingency Plan

<blockquote>(a)   Require primary and alternate telecommunications service providers to have contingency
      plans;
(b) Review provider contingency plans to ensure that the plans meet organizational contingency
    requirements; and
(c)   Obtain evidence of contingency testing and training by providers [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_8_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_8_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-8(5) Alternate Telecommunication Service Testing

<blockquote>Test alternate telecommunication services [Assignment: organization-defined frequency].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_8_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-9 System Backup

<blockquote>a.    Conduct backups of user-level information contained in the system [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives];
b.    Conduct backups of system-level information contained in the system [Assignment: organization-defined frequency consistent with recovery time and recovery point objectives];
c.    Conduct backups of system documentation including security-related documentation
      [Assignment: organization-defined frequency consistent with recovery time
and recovery point objectives]; and d.    Protect the confidentiality, integrity, and availability of backup information at storage
      locations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_9_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-9(1) Testing for Reliability and Integrity

<blockquote>Test backup information [Assignment: organization-defined frequency] to verify media reliability
and information integrity.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_9_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_9_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-9(2) Test Restoration Using Sampling

<blockquote>Use a sample of backup information in the restoration of selected system functions as part of
contingency plan testing.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_9_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_9_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-9(3) Separate Storage for Critical Information

<blockquote>Store backup copies of [Assignment: organization-defined critical system software and other security-related information] in a separate facility or in a fire-rated container that is not collocated
with the operational system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_9_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_9_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-9(5) Transfer to Alternate Storage Site

<blockquote>Transfer system backup information to the alternate storage site [Assignment: organization-defined time-period and transfer rate consistent with the recovery time and recovery point objectives].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_9_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_9_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-9(6) Redundant Secondary System

<blockquote>Conduct system backup by maintaining a redundant secondary system that is not collocated with
the primary system and that can be activated without loss of information or disruption to
operations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_9_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_9_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-9(7) Dual Authorization

<blockquote>Enforce dual authorization for the deletion or destruction of [Assignment: organization-defined backup information].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_9_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_9_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-9(8) Cryptographic Protection

<blockquote>Implement cryptographic mechanisms to prevent unauthorized disclosure and modification of
[Assignment: organization-defined backup information].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_9_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-10 System Recovery and Reconstitution

<blockquote>Provide for the recovery and reconstitution of the system to a known state after a
disruption, compromise, or failure within [Assignment: organization-defined time-period consistent with recovery time and recovery point objectives].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_10_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-10(2) Transaction Recovery

<blockquote>Implement transaction recovery for systems that are transaction-based.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_10_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_10_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-10(4) Restore Within Time-Period

<blockquote>Provide the capability to restore system components within [Assignment: organization-defined restoration time-periods] from configuration-controlled and integrity-protected information
representing a known, operational state for the components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_10_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_10_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-10(6) Component Protection

<blockquote>Protect system components used for backup and restoration.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_10_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-11 Alternate Communications Protocols

<blockquote>Provide the capability to employ [Assignment: organization-defined alternative communications protocols] in support of maintaining continuity of operations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-12 Safe Mode

<blockquote>When [Assignment: organization-defined conditions] are detected, enter a safe mode of
operation with [Assignment: organization-defined restrictions of safe mode of operation].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_cp_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### CP-13 Alternative Security Mechanisms

<blockquote>Employ [Assignment: organization-defined alternative or supplemental security mechanisms] for satisfying [Assignment: organization-defined security functions] when the
primary means of implementing the security function is unavailable or compromised.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_cp_13_impl|safe}}
{% endif %}
{% endfor %}

## IA - Identification and Authentication


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-1 Identification and Authentication Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    An identification and authentication policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives,
regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the identification and
authentication policy
           and the associated identification and authentication controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     identification and authentication policy and procedures;
c.   Review and update the current identification and authentication:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the identification and authentication procedures implement the identification and
     authentication policy and controls; and
e.   Develop, document, and implement remediation actions for violations of the identification
     and authentication policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-2 Identification and Authentication (Organizational Users)

<blockquote>Uniquely identify and authenticate organizational users or processes acting on behalf of
organizational users.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_2_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-2(1) Multifactor Authentication to Privileged Accounts

<blockquote>Implement multifactor authentication for access to privileged accounts.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_2_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_2_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-2(2) Multifactor Authentication to Non-Privileged Accounts

<blockquote>Implement multifactor authentication for access to non-privileged accounts.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_2_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_2_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-2(5) Individual Authentication With Group Authentication

<blockquote>When shared accounts or authenticators are employed, require users to be individually
authenticated before granting access to the shared accounts or resources.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_2_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_2_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-2(8) Access to Accounts — Replay Resistant

<blockquote>Implement replay-resistant authentication mechanisms for access to [Selection (one or more): privileged accounts; non-privileged accounts].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_2_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_2_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-2(10) Single Sign-On

<blockquote>Provide a single sign-on capability for [Assignment: organization-defined system accounts and services].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_2_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_2_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-2(12) Acceptance of Piv Credentials

<blockquote>Accept and electronically verify Personal Identity Verification credentials.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_2_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-3 Device Identification and Authentication

<blockquote>Uniquely identify and authenticate [Assignment: organization-defined specific and/or types of devices] before establishing a [Selection (one or more): local; remote; network]
connection.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-3(1) Cryptographic Bidirectional Authentication

<blockquote>Authenticate [Assignment: organization-defined specific devices and/or types of devices] before
establishing [Selection (one or more): local; remote; network] connection using bidirectional
authentication that is cryptographically based.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-3(3) Dynamic Address Allocation

<blockquote>(a)   Where addresses are allocated dynamically, standardize dynamic address allocation lease
      information and the lease duration assigned to devices in accordance with
[Assignment: organization-defined lease information and lease duration]; and (b) Audit lease information when assigned to a device.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_3_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-3(4) Device Attestation

<blockquote>Handle device identification and authentication based on attestation by [Assignment: organization-defined configuration management process].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_3_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-4 Identifier Management

<blockquote>Manage system identifiers by:
a.    Receiving authorization from [Assignment: organization-defined personnel or roles] to assign
      an individual, group, role, or device identifier;
b.    Selecting an identifier that identifies an individual, group, role, or device;
c.    Assigning the identifier to the intended individual, group, role, or device; and
d.    Preventing reuse of identifiers for [Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-4(1) Prohibit Account Identifiers As Public Identifiers

<blockquote>Prohibit the use of system account identifiers that are the same as public identifiers for individual
electronic mail accounts.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_4_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-4(4) Identify User Status

<blockquote>Manage individual identifiers by uniquely identifying each individual as [Assignment: organization-defined characteristic identifying individual status].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_4_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_4_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-4(5) Dynamic Management

<blockquote>Manage individual identifiers dynamically.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_4_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_4_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-4(6) Cross-Organization Management

<blockquote>Coordinate with [Assignment: organization-defined external organizations] for cross-organization
management of identifiers.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_4_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_4_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-4(8) Pairwise Pseudonymous Identifiers

<blockquote>Generate pairwise pseudonymous identifiers.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_4_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5 Authenticator Management

<blockquote>Manage system authenticators by:
a.    Verifying, as part of the initial authenticator distribution, the identity of the individual, group,
      role, or device receiving the authenticator;
b.    Establishing initial authenticator content for any authenticators issued by the organization;
c.    Ensuring that authenticators have sufficient strength of mechanism for their intended use;
d.    Establishing and implementing administrative procedures for initial authenticator distribution,
      for lost/compromised or damaged authenticators, and for revoking authenticators;
e.    Establishing minimum and maximum lifetime restrictions and reuse conditions for
      authenticators;




f.    Changing/refreshing authenticators [Assignment: organization-defined time-period by authenticator type];
g.    Protecting authenticator content from unauthorized disclosure and modification;
h.    Requiring individuals to take, and having devices implement, specific security controls to
      protect authenticators; and
i.    Changing authenticators for group/role accounts when membership to those accounts changes.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(1) Password-Based Authentication

<blockquote>For password-based authentication:
(a)   Maintain a list of commonly-used, expected, or compromised passwords and update the list
      [Assignment: organization-defined frequency] and when organizational passwords are
      suspected to have been compromised directly or indirectly;
(b) Verify, when users create or update passwords, that the passwords are not found on the
    organization-defined list of commonly-used, expected, or compromised passwords;
(c)   Transmit only cryptographically-protected passwords;
(d) Store passwords using an approved hash algorithm and salt, preferably using a keyed hash;
(e)   Require immediate selection of a new password upon account recovery;
(f)   Allow user selection of long passwords and passphrases, including spaces and all printable
      characters; and
(g) Employ automated tools to assist the user in selecting strong password authenticators.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(2) Public Key-Based Authentication

<blockquote>For public key-based authentication:
(a)   Enforce authorized access to the corresponding private key; and
(b) Map the authenticated identity to the account of the individual or group; and
When public key infrastructure (PKI) is used:
(c)   Validate certificates by constructing and verifying a certification path to an accepted trust
      anchor including checking certificate status information; and
(d) Implement a local cache of revocation data to support path discovery and validation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(5) Change Authenticators Prior to Delivery

<blockquote>Require developers and installers of system components to provide unique authenticators or
change default authenticators prior to delivery and installation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(6) Protection of Authenticators

<blockquote>Protect authenticators commensurate with the security category of the information to which use of
the authenticator permits access.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(7) no Embedded Unencrypted Static Authenticators

<blockquote>Ensure that unencrypted static authenticators are not embedded in applications or access scripts
or stored on function keys.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(8) Multiple System Accounts

<blockquote>Implement [Assignment: organization-defined security safeguards] to manage the risk of
compromise due to individuals having accounts on multiple systems.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(9) Federated Credential Management

<blockquote>Use [Assignment: organization-defined external organizations] to federate authenticators.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(10) Dynamic Credential Binding

<blockquote>Bind identities and authenticators dynamically.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(12) Biometric Authentication Performance

<blockquote>For biometric-based authentication, employ mechanisms that satisfy [Assignment: organization-defined biometric quality requirements].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(13) Expiration of Cached Authenticators

<blockquote>Prohibit the use of cached authenticators after [Assignment: organization-defined time-period].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(14) Managing Content of Pki Trust Stores

<blockquote>For PKI-based authentication, employ a deliberate organization-wide methodology for managing
the content of PKI trust stores installed across all platforms including networks, operating
systems, browsers, and applications.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(15) Gsa-Approved Products and Services

<blockquote>Use only General Services Administration-approved and validated products and services.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(16) In-Person or Trusted External Party Authenticator Issuance

<blockquote>Require that the issuance of [Assignment: organization-defined types of and/or specific authenticators] be conducted [Selection: in person; by a trusted external party] before
[Assignment: organization-defined registration authority] with authorization by [Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_5_17_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-5(17) Presentation Attack Detection for Biometric Authenticators

<blockquote>Employ presentation attack detection mechanisms for biometric-based authentication.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_5_17_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-6 Authenticator Feedback

<blockquote>Obscure feedback of authentication information during the authentication process to
protect the information from possible exploitation and use by unauthorized individuals.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-7 Cryptographic Module Authentication

<blockquote>Implement mechanisms for authentication to a cryptographic module that meet the
requirements of applicable laws, Executive Orders, directives, policies, regulations, standards, and
guidelines for such authentication.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-8 Identification and Authentication (Non-Organizational Users)

<blockquote>Uniquely identify and authenticate non-organizational users or processes acting on behalf
of non-organizational users.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_8_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-8(1) Acceptance of Piv Credentials From Other Agencies

<blockquote>Accept and electronically verify Personal Identity Verification credentials from other federal
agencies.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_8_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_8_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-8(2) Acceptance of External Party Credentials

<blockquote>Accept only external credentials that are NIST compliant.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_8_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_8_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-8(4) Use of Nist-Issued Profiles

<blockquote>Conform to NIST-issued profiles for identity management.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_8_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_8_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-8(5) Acceptance of Piv-I Credentials

<blockquote>Accept and electronically verify Personal Identity Verification-I (PIV-I) credentials.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_8_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_8_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-8(6) Disassociability

<blockquote>Implement [Assignment: organization-defined measures] to disassociate user attributes or
credential assertion relationships among individuals, credential service providers, and relying
parties.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_8_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-9 Service Identification and Authentication

<blockquote>Identify and authenticate [Assignment: organization-defined system services and applications] before establishing communications with devices, users, or other services or
applications.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_9_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-9(1) Information Exchange

<blockquote>Ensure that service providers receive, validate, and transmit identification and authentication
information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_9_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_9_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-9(2) Transmission of Decisions

<blockquote>Transmit identification and authentication decisions between [Assignment: organization-defined services] consistent with organizational policies.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_9_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-10 Adaptive Authentication

<blockquote>Require individuals accessing the system to employ [Assignment: organization-defined supplemental authentication techniques or mechanisms] under specific [Assignment: organization-defined circumstances or situations].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-11 Re-authentication

<blockquote>Require users to re-authenticate when [Assignment: organization-defined circumstances or situations requiring re-authentication].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-12 Identity Proofing

<blockquote>a.    Identity proof users that require accounts for logical access to systems based on appropriate
      identity assurance level requirements as specified in applicable standards and guidelines;
b.    Resolve user identities to a unique individual; and





c.    Collect, validate, and verify identity evidence.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_12_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-12(1) Supervisor Authorization

<blockquote>Require that the registration process to receive an account for logical access includes supervisor
or sponsor authorization.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_12_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_12_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-12(2) Identity Evidence

<blockquote>Require evidence of individual identification be presented to the registration authority.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_12_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_12_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-12(3) Identity Evidence Validation and Verification

<blockquote>Require that the presented identity evidence be validated and verified through [Assignment: organizational defined methods of validation and verification].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_12_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_12_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-12(4) In-Person Validation and Verification

<blockquote>Require that the validation and verification of identity evidence be conducted in person before a
designated registration authority.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_12_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_12_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-12(5) Address Confirmation

<blockquote>Require that a [Selection: registration code; notice of proofing] be delivered through an out-of-
band channel to verify the users address (physical or digital) of record.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_12_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ia_12_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IA-12(6) Accept Externally-Proofed Identities

<blockquote>Accept externally-proofed identities at [Assignment: organization-defined identity assurance level].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ia_12_6_impl|safe}}
{% endif %}
{% endfor %}

## IP - Individual Participation


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ip_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IP-1 Individual Participation Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    An individual participation policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the individual participation policy and the
           associated individual participation controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     individual participation policy and procedures;
c.   Review and update the current individual participation:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the individual participation procedures implement the individual participation
     policy and controls; and
e.   Develop, document, and implement remediation actions for violations of the individual
     participation policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ip_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ip_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IP-2 Consent

<blockquote>Implement [Assignment: organization-defined tools or mechanisms] for users to authorize
the processing of their personally identifiable information prior to its collection that:
a.   Use plain language and provide examples to illustrate the potential privacy risks of the
     authorization; and




b.    Provide a means for users to decline the authorization.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ip_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ip_2_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IP-2(1) Attribute Management

<blockquote>Allow data subjects to tailor use permissions to selected attributes.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ip_2_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ip_2_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IP-2(2) Just-In-Time Notice of Consent

<blockquote>Present authorizations to process personally identifiable information in conjunction with the data
action or [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ip_2_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ip_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IP-3 Redress

<blockquote>a.    Establish and implement a process for individuals to have inaccurate personally identifiable
      information maintained by the organization corrected or amended; and
b.    Establish and implement a process for disseminating corrections or amendments of personally
      identifiable information to other authorized users of the personally identifiable
information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ip_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ip_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IP-3(1) Notice of Correction or Amendment

<blockquote>Notify affected individuals if their personally identifiable information has been corrected or
amended.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ip_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ip_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IP-3(2) Appeal

<blockquote>Provide [Assignment: organization-defined process] for individuals to appeal an adverse decision
and have incorrect information amended.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ip_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ip_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IP-4 Privacy Notice

<blockquote>a.    Make privacy notice(s) available to individuals upon first interacting with an organization,
      and subsequently [Assignment: organization-defined frequency].
b.    Ensure that privacy notices are clear and easy-to-understand, expressing information about
      personally identifiable information processing in plain language.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ip_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ip_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IP-4(1) Just-In-Time Notice of Privacy Authorization

<blockquote>Present authorizations to process personally identifiable information in conjunction with the data
action, or [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ip_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ip_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IP-5 Privacy Act Statements

<blockquote>a.   Include Privacy Act Statements on organizational forms that collect personally identifiable
     information, or on separate forms that can be retained by individuals; or
b.   Read a Privacy Act Statement to the individual prior to initiating the collection of personally
     identifiable information verbally.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ip_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ip_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IP-6 Individual Access

<blockquote>Provide individuals the ability to access their personally identifiable information
maintained in organizational systems of records.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ip_6_impl|safe}}
{% endif %}
{% endfor %}

## IR - Incident Response


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-1 Incident Response Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    An incident response policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the incident response policy and the
           associated incident response controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     incident response policy and procedures;
c.   Review and update the current incident response:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the incident response procedures implement the incident response policy and
     controls; and
e.   Develop, document, and implement remediation actions for violations of the incident
     response policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-2 Incident Response Training

<blockquote>Provide incident response training to system users consistent with assigned roles and
responsibilities:
a.   Within [Assignment: organization-defined time-period] of assuming an incident response role
     or responsibility;




b.    When required by system changes; and
c.    [Assignment: organization-defined frequency] thereafter.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_2_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-2(1) Simulated Events

<blockquote>Incorporate simulated events into incident response training to facilitate effective response by
personnel in crisis situations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_2_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_2_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-2(2) Automated Training Environments

<blockquote>Employ automated mechanisms to provide a more thorough and realistic incident response
training environment.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_2_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-3 Incident Response Testing

<blockquote>Test the incident response capability for the system [Assignment: organization-defined frequency] using [Assignment: organization-defined tests] to determine the incident response
effectiveness and documents the results.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-3(1) Automated Testing

<blockquote>Employ automated mechanisms to more thoroughly and effectively test the incident response
capability.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-3(2) Coordination With Related Plans

<blockquote>Coordinate incident response testing with organizational elements responsible for related plans.
                     Organizational plans related to incident response testing include, for
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-3(3) Continuous Improvement

<blockquote>Use qualitative and quantitative data from testing to:
(a)   Determine the effectiveness of incident response processes;
(b) Continuously improve incident response processes incorporating advanced information
    security practices; and
(c)   Provide incident response measures and metrics that are accurate, consistent, and in a
      reproducible format.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-4 Incident Handling

<blockquote>a.    Implement an incident handling capability for security and privacy incidents that includes
      preparation, detection and analysis, containment, eradication, and recovery;
b.    Coordinate incident handling activities with contingency planning activities;
c.    Incorporate lessons learned from ongoing incident handling activities into incident response
      procedures, training, and testing, and implement the resulting changes accordingly;
and d.    Ensure the rigor, intensity, scope, and results of incident handling activities are comparable
      and predictable across the organization.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-4(1) Automated Incident Handling Processes

<blockquote>Employ automated mechanisms to support the incident handling process.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_4_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-4(2) Dynamic Reconfiguration

<blockquote>Include dynamic reconfiguration of [Assignment: organization-defined system components] as
part of the incident response capability.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_4_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_4_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-4(3) Continuity of Operations

<blockquote>Identify [Assignment: organization-defined classes of incidents] and [Assignment: organization-defined actions to take in response to classes of incidents] to ensure continuation of
organizational missions and business functions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_4_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_4_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-4(4) Information Correlation

<blockquote>Correlate incident information and individual incident responses to achieve an organization-wide
perspective on incident awareness and response.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_4_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_4_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-4(5) Automatic Disabling of System

<blockquote>Implement a configurable capability to automatically disable the system if [Assignment: organization-defined security violations] are detected.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_4_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_4_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-4(6) Insider Threats — Specific Capabilities

<blockquote>Implement an incident handling capability for incidents involving insider threats.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_4_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_4_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-4(7) Insider Threats — Intra-Organization Coordination

<blockquote>Coordinate an incident handling capability for insider threats across [Assignment: organization-defined components or elements of the organization].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_4_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_4_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-4(8) Correlation With External Organizations

<blockquote>Coordinate with [Assignment: organization-defined external organizations] to correlate and share
[Assignment: organization-defined incident information] to achieve a cross-organization
perspective on incident awareness and more effective incident responses.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_4_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_4_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-4(9) Dynamic Response Capability

<blockquote>Employ [Assignment: organization-defined dynamic response capabilities] to effectively respond
to security incidents.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_4_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_4_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-4(10) Supply Chain Coordination

<blockquote>Coordinate incident handling activities involving supply chain events with other organizations
involved in the supply chain.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_4_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-5 Incident Monitoring

<blockquote>Track and document system security and privacy incidents.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_5_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-5(1) Automated Tracking, Data Collection, and Analysis

<blockquote>Employ automated mechanisms to assist in the tracking of security and privacy incidents and in
the collection and analysis of incident information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_5_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-6 Incident Reporting

<blockquote>a.    Require personnel to report suspected security and privacy incidents to the organizational
      incident response capability within [Assignment: organization-defined time-period];
and b.    Report security, privacy, and supply chain incident information to [Assignment: organization-defined authorities].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_6_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-6(1) Automated Reporting

<blockquote>Employ automated mechanisms to assist in the reporting of security and privacy incidents.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_6_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_6_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-6(2) Vulnerabilities Related to Incidents

<blockquote>Report system vulnerabilities associated with reported security and privacy incidents to
[Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_6_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_6_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-6(3) Supply Chain Coordination

<blockquote>Provide security and privacy incident information to the provider of the product or service and
other organizations involved in the supply chain for systems or system components related to the
incident.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_6_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-7 Incident Response Assistance

<blockquote>Provide an incident response support resource, integral to the organizational incident
response capability that offers advice and assistance to users of the system for the handling and
reporting of security and privacy incidents.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_7_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-7(1) Automation Support for Availability of Information and Support

<blockquote>Employ automated mechanisms to increase the availability of incident response-related
information and support.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_7_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_7_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-7(2) Coordination With External Providers

<blockquote>(a)   Establish a direct, cooperative relationship between its incident response capability and
      external providers of system protection capability; and
(b) Identify organizational incident response team members to the external providers.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_7_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-8 Incident Response Plan

<blockquote>a.    Develop an incident response plan that:
      1.    Provides the organization with a roadmap for implementing its incident response
            capability;
      2.    Describes the structure and organization of the incident response capability;
      3.    Provides a high-level approach for how the incident response capability fits into the
            overall organization;
      4.    Meets the unique requirements of the organization, which relate to mission, size,
            structure, and functions;
      5.    Defines reportable incidents;
      6.    Provides metrics for measuring the incident response capability within the organization;
      7.    Defines the resources and management support needed to effectively maintain and
            mature an incident response capability;
      8.    Is reviewed and approved by [Assignment: organization-defined personnel or roles]
            [Assignment: organization-defined frequency]; and
      9.    Explicitly designates responsibility for incident response to [Assignment: organization-defined entities, personnel, or roles].
b.    Distribute copies of the incident response plan to [Assignment: organization-defined incident response personnel (identified by name and/or by role) and organizational elements];
c.    Update the incident response plan to address system and organizational changes or problems
      encountered during plan implementation, execution, or testing;
d.    Communicate incident response plan changes to [Assignment: organization-defined incident response personnel (identified by name and/or by role) and organizational elements]; and





e.    Protect the incident response plan from unauthorized disclosure and modification.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_8_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-8(1) Personally Identifiable Information Processes

<blockquote>Include the following additional processes in the Incident Response Plan for incidents involving
personally identifiable information:
(a)   A process to determine if notice to oversight organizations is appropriate and to provide that
      notice, if appropriate;
(b) An assessment process to determine the extent of the harm, embarrassment, inconvenience,
    or unfairness to affected individuals; and
(c)   A process to ensure prompt reporting by organizational users of any privacy incident to
      [Assignment: organization-defined roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_8_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-9 Information Spillage Response

<blockquote>Respond to information spills by:
a.    Identifying the specific information involved in the system contamination;
b.    Alerting [Assignment: organization-defined personnel or roles] of the information spill using
      a method of communication not associated with the spill;
c.    Isolating the contaminated system or system component;
d.    Eradicating the information from the contaminated system or component;
e.    Identifying other systems or system components that may have been subsequently
      contaminated; and
f.    Performing the following additional actions: [Assignment: organization-defined actions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_9_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-9(1) Responsible Personnel

<blockquote>Assign [Assignment: organization-defined personnel or roles] with responsibility for responding to
information spills.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_9_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_9_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-9(2) Training

<blockquote>Provide information spillage response training [Assignment: organization-defined frequency].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_9_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_9_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-9(3) Post-Spill Operations

<blockquote>Implement [Assignment: organization-defined procedures] to ensure that organizational personnel
impacted by information spills can continue to carry out assigned tasks while contaminated
systems are undergoing corrective actions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_9_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_9_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-9(4) Exposure to Unauthorized Personnel

<blockquote>Employ [Assignment: organization-defined security safeguards] for personnel exposed to
information not within assigned access authorizations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_9_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ir_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### IR-10 Integrated Information Security Analysis Team

<blockquote>Establish an integrated team of forensic and malicious code analysts, tool developers, and
real-time operations personnel to handle incidents.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ir_10_impl|safe}}
{% endif %}
{% endfor %}

## MA - Maintenance


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-1 System Maintenance Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A system maintenance policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the system maintenance policy and the
           associated system maintenance controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     system maintenance policy and procedures;
c.   Review and update the current system maintenance:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the system maintenance procedures implement the system maintenance policy and
     controls; and
e.   Develop, document, and implement remediation actions for violations of the maintenance
     policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-2 Controlled Maintenance

<blockquote>a.   Schedule, document, and review records of maintenance, repair, or replacement on system
     components in accordance with manufacturer or vendor specifications and/or organizational
     requirements;




b.    Approve and monitor all maintenance activities, whether performed on site or remotely and
      whether the system or system components are serviced on site or removed to another location;
c.    Require that [Assignment: organization-defined personnel or roles] explicitly approve the
      removal of the system or system components from organizational facilities for off-site
      maintenance, repair, or replacement;
d.    Sanitize equipment to remove all information from associated media prior to removal from
      organizational facilities for off-site maintenance, repair, or replacement;
e.    Check all potentially impacted security and privacy controls to verify that the controls are still
      functioning properly following maintenance, repair, or replacement actions; and
f.    Include [Assignment: organization-defined maintenance-related information] in
      organizational maintenance records.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_2_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-2(2) Automated Maintenance Activities

<blockquote>(a)   Employ automated mechanisms to schedule, conduct, and document maintenance, repair,
      and replacement actions for the system or system components; and
(b) Produce up-to date, accurate, and complete records of all maintenance, repair, and
    replacement actions requested, scheduled, in process, and completed.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_2_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-3 Maintenance Tools

<blockquote>a.    Approve, control, and monitor the use of system maintenance tools; and
b.    Review previously approved system maintenance tools [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-3(1) Inspect Tools

<blockquote>Inspect the maintenance tools carried into a facility by maintenance personnel for improper or
unauthorized modifications.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-3(2) Inspect Media

<blockquote>Check media containing diagnostic and test programs for malicious code before the media are
used in the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-3(3) Prevent Unauthorized Removal

<blockquote>Prevent the removal of maintenance equipment containing organizational information by:
(a)   Verifying that there is no organizational information contained on the equipment;
(b) Sanitizing or destroying the equipment;
(c)   Retaining the equipment within the facility; or
(d) Obtaining an exemption from [Assignment: organization-defined personnel or roles] explicitly
    authorizing removal of the equipment from the facility.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_3_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-3(4) Restricted Tool Use

<blockquote>Restrict the use of maintenance tools to authorized personnel only.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_3_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-4 Nonlocal Maintenance

<blockquote>a.    Approve and monitor nonlocal maintenance and diagnostic activities;
b.    Allow the use of nonlocal maintenance and diagnostic tools only as consistent with
      organizational policy and documented in the security plan for the system;
c.    Employ strong authenticators in the establishment of nonlocal maintenance and diagnostic
      sessions;
d.    Maintain records for nonlocal maintenance and diagnostic activities; and
e.    Terminate session and network connections when nonlocal maintenance is completed.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-4(1) Auditing and Review

<blockquote></blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_4_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-4(3) Comparable Security and Sanitization

<blockquote>(a)   Require that nonlocal maintenance and diagnostic services be performed from a system that
      implements a security capability comparable to the capability implemented on the system
      being serviced; or
(b) Remove the component to be serviced from the system prior to nonlocal maintenance or
    diagnostic services; sanitize the component (for organizational information) before removal
    from organizational facilities; and after the service is performed, inspect and sanitize the
    component (for potentially malicious software) before reconnecting the component to the
    system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_4_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_4_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-4(4) Authentication and Separation of Maintenance Sessions

<blockquote>Protect nonlocal maintenance sessions by:
(a)   Employing [Assignment: organization-defined authenticators that are replay resistant]; and
(b) Separating the maintenance sessions from other network sessions with the system by either:
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_4_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_4_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-4(5) Approvals and Notifications

<blockquote>(a)   Require the approval of each nonlocal maintenance session by [Assignment: organization-defined personnel or roles]; and
(b) Notify [Assignment: organization-defined personnel or roles] of the date and time of planned
    nonlocal maintenance.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_4_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_4_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-4(6) Cryptographic Protection

<blockquote>Implement cryptographic mechanisms to protect the integrity and confidentiality of nonlocal
maintenance and diagnostic communications.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_4_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_4_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-4(7) Remote Disconnect Verification

<blockquote>Implement remote disconnect verification at the termination of nonlocal maintenance and
diagnostic sessions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_4_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-5 Maintenance Personnel

<blockquote>a.    Establish a process for maintenance personnel authorization and maintains a list of authorized
      maintenance organizations or personnel;
b.    Verify that non-escorted personnel performing maintenance on the system possess the
      required access authorizations; and
c.    Designate organizational personnel with required access authorizations and technical
      competence to supervise the maintenance activities of personnel who do not possess the
      required access authorizations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_5_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-5(1) Individuals Without Appropriate Access

<blockquote>formal access approvals are escorted and supervised during the performance of
maintenance and diagnostic activities on the system by approved organizational
personnel who are fully cleared, have appropriate access authorizations, and are
technically qualified;
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_5_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_5_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-5(2) Security Clearances for Classified Systems

<blockquote>Verify that personnel performing maintenance and diagnostic activities on a system processing,
storing, or transmitting classified information possess security clearances and formal access
approvals for at least the highest classification level and for all compartments of information on
the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_5_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_5_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-5(3) Citizenship Requirements for Classified Systems

<blockquote>Verify that personnel performing maintenance and diagnostic activities on a system processing,
storing, or transmitting classified information are U.S. citizens.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_5_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_5_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-5(4) Foreign Nationals

<blockquote>Verify that:
(a)   Foreign nationals with appropriate security clearances are used to conduct maintenance and
      diagnostic activities on classified systems only when the systems are jointly owned and
      operated by the United States and foreign allied governments, or owned and operated solely
      by foreign allied governments; and
(b) Approvals, consents, and detailed operational conditions regarding the use of foreign
    nationals to conduct maintenance and diagnostic activities on classified systems are fully
    documented within Memoranda of Agreements.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_5_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_5_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-5(5) Non-System Maintenance

<blockquote>Verify that non-escorted personnel performing maintenance activities not directly associated with
the system but in the physical proximity of the system, have required access authorizations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_5_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-6 Timely Maintenance

<blockquote>Obtain maintenance support and/or spare parts for [Assignment: organization-defined system components] within [Assignment: organization-defined time-period] of failure.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_6_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-6(1) Preventive Maintenance

<blockquote>Perform preventive maintenance on [Assignment: organization-defined system components] at
[Assignment: organization-defined time intervals].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_6_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_6_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-6(2) Predictive Maintenance

<blockquote>Perform predictive maintenance on [Assignment: organization-defined system components] at
[Assignment: organization-defined time intervals].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_6_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_6_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-6(3) Automated Support for Predictive Maintenance

<blockquote>Employ automated mechanisms to transfer predictive maintenance data to a computerized
maintenance management system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_6_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ma_6_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MA-6(4) Adequate Supply

<blockquote>Employ [Assignment: organization-defined security safeguards] to ensure an adequate supply of
[Assignment: organization-defined critical system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ma_6_4_impl|safe}}
{% endif %}
{% endfor %}

## MP - Media Protection


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-1 Media Protection Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A media protection policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the media protection policy and the
           associated media protection controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     media protection policy and procedures;
c.   Review and update the current media protection:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the media protection procedures implement the media protection policy and
     controls; and
e.   Develop, document, and implement remediation actions for violations of the media protection
     policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-2 Media Access

<blockquote>Restrict access to [Assignment: organization-defined types of digital and/or non-digital media] to [Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-3 Media Marking

<blockquote>a.    Mark system media indicating the distribution limitations, handling caveats, and applicable
      security markings (if any) of the information; and
b.    Exempt [Assignment: organization-defined types of system media] from marking if the media
      remain within [Assignment: organization-defined controlled areas].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-4 Media Storage

<blockquote>a.    Physically control and securely store [Assignment: organization-defined types of digital and/or non-digital media] within [Assignment: organization-defined controlled areas]; and
b.    Protect system media until the media are destroyed or sanitized using approved equipment,
      techniques, and procedures.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_4_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-4(2) Automated Restricted Access

<blockquote>Employ automated mechanisms to restrict access to media storage areas and to audit access
attempts and access granted.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_4_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-5 Media Transport

<blockquote>a.    Protect and control [Assignment: organization-defined types of system media] during transport
      outside of controlled areas using [Assignment: organization-defined security
safeguards]; b.    Maintain accountability for system media during transport outside of controlled areas;
c.    Document activities associated with the transport of system media; and
d.    Restrict the activities associated with the transport of system media to authorized personnel.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_5_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-5(3) Custodians

<blockquote>Employ an identified custodian during transport of system media outside of controlled areas.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_5_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-6 Media Sanitization

<blockquote>a.    Sanitize [Assignment: organization-defined system media] prior to disposal, release out of
      organizational control, or release for reuse using [Assignment: organization-defined
sanitization techniques and procedures]; and b.    Employ sanitization mechanisms with the strength and integrity commensurate with the
      security category or classification of the information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_6_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-6(1) Review, Approve, Track, Document, Verify

<blockquote>Review, approve, track, document, and verify media sanitization and disposal actions.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_6_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_6_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-6(2) Equipment Testing

<blockquote>Test sanitization equipment and procedures [Assignment: organization-defined frequency] to
verify that the intended sanitization is being achieved.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_6_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_6_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-6(3) Nondestructive Techniques

<blockquote>Apply nondestructive sanitization techniques to portable storage devices prior to connecting such
devices to the system under the following circumstances: [Assignment: organization-defined circumstances requiring sanitization of portable storage devices].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_6_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_6_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-6(7) Dual Authorization

<blockquote>Enforce dual authorization for the sanitization of [Assignment: organization-defined system media].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_6_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_6_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-6(8) Remote Purging or Wiping of Information

<blockquote>Provide the capability to purge or wipe information from [Assignment: organization-defined systems or system components] either remotely or under the following conditions: [Assignment: organization-defined conditions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_6_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_6_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-6(9) Destruction of Personally Identifiable Information

<blockquote>Facilitate the destruction of personally identifiable information by:
(a)   De-identifying the personally identifiable information;
(b) Proactively reviewing media to actively find personally identifiable information and removing
    such information; and
(c)   Reviewing media as it is being archived or disposed to find and remove personally identifiable
      information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_6_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-7 Media Use

<blockquote>a.    [Selection: Restrict; Prohibit] the use of [Assignment: organization-defined types of system media] on [Assignment: organization-defined systems or system components] using
      [Assignment: organization-defined security safeguards]; and
b.    Prohibit the use of portable storage devices in organizational systems when such devices have
      no identifiable owner.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_7_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-7(2) Prohibit Use of Sanitization-Resistant Media

<blockquote>Prohibit the use of sanitization-resistant media in organizational systems.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_7_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-8 Media Downgrading

<blockquote>a.    Establish [Assignment: organization-defined system media downgrading process] that
      includes employing downgrading mechanisms with strength and integrity commensurate
with
      the security category or classification of the information;
b.    Verify that the system media downgrading process is commensurate with the security
      category and/or classification level of the information to be removed and
the access
      authorizations of the potential recipients of the downgraded information;
c.    Identify [Assignment: organization-defined system media requiring downgrading]; and
d.    Downgrade the identified system media using the established process.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_8_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-8(1) Documentation of Process

<blockquote>Document system media downgrading actions.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_8_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_8_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-8(2) Equipment Testing

<blockquote>Test downgrading equipment and procedures [Assignment: organization-defined frequency] to
verify that intended downgrading actions are being achieved.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_8_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_8_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-8(3) Controlled Unclassified Information

<blockquote>Downgrade system media containing [Assignment: organization-defined Controlled Unclassified Information (CUI)] prior to public release.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_8_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_mp_8_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### MP-8(4) Classified Information

<blockquote>Downgrade system media containing classified information prior to release to individuals without
required access authorizations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_mp_8_4_impl|safe}}
{% endif %}
{% endfor %}

## PA - Privacy Authorization


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pa_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PA-1 Privacy Authorization Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A privacy authorization policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the privacy authorization policy and the
           associated privacy authorization controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     privacy authorization policy and procedures;
c.   Review and update the current privacy authorization:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the privacy authorization procedures implement the privacy authorization policy
     and controls; and
e.   Develop, document, and implement remediation actions for violations of the privacy
     authorization policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pa_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pa_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PA-2 Authority to Collect

<blockquote>Determine and document the legal authority that permits the collection, use, maintenance,
and sharing of personally identifiable information, either generally or in support of a specific
program or system need.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pa_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pa_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PA-3 Purpose Specification

<blockquote>Identify and document the purpose(s) for which personally identifiable information is
collected, used, maintained, and shared in its privacy notices.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pa_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pa_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PA-3(1) Usage Restrictions of Personally Identifiable Information

<blockquote>Restrict the use of personally identifiable information to only the authorized purpose(s) consistent
with applicable laws or regulations and/or in public notices.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pa_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pa_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PA-3(2) Automation

<blockquote>Employ automated mechanisms to support records management of authorizing policies and
procedures for personally identifiable information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pa_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pa_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PA-4 Information Sharing with External Parties

<blockquote>a.   Develop, document, and disseminate guidelines to [Assignment: organization-defined personnel or roles] for the sharing of personally identifiable information externally, only for
     the authorized purposes identified in the Privacy Act and/or described in its notices, or for a
     purpose that is compatible with those purposes;
b.   Evaluate proposed new instances of sharing personally identifiable information with external
     parties to assess whether:
     1.    The sharing is authorized; and
     2.    Additional or new public notice is required;
c.   Enter into information sharing agreements with external parties that specifically:
     1.    Describe the personally identifiable information covered;
     2.    Enumerate the purpose(s) for which the personally identifiable information may be used;
           and
     3.    Include security requirements consistent with the information being shared; and
d.   Monitor and audit the authorized sharing of personally identifiable information with external
     parties.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pa_4_impl|safe}}
{% endif %}
{% endfor %}

## PE - Physical and Environmental Protection


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-1 Physical and Environmental Protection Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A physical and environmental protection policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives,
regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the physical and environmental
protection
           policy and the associated physical and environmental protection controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     physical and environmental protection policy and procedures;
c.   Review and update the current physical and environmental protection:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the physical and environmental protection procedures implement the physical and
     environmental protection policy and controls; and
e.   Develop, document, and implement remediation actions for violations of the physical and
     environmental protection policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-2 Physical Access Authorizations

<blockquote>a.   Develop, approve, and maintain a list of individuals with authorized access to the facility
     where the system resides;
b.   Issue authorization credentials for facility access;




c.    Review the access list detailing authorized facility access by individuals [Assignment: organization-defined frequency]; and
d.    Remove individuals from the facility access list when access is no longer required.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_2_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-2(1) Access by Position and Role

<blockquote>Authorize physical access to the facility where the system resides based on position or role.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_2_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_2_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-2(2) Two Forms of Identification

<blockquote>Require two forms of identification from [Assignment: organization-defined list of acceptable forms of identification] for visitor access to the facility where the system resides.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_2_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_2_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-2(3) Restrict Unescorted Access

<blockquote>Restrict unescorted access to the facility where the system resides to personnel with [Selection (one or more): security clearances for all information contained within the system; formal access authorizations for all information contained within the system; need for access to all information contained within the system; &lt;1&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_2_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-3 Physical Access Control

<blockquote>a.    Enforce physical access authorizations at [Assignment: organization-defined entry and exit points to the facility where the system resides] by;
      1.   Verifying individual access authorizations before granting access to
the facility; and
      2.   Controlling ingress and egress to the facility using [Selection (one
or more): &lt;2&gt;; guards]; b.    Maintain physical access audit logs for [Assignment: organization-defined entry/exit points];
c.    Provide [Assignment: organization-defined security safeguards] to control access to areas
      within the facility designated as publicly accessible;
d.    Escort visitors and monitor visitor activity [Assignment: organization-defined circumstances requiring visitor escorts and monitoring];



e.    Secure keys, combinations, and other physical access devices;
f.    Inventory [Assignment: organization-defined physical access devices] every [Assignment: organization-defined frequency]; and
g.    Change combinations and keys [Assignment: organization-defined frequency] and/or when
      keys are lost, combinations are compromised, or individuals are transferred
or terminated.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-3(1) System Access

<blockquote>Enforce physical access authorizations to the system in addition to the physical access controls
for the facility at [Assignment: organization-defined physical spaces containing one or more components of the system].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-3(2) Facility and System Boundaries

<blockquote>Perform security checks [Assignment: organization-defined frequency] at the physical boundary of
the facility or system for exfiltration of information or removal of system components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-3(3) Continuous Guards

<blockquote>Employ guards to control [Assignment: organization-defined physical access points] to the facility
where the system resides 24 hours per day, 7 days per week.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_3_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-3(4) Lockable Casings

<blockquote>Use lockable physical casings to protect [Assignment: organization-defined system components]
from unauthorized physical access.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_3_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_3_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-3(5) Tamper Protection

<blockquote>Employ [Assignment: organization-defined security safeguards] to [Selection (one or more): detect; prevent] physical tampering or alteration of [Assignment: organization-defined hardware components] within the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_3_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_3_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-3(7) Physical Barriers

<blockquote>Limit access using physical barriers.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_3_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-4 Access Control for Transmission

<blockquote>Control physical access to [Assignment: organization-defined system distribution and transmission lines] within organizational facilities using [Assignment: organization-defined security safeguards].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-5 Access Control for Output Devices

<blockquote>Control physical access to output from [Assignment: organization-defined output devices]
to prevent unauthorized individuals from obtaining the output.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_5_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-5(1) Access to Output by Authorized Individuals

<blockquote>Verify that only authorized individuals receive output from output devices.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_5_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_5_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-5(2) Access to Output by Individual Identity

<blockquote>Link individual identity to receipt of output from output devices.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_5_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_5_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-5(3) Marking Output Devices

<blockquote>Mark [Assignment: organization-defined system output devices] indicating the appropriate security
marking of the information permitted to be output from the device.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_5_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-6 Monitoring Physical Access

<blockquote>a.    Monitor physical access to the facility where the system resides to detect and respond to
      physical security incidents;
b.    Review physical access logs [Assignment: organization-defined frequency] and upon
      occurrence of [Assignment: organization-defined events or potential indications of events];
      and
c.    Coordinate results of reviews and investigations with the organizational incident response
      capability.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_6_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-6(1) Intrusion Alarms and Surveillance Equipment

<blockquote>Monitor physical access to the facility where the system resides using physical intrusion alarms
and surveillance equipment.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_6_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_6_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-6(2) Automated Intrusion Recognition and Responses

<blockquote>Employ automated mechanisms to recognize [Assignment: organization-defined classes or types of intrusions] and initiate [Assignment: organization-defined response actions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_6_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_6_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-6(3) Video Surveillance

<blockquote>Employ video surveillance of [Assignment: organization-defined operational areas] and retain
video recordings for [Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_6_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_6_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-6(4) Monitoring Physical Access to Systems

<blockquote>Monitor physical access to the system in addition to the physical access monitoring of the facility
at [Assignment: organization-defined physical spaces containing one or more components of the system].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_6_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-8 Visitor Access Records

<blockquote>a.    Maintain visitor access records to the facility where the system resides for [Assignment: organization-defined time-period]; and
b.    Review visitor access records [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_8_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-8(1) Automated Records Maintenance and Review

<blockquote>Employ automated mechanisms to facilitate the maintenance and review of visitor access records.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_8_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-9 Power Equipment and Cabling

<blockquote>Protect power equipment and power cabling for the system from damage and destruction.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_9_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-9(1) Redundant Cabling

<blockquote>Employ redundant power cabling paths that are physically separated by [Assignment: organization-defined distance].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_9_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_9_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-9(2) Automatic Voltage Controls

<blockquote>Employ automatic voltage controls for [Assignment: organization-defined critical system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_9_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-10 Emergency Shutoff

<blockquote>a.    Provide the capability of shutting off power to the system or individual system components in
      emergency situations;
b.    Place emergency shutoff switches or devices in [Assignment: organization-defined location by system or system component] to facilitate safe and easy access for personnel; and
c.    Protect emergency power shutoff capability from unauthorized activation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-11 Emergency Power

<blockquote>Provide a short-term uninterruptible power supply to facilitate [Selection (one or more): an orderly shutdown of the system; transition of the system to long-term alternate power] in the
event of a primary power source loss.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_11_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-11(1) Long-Term Alternate Power Supply — Minimal Operational Capability

<blockquote>Provide a long-term alternate power supply for the system that can maintain minimally required
operational capability in the event of an extended loss of the primary power source.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_11_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_11_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-11(2) Long-Term Alternate Power Supply — Self-Contained

<blockquote>Provide a long-term alternate power supply for the system that is:
(a)   Self-contained;
(b) Not reliant on external power generation; and




(c)   Capable of maintaining [Selection: minimally required operational capability; full operational capability] in the event of an extended loss of the primary power source.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_11_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-12 Emergency Lighting

<blockquote>Employ and maintain automatic emergency lighting for the system that activates in the
event of a power outage or disruption and that covers emergency exits and evacuation routes
within the facility.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_12_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-12(1) Essential Missions and Business Functions

<blockquote>Provide emergency lighting for all areas within the facility supporting essential missions and
business functions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_12_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-13 Fire Protection

<blockquote>Employ and maintain fire suppression and detection devices/systems for the system that
are supported by an independent energy source.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_13_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-13(1) Detection Devices and Systems

<blockquote>Employ fire detection devices/systems for the system that activate automatically and notify
[Assignment: organization-defined personnel or roles] and [Assignment: organization-defined emergency responders] in the event of a fire.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_13_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_13_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-13(2) Automatic Suppression Devices and Systems

<blockquote>(a)   Employ fire suppression devices/systems for the system that provide automatic notification of
      any activation to [Assignment: organization-defined personnel or roles]
and [Assignment: organization-defined emergency responders]; and (b) Employ an automatic fire suppression capability for the system when the facility is not staffed
    on a continuous basis.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_13_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_13_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-13(4) Inspections

<blockquote>Verify that the facility undergoes [Assignment: organization-defined frequency] fire protection
inspections by authorized and qualified inspectors and resolves identified deficiencies within
[Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_13_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-14 Temperature and Humidity Controls

<blockquote>a.    Maintain temperature and humidity levels within the facility where the system resides at
      [Assignment: organization-defined acceptable levels]; and
b.    Monitor temperature and humidity levels [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_14_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-14(1) Automatic Controls

<blockquote>Employs automatic temperature and humidity controls in the facility to prevent fluctuations
potentially harmful to the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_14_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_14_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-14(2) Monitoring With Alarms and Notifications

<blockquote>Employ temperature and humidity monitoring that provides an alarm or notification of changes
potentially harmful to personnel or equipment to [Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_14_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-15 Water Damage Protection

<blockquote>Protect the system from damage resulting from water leakage by providing master shutoff
or isolation valves that are accessible, working properly, and known to key personnel.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_15_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-15(1) Automation Support

<blockquote>Employ automated mechanisms to detect the presence of water near the system and alert
[Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_15_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-16 Delivery and Removal

<blockquote>      Authorize, monitor, and control [Assignment: organization-defined types
of system components] entering and exiting the facility and maintain records of those items.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_17_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-17 Alternate Work Site

<blockquote>a.    Determine and document the [Assignment: organization-defined alternate work sites] allowed
      for use by employees;
b.    Employ [Assignment: organization-defined security and privacy controls] at alternate work
      sites;
c.    Assess the effectiveness of security and privacy controls at alternate work sites; and
d.    Provide a means for employees to communicate with information security and privacy
      personnel in case of security or privacy incidents or problems.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_17_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_18_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-18 Location of System Components

<blockquote>       Position system components within the facility to minimize potential damage from

[Assignment: organization-defined physical and environmental hazards] and to minimize the
opportunity for unauthorized access.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_18_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_18_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-18(1) Facility Site

<blockquote>(a)   Plan the location or site of the facility where the system resides considering physical and
      environmental hazards; and
(b) For existing facilities, consider the physical and environmental hazards in the organizational
    risk management strategy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_18_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_19_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-19 Information Leakage

<blockquote>Protect the system from information leakage due to electromagnetic signals emanations.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_19_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_19_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-19(1) National Emissions and Tempest Policies and Procedures

<blockquote>Protect system components, associated data communications, and networks in accordance with
national Emissions Security policies and procedures based on the security category or
classification of the information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_19_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_20_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-20 Asset Monitoring and Tracking

<blockquote>Employ [Assignment: organization-defined asset location technologies] to track and
monitor the location and movement of [Assignment: organization-defined assets] within
[Assignment: organization-defined controlled areas].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_20_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_21_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-21 Electromagnetic Pulse Protection

<blockquote>Employ [Assignment: organization-defined security safeguards] against electromagnetic
pulse damage for [Assignment: organization-defined systems and system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_21_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pe_22_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PE-22 Component Marking

<blockquote>Mark [Assignment: organization-defined system hardware components] indicating the
impact or classification level of the information permitted to be processed, stored, or transmitted
by the hardware component.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pe_22_impl|safe}}
{% endif %}
{% endfor %}

## PL - Planning


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-1 Planning Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    Security and privacy planning policies that:
           (a) Address purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Are consistent with applicable laws, Executive Orders, directives,
regulations,
               policies, standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the security and privacy
planning policies
           and the associated security and privacy planning controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     security and privacy planning policies and procedures;
c.   Review and update the current security and privacy planning:
     1.    Policies [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the security and privacy planning procedures implement the security and privacy
     planning policies and controls; and
e.   Develop, document, and implement remediation actions for violations of the planning policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-2 Security and Privacy Plans

<blockquote>a.   Develop security and privacy plans for the system that:
     1.    Are consistent with the organization’s enterprise architecture;
     2.    Explicitly define the authorization boundary for the system;




      3.   Describe the operational context of the system in terms of missions and business
           processes;
      4.   Provide the security categorization of the system including supporting rationale;
      5.   Describe the operational environment for the system and relationships with or
           connections to other systems;
      6.   Provide an overview of the security and privacy requirements for the system;
      7.   Identify any relevant overlays, if applicable;
      8.   Describe the security and privacy controls in place or planned for meeting those
           requirements including a rationale for the tailoring decisions; and
      9.   Are reviewed and approved by the authorizing official or designated representative prior
           to plan implementation;
b.    Distribute copies of the security and privacy plans and communicate subsequent changes to
      the plans to [Assignment: organization-defined personnel or roles];
c.    Review the security and privacy plans [Assignment: organization-defined frequency];
d.    Update the security and privacy plans to address changes to the system and environment of
      operation or problems identified during plan implementation or security and privacy control
      assessments; and
e.    Protect the security and privacy plans from unauthorized disclosure and modification.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_2_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-2(3) Plan and Coordinate With Other Organizational Entities

<blockquote>Plan and coordinate security- and privacy-related activities affecting the system with [Assignment: organization-defined individuals or groups] before conducting such activities to reduce the impact
on other organizational entities.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_2_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-4 Rules of Behavior

<blockquote>a.    Establish and provide to individuals requiring access to the system, the rules that describe
      their responsibilities and expected behavior for information and system
usage, security, and
      privacy;
b.    Receive a documented acknowledgment from such individuals, indicating that they have read,
      understand, and agree to abide by the rules of behavior, before authorizing
access to
      information and the system;
c.    Review and update the rules of behavior [Assignment: organization-defined frequency]; and
d.    Require individuals who have signed a previous version of the rules of behavior to read and
      re-sign [Selection (one or more): &lt;2&gt;; when the rules are revised or updated.]
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-4(1) Social Media and Networking Restrictions

<blockquote>Include in the rules of behavior, explicit restrictions on the use of social media and networking
sites and posting organizational information on public websites.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-7 Concept of Operations

<blockquote>a.   Develop a Concept of Operations (CONOPS) for the system describing how the organization
     intends to operate the system from the perspective of information security and privacy; and
b.   Review and update the CONOPS [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-8 Security and Privacy Architectures

<blockquote>a.   Develop security and privacy architectures for the system that:
     1.    Describe the philosophy, requirements, and approach to be taken for
protecting the
           confidentiality, integrity, and availability of organizational information;
     2.    Describe the philosophy, requirements, and approach to be taken for
processing
           personally identifiable information;
     3.    Describe how the security and privacy architectures are integrated
into and support the
           enterprise architecture; and
     4.    Describe any security- and privacy-related assumptions about, and dependencies
on,
           external services;
b.   Review and update the security and privacy architectures [Assignment: organization-defined frequency] to reflect updates in the enterprise architecture; and
c.   Reflect planned security and privacy architecture changes in the security and privacy plans,
     the Concept of Operations (CONOPS), and organizational procurements and acquisitions.
                     This control addresses actions taken by organizations in
the design and
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_8_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-8(1) Defense-In-Depth

<blockquote>Design the security and privacy architectures for the system using a defense-in-depth approach
that:
(a)   Allocates [Assignment: organization-defined security and privacy safeguards] to
      [Assignment: organization-defined locations and architectural layers]; and
(b) Ensures that the allocated security and privacy safeguards operate in a coordinated and
    mutually reinforcing manner.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_8_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_8_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-8(2) Supplier Diversity

<blockquote>Require that [Assignment: organization-defined security and privacy safeguards] allocated to
[Assignment: organization-defined locations and architectural layers] are obtained from different
suppliers.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_8_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-9 Central Management

<blockquote>Centrally manage [Assignment: organization-defined security and privacy controls and related processes].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-10 Baseline Selection

<blockquote>Select a control baseline for the system.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pl_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PL-11 Baseline Tailoring

<blockquote>Tailor the selected control baseline by applying specified tailoring actions.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pl_11_impl|safe}}
{% endif %}
{% endfor %}

## PM - Program Management


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-1 Information Security Program Plan

<blockquote>a.   Develop and disseminate an organization-wide information security program plan that:
     1.    Provides an overview of the requirements for the security program and
a description of
           the security program management controls and common controls in place
or planned for
           meeting those requirements;
     2.    Includes the identification and assignment of roles, responsibilities,
management
           commitment, coordination among organizational entities, and compliance;
     3.    Reflects the coordination among organizational entities responsible
for information
           security; and
     4.    Is approved by a senior official with responsibility and accountability
for the risk being
           incurred to organizational operations (including mission, functions,
image, and
           reputation), organizational assets, individuals, other organizations,
and the Nation; b.   Review the organization-wide information security program plan [Assignment: organization-defined frequency];
c.   Update the information security program plan to address organizational changes and problems
     identified during plan implementation or control assessments; and
d.   Protect the information security program plan from unauthorized disclosure and modification.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-2 Inforamtion Security Program Roles

<blockquote>a.   Appoint a Senior Agency Information Security Officer with the mission and resources to
     coordinate, develop, implement, and maintain an organization-wide information security
     program;
b.   Appoint a Senior Accountable Official for Risk Management to align information security
     management proceeses with strategic, operational, and budgetary planning procceses; and
c.   Appoint a Risk Executive (function) to view and analyze risk from an organization-wide
     perspective and ensure management of risk is consistent across the organization.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-3 Information Security and Privacy Resources

<blockquote>a.   Include the resources needed to implement the information security and privacy programs in
     capital planning and investment requests and document all exceptions to this
requirement; b.   Prepare documentation required for addressing information security and privacy programs in
     capital planning and investment requests in accordance with applicable laws,
Executive
     Orders, directives, policies, regulations, standards; and
c.   Make available for expenditure, the planned information security and privacy resources.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-4 Plan of Action and Milestones Process family have been

<blockquote>a.   Implement a process to ensure that plans of action and milestones for the security and privacy
     programs and associated organizational systems:
     1.    Are developed and maintained;
     2.    Document the remedial information security and privacy actions to adequately respond to
           risk to organizational operations and assets, individuals, other organizations, and the
           Nation; and
     3.    Are reported in accordance with established reporting requirements.




b.   Review plans of action and milestones for consistency with the organizational risk
     management strategy and organization-wide priorities for risk response actions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-5 System Inventory

<blockquote>Develop and maintain an inventory of organizational systems.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-6 Measures of Performance federal laws, Executive

<blockquote>Develop, monitor, and report on the results of information security and privacy measures
of performance.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-7 Enterprise Architecture Orders, directives,

<blockquote>Develop an enterprise architecture with consideration for information security, privacy,
and the resulting risk to organizational operations and assets, individuals, other organizations, and
the Nation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-8 Critical Infrastructure Plan

<blockquote>Address information security and privacy issues in the development, documentation, and
updating of a critical infrastructure and key resources protection plan.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-9 Risk Management Strategy

<blockquote>a.   Develops a comprehensive strategy to manage:
     1.    Security risk to organizational operations and assets, individuals,
other organizations, and
           the Nation associated with the operation and use of organizational
systems;
     2.    Privacy risk to individuals resulting from the collection, sharing,
storing, transmitting,
           use, and disposal of personally identifiable information; and
     3.    Supply chain risks associated with the development, acquisition, maintenance,
and
           disposal of systems, system components, and system services;
b.   Implement the risk management strategy consistently across the organization; and
c.   Review and update the risk management strategy [Assignment: organization-defined frequency] or as required, to address organizational changes.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-10 Authorization Process

<blockquote>a.   Manage the security and privacy state of organizational systems and the environments in
     which those systems operate through authorization processes;
b.   Designate individuals to fulfill specific roles and responsibilities within the organizational risk
     management process; and
c.   Integrate the authorization processes into an organization-wide risk management program.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-11 Mission and Business Process Definition FIPS 200 impact levels

<blockquote>a.   Define organizational mission and business processes with consideration for information
     security and privacy and the resulting risk to organizational operations,
organizational assets,
     individuals, other organizations, and the Nation; and
b.   Determine information protection and personally identifiable information processing needs
     arising from the defined mission and business processes; and
c.   Review and revise the mission and business processes [Assignment: organization-defined frequency], until achievable protection and personally identifiable information processing
     needs are obtained.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-12 Insider Threat Program

<blockquote>Implement an insider threat program that includes a cross-discipline insider threat incident
handling team.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-13 Security and Privacy Workforce control baselines in

<blockquote>Establish a security and privacy workforce development and improvement program.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-14 Testing, Training, and Monitoring Appendix D. Tailoring

<blockquote>a.   Implement a process for ensuring that organizational plans for conducting security and
     privacy testing, training, and monitoring activities associated with organizational systems:
     1.    Are developed and maintained; and
     2.    Continue to be executed in a timely manner;
b.   Review testing, training, and monitoring plans for consistency with the organizational risk
     management strategy and organization-wide priorities for risk response actions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-15 Contacts with Groups and Associations

<blockquote>Establish and institutionalize contact with selected groups and associations within the
security and privacy communities:
a.   To facilitate ongoing security and privacy education and training for organizational personnel;
b.   To maintain currency with recommended security and privacy practices, techniques, and
     technologies; and
c.   To share current security- and privacy-related information including threats, vulnerabilities,
     and incidents.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-16 Threat Awareness Program

<blockquote>Implement a threat awareness program that includes a cross-organization information-
sharing capability.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_16_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-16(1) Automated Means for Sharing Threat Intelligence

<blockquote>Utilize automated means to maximize the effectiveness of sharing threat intelligence information.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_16_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_17_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-17 Protecting CUI on External Systems on the programmatic,

<blockquote>a.    Establish policy and procedures to ensure that the requirements for the protection of
      Controlled Unclassified Information processed, stored or transmitted on external systems, are
      implemented in accordance with applicable laws, Executive Orders, directives, policies,
      regulations, and standards.
b.    Update the policy and procedures [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_17_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_18_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-18 Privacy Program Plan

<blockquote>a.    Develop and disseminate an organization-wide privacy program plan that provides an
      overview of the agency’s privacy program, and:



     1.   Includes a description of the structure of the privacy program and the resources dedicated
          to the privacy program;
     2.   Provides an overview of the requirements for the privacy program and a description of
          the privacy program management controls and common controls in place or planned for
          meeting those requirements;
     3.   Includes the role of the Senior Agency Official for Privacy and the identification and
          assignment of roles of other privacy officials and staff and their responsibilities;
     4.   Describes management commitment, compliance, and the strategic goals and objectives
          of the privacy program;
     5.   Reflects coordination among organizational entities responsible for the different aspects
          of privacy; and
     6.   Is approved by a senior official with responsibility and accountability for the privacy risk
          being incurred to organizational operations (including mission, functions, image, and
          reputation), organizational assets, individuals, other organizations, and the Nation; and
b.   Update the plan to address changes in federal privacy laws and policy and organizational
     changes and problems identified during plan implementation or privacy control assessments.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_18_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_19_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-19 Privacy Program Roles independent of any

<blockquote>Appoint a Senior Agency Official for Privacy with the authority, mission, accountability,
and resources to coordinate, develop, and implement, applicable privacy requirements and manage
privacy risks through the organization-wide privacy program.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_19_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_20_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-20 System of Records Notice system and essential

<blockquote>a.   Publish System of Records Notices in the Federal Register, subject to required oversight
     processes, for systems containing personally identifiable information; and
b.   Keep System of Records Notices current.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_20_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_21_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-21 Dissemination of Privacy Program Information

<blockquote>a.   Ensure that the public has access to information about organizational privacy activities and
     can communicate with its Senior Agency Official for Privacy;
b.   Ensure that organizational privacy practices are publicly available through organizational
     websites or otherwise; and
c.   Employ publicly facing email addresses and/or phone lines to enable the public to provide
     feedback and/or direct questions to privacy offices regarding privacy practices.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_21_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_22_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-22 Accounting of Disclosures

<blockquote>a.    Develop and maintain an accounting of disclosures of personally identifiable information held
      in each system of records under its control, including:
      1.   Date, nature, and purpose of each disclosure of a record; and
      2.   Name and address of the person or organization to which the disclosure
was made; b.    Retain the accounting of disclosures for the life of the record or five years after the disclosure
      is made, whichever is longer; and
c.    Make the accounting of disclosures available to the person named in the record upon request.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_22_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_23_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-23 Data Quality Management document the controls

<blockquote>Issue guidelines ensuring and maximizing the quality, utility, objectivity, integrity, impact
determination, and de-identification of personally identifiable information across the information
life cycle.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_23_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_23_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-23(1) AUTOMATION in their information

<blockquote>Issue technical guidelines and documentation to support automated evaluation of data quality
across the information life cycle.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_23_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_23_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-23(2) Data Tagging

<blockquote>Issue data modeling guidelines to support tagging of personally identifiable information.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_23_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_23_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-23(3) UPDATING PERSONALLY IDENTIFIABLE INFORMATION plans, together with the

<blockquote>When managing personally identifiable information, develop procedures and incorporate
mechanisms to identify and record the method under which the information is updated, and the
frequency that such updates occur.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_23_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_24_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-24 Data Management Board security and privacy

<blockquote>a.    Establish a written charter for a Data Management Board;
b.    Establish the Data Management Board consisting of [Assignment: organization-defined roles]
      with the following responsibilities:
      1.   Develop and implement guidelines supporting data modeling, quality,
integrity, and de-
           identification needs of personally identifiable information across
the information life
           cycle;
      2.   Review and approve applications to release data outside of the organization,
archiving the
           applications and the released data, and performing post-release monitoring
to ensure that
           the assumptions made as part of the data release continue to be valid;
c.    Include requirements for personnel interaction with the Data Management Board in security
      and privacy awareness and/or role-based training.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_24_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_25_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-25 Data Integrity Board

<blockquote>      Establish a Data Integrity Board to oversee organizational Computer Matching

Agreements.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_25_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_25_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-25(1) PUBLISH AGREEMENTS ON WEBSITE totality of security and

<blockquote>Publish Computer Matching Agreements on the public website of the organization.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_25_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_26_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-26 Minimization of PII Used in Testing Training, and Research are employed by the

<blockquote>a.    Develop and implement policies and procedures that address the use of personally identifiable
      information for internal testing, training, and research;
b.    Take measures to limit or minimize the amount of personally identifiable information used for
      internal testing, training, and research purposes; and
c.    Authorize the use of personally identifiable information when such information is required for
      internal testing, training, and research.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_26_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_27_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-27 Individual Access Control

<blockquote>a.   Publish:
     1.    Policies governing how individuals may request access to records maintained in a Privacy
           Act system of records; and
     2.    Access procedures in System of Records Notices; and
b.   Ensure that the published policies and access procedures are consistent with Privacy Act
     requirements and Office of Management and Budget policies and guidance for the proper
     processing of Privacy Act requests.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_27_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_28_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-28 Complaint Management

<blockquote>Implement a process for receiving and responding to complaints, concerns, or questions
from individuals about the organizational privacy practices that includes:
a.   Mechanisms that are easy to use and readily accessible by the public;
b.   All information necessary for successfully filing complaints; and
c.   Tracking mechanisms to ensure all complaints received are reviewed and appropriately
     addressed in a timely manner.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_28_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_29_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-29 Inventory of PII

<blockquote>a.    Establish, maintain, and update [Assignment: organization-defined frequency] an inventory of
      all programs and systems that create, collect, use, process, store, maintain,
disseminate,
      disclose, or dispose of personally identifiable information;
b.    Provide updates of the personally identifiable information inventory to the Chief Information
      Officer, Senior Agency Official for Privacy, and Senior Agency Information
Security Officer
      [Assignment: organization-defined frequency];
c.    Use the personally identifiable information inventory to support the establishment of
      information security and privacy requirements for all new or modified systems
containing
      personally identifiable information;
d.    Review the personally identifiable information inventory [Assignment: organization-defined frequency];
e.    Ensure to the extent practicable, that personally identifiable information is accurate, relevant,
      timely, and complete; and
f.    Reduce personally identifiable information to the minimum necessary for the proper
      performance of authorized organizational functions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_29_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_29_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-29(1) Automation Support

<blockquote>Employ automated mechanisms to determine if personally identifiable information is maintained in
electronic form.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_29_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_30_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-30 Privacy Reporting

<blockquote>Develop, disseminate, and update privacy reports to:
a.    The Office of Management and Budget, Congress, and other oversight bodies to demonstrate
      accountability with statutory and regulatory privacy program mandates; and
b.    [Assignment: organization-defined officials] and other personnel with responsibility for
      monitoring privacy program progress and compliance.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_30_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_31_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-31 Supply Chain Risk Management Plan

<blockquote>a.   Develop a plan for managing supply chain risks associated with the development, acquisition,
     maintenance, and disposal of systems, system components, and system services;
b.   Implement the supply chain risk management plan consistently across the organization; and
c.   Review and update the supply chain risk management plan [Assignment: organization-defined frequency] or as required, to address organizational changes.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_31_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_pm_32_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PM-32 Risk Framing

<blockquote>a.   Identify assumptions affecting risk assessments, risk response, and risk monitoring;
b.   Identify constraints affecting risk assessments, risk response, and risk monitoring;
c.   Identify the organizational risk tolerance; and
d.   Identify priorities and trade-offs considered by the organization for managing risk.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_pm_32_impl|safe}}
{% endif %}
{% endfor %}

## PS - Personnel Security


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-1 Personnel Security Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A personnel security policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the personnel security policy and the
           associated personnel security controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     personnel security policy and procedures;
c.   Review and update the current personnel security:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the personnel security procedures implement the personnel security policy and
     controls; and
e.   Develop, document, and implement remediation actions for violations of the personnel
     security policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-2 Position Risk Designation

<blockquote>a.   Assign a risk designation to all organizational positions;
b.   Establish screening criteria for individuals filling those positions; and





c.    Review and update position risk designations [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-3 Personnel Screening

<blockquote>a.    Screen individuals prior to authorizing access to the system; and
b.    Rescreen individuals in accordance with [Assignment: organization-defined conditions requiring rescreening and, where rescreening is so indicated, the frequency of rescreening].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-3(1) Classified Information

<blockquote>Verify that individuals accessing a system processing, storing, or transmitting classified
information are cleared and indoctrinated to the highest classification level of the information to
which they have access on the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-3(2) Formal Indoctrination

<blockquote>Verify that individuals accessing a system processing, storing, or transmitting types of classified
information which require formal indoctrination, are formally indoctrinated for all the relevant types
of information to which they have access on the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-3(3) Information With Special Protection Measures

<blockquote>Verify that individuals accessing a system processing, storing, or transmitting information
requiring special protection:
(a)   Have valid access authorizations that are demonstrated by assigned official government
      duties; and
(b) Satisfy [Assignment: organization-defined additional personnel screening criteria].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_3_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-3(4) Citizenship Requirements

<blockquote>Verify that individuals accessing a system processing, storing, or transmitting [Assignment: organization-defined information types] meet [Assignment: organization-defined citizenship requirements].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_3_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-4 Personnel Termination

<blockquote>Upon termination of individual employment:
a.    Disable system access within [Assignment: organization-defined time-period];
b.    Terminate or revoke any authenticators and credentials associated with the individual;
c.    Conduct exit interviews that include a discussion of [Assignment: organization-defined information security topics];
d.    Retrieve all security-related organizational system-related property;
e.    Retain access to organizational information and systems formerly controlled by terminated
      individual; and
f.    Notify [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-4(1) Post-Employment Requirements

<blockquote>(a)   Notify terminated individuals of applicable, legally binding post-employment requirements for
      the protection of organizational information; and
(b) Require terminated individuals to sign an acknowledgment of post-employment requirements
    as part of the organizational termination process.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_4_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-4(2) Automated Notification

<blockquote>Employ automated mechanisms to notify [Assignment: organization-defined personnel or roles]
upon termination of an individual.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_4_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-5 Personnel Transfer

<blockquote>a.    Review and confirm ongoing operational need for current logical and physical access
      authorizations to systems and facilities when individuals are reassigned
or transferred to other
      positions within the organization;
b.    Initiate [Assignment: organization-defined transfer or reassignment actions] within
      [Assignment: organization-defined time-period following the formal transfer
action]; c.    Modify access authorization as needed to correspond with any changes in operational need
      due to reassignment or transfer; and
d.    Notify [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-6 Access Agreements

<blockquote>a.    Develop and document access agreements for organizational systems;
b.    Review and update the access agreements [Assignment: organization-defined frequency]; and
c.    Verify that individuals requiring access to organizational information and systems:
      1.   Sign appropriate access agreements prior to being granted access; and
      2.   Re-sign access agreements to maintain access to organizational systems
when access
           agreements have been updated or [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_6_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-6(2) Classified Information Requiring Special Protection

<blockquote>Verify that access to classified information requiring special protection is granted only to
individuals who:




(a)   Have a valid access authorization that is demonstrated by assigned official government
      duties;
(b) Satisfy associated personnel security criteria; and
(c)   Have read, understood, and signed a nondisclosure agreement.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_6_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_6_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-6(3) Post-Employment Requirements

<blockquote>(a)   Notify individuals of applicable, legally binding post-employment requirements for protection
      of organizational information; and
(b) Require individuals to sign an acknowledgment of these requirements, if applicable, as part of
    granting initial access to covered information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_6_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-7 External Personnel Security

<blockquote>a.    Establish personnel security requirements including security roles and responsibilities for
      external providers;
b.    Require external providers to comply with personnel security policies and procedures
      established by the organization;
c.    Document personnel security requirements;
d.    Require external providers to notify [Assignment: organization-defined personnel or roles] of
      any personnel transfers or terminations of external personnel who possess organizational
      credentials and/or badges, or who have system privileges within [Assignment: organization-defined time-period]; and
e.    Monitor provider compliance.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ps_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### PS-8 Personnel Sanctions

<blockquote>a.   Employ a formal sanctions process for individuals failing to comply with established
     information security policies and procedures; and
b.   Notify [Assignment: organization-defined personnel or roles] within [Assignment: organization-defined time-period] when a formal employee sanctions process is initiated,
     identifying the individual sanctioned and the reason for the sanction.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ps_8_impl|safe}}
{% endif %}
{% endfor %}

## RA - Risk Assessment


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-1 Risk Assessment Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A risk assessment policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the risk assessment policy and the
           associated risk assessment controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     risk assessment policy and procedures;
c.   Review and update the current risk assessment:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the risk assessment procedures implement the risk assessment policy and controls;
     and
e.   Develop, document, and implement remediation actions for violations of the risk assessment
     policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-2 Security Categorization

<blockquote>a.   Categorize the system and information it processes, stores, and transmits;
b.   Document the security categorization results including supporting rationale, in the security
     plan for the system; and




c.    Verify that the authorizing official or authorizing official designated representative reviews
      and approves the security categorization decision.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_2_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-2(1) Second-Level Categorization

<blockquote>Conduct a second-level categorization of organizational systems to obtain additional granularity
on system impact levels.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_2_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-3 Risk Assessment

<blockquote>a.    Conduct a risk assessment, including the likelihood and magnitude of harm, from:
      1.   The unauthorized access, use, disclosure, disruption, modification, or destruction of the
           system, the information it processes, stores, or transmits, and any related information; and
      2.   Privacy-related problems for individuals arising from the intentional processing of
           personally identifiable information;
b.    Integrate risk assessment results and risk management decsions from the organization and
      missions/business process perspectives with system-level risk assessments;
c.    Document risk assessment results in [Selection: security and privacy plans; risk assessment report; &lt;1&gt;];




d.    Review risk assessment results [Assignment: organization-defined frequency];
e.    Disseminate risk assessment results to [Assignment: organization-defined personnel or roles];
      and
f.    Update the risk assessment [Assignment: organization-defined frequency] or when there are
      significant changes to the system, its environment of operation, or other conditions that may
      impact the security or privacy state of the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-3(1) Supply Chain Risk Assessment

<blockquote>(a)   Assess supply chain risks associated with [Assignment: organization-defined systems, system components, and system services]; and
(b) Update the supply chain risk assessment [Assignment: organization-defined frequency], when
    there are significant changes to the relevant supply chain, or when changes
to the system,
    environments of operation, or other conditions may necessitate a change in
the supply chain.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-5 Vulnerability Scanning

<blockquote>a.    Scan for vulnerabilities in the system and hosted applications [Assignment: organization-defined frequency and/or randomly in accordance with organization-defined process] and
      when new vulnerabilities potentially affecting the system are identified
and reported; b.    Employ vulnerability scanning tools and techniques that facilitate interoperability among
      tools and automate parts of the vulnerability management process by using
standards for:
      1.   Enumerating platforms, software flaws, and improper configurations;
      2.   Formatting checklists and test procedures; and
      3.   Measuring vulnerability impact;
c.    Analyze vulnerability scan reports and results from control assessments;
d.    Remediate legitimate vulnerabilities [Assignment: organization-defined response times] in
      accordance with an organizational assessment of risk;
e.    Share information obtained from the vulnerability scanning process and control assessments
      with [Assignment: organization-defined personnel or roles] to help eliminate
similar
      vulnerabilities in other systems; and
f.    Employ vulnerability scanning tools that include the capability to readily update the
      vulnerabilities to be scanned.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_5_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-5(2) Update by Frequency, Prior to New Scan, or When Identified

<blockquote>Update the system vulnerabilities to be scanned [Selection (one or more): &lt;1&gt;; prior to a new scan; when new vulnerabilities are identified and reported].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_5_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_5_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-5(3) Breadth and Depth of Coverage

<blockquote>Employ vulnerability scanning procedures that can identify the breadth and depth of coverage.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_5_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_5_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-5(4) Discoverable Information

<blockquote>Determine unintended discoverable information about the system and take [Assignment: organization-defined corrective actions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_5_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_5_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-5(5) Privileged Access

<blockquote>Implements privileged access authorization to [Assignment: organization-identified system components] for [Assignment: organization-defined vulnerability scanning activities].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_5_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_5_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-5(6) Automated Trend Analyses

<blockquote>Employ automated mechanisms to compare the results of vulnerability scans over time to
determine trends in system vulnerabilities.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_5_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_5_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-5(8) Review Historic Audit Logs

<blockquote>Review historic audit logs to determine if a vulnerability identified in the system has been
previously exploited.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_5_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_5_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-5(10) Correlate Scanning Information

<blockquote>Correlate the output from vulnerability scanning tools to determine the presence of multi-
vulnerability and multi-hop attack vectors.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_5_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-6 Technical Surveillance Countermeasures Survey

<blockquote>Employ a technical surveillance countermeasures survey at [Assignment: organization-defined locations] [Selection (one or more): &lt;2&gt;; &lt;3&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-7 Risk Response

<blockquote>Respond to findings from security and privacy assessments, monitoring, and audits.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-8 Privacy Impact Assessments

<blockquote>Conduct privacy impact assessments for systems, programs, or other activities that pose a
privacy risk before:
a.     Developing or procuring information technology that collects, maintains, or disseminates
       information that is in an identifiable form; and
b.     Initiating a new collection of information that:
       1.   Will be collected, maintained, or disseminated using information technology; and
       2.   Includes information in an identifiable form permitting the physical or online contacting
            of a specific individual, if identical questions have been posed to, or identical reporting
            requirements imposed on, ten or more persons, other than agencies, instrumentalities, or
            employees of the Federal Government.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_ra_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### RA-9 Criticality Analysis

<blockquote>       Identify critical system components and functions by performing a criticality analysis for

[Assignment: organization-defined systems, system components, or system services] at
[Assignment: organization-defined decision points in the system development life cycle].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_ra_9_impl|safe}}
{% endif %}
{% endfor %}

## SA - System and Services Acquisition


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-1 System and Services Acquisition Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A system and services acquisition policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives, regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the system and services acquisition policy
           and the associated system and services acquisition controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     system and services acquisition policy and procedures;
c.   Review and update the current system and services acquisition:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the system and services acquisition procedures implement the system and services
     acquisition policy and controls; and
e.   Develop, document, and implement remediation actions for violations of the system and
     services acquisition policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-2 Allocation of Resources

<blockquote>a.   Determine information security and privacy requirements for the system or system service in
     mission and business process planning;





b.    Determine, document, and allocate the resources required to protect the system or system
      service as part of the organizational capital planning and investment control process; and
c.    Establish a discrete line item for information security and privacy in organizational
      programming and budgeting documentation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-3 System Development Life Cycle

<blockquote>a.    Manage the system using [Assignment: organization-defined system development life cycle]
      that incorporates information security and privacy considerations;
b.    Define and document information security and privacy roles and responsibilities throughout
      the system development life cycle;
c.    Identify individuals having information security and privacy roles and responsibilities; and
d.    Integrate the organizational information security and privacy risk management process into
      system development life cycle activities.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-3(1) Manage Development Environment

<blockquote>Protect system development, test, and integration environments commensurate with risk
throughout the system development life cycle for the system, system component, or system
service.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-3(2) Use of Live Data

<blockquote>(a)   Approve, document, and control the use of live data in development, test, and integration
      environments for the system, system component, or system service; and
(b) Ensure development, test, and integration environments for the system, system component,
    or system service are protected at the same impact or classification level as any live data
    used.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-3(3) Technology Refresh

<blockquote>Plan for and implement a technology refresh schedule to support the system throughout the
system development life cycle.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-4 Acquisition Process

<blockquote>Include the following requirements, descriptions, and criteria, explicitly or by reference, in
the acquisition contract for the system, system component, or system service:
a.    Security and privacy functional requirements;
b.    Strength of mechanism requirements;
c.    Security and privacy assurance requirements;
d.    Security and privacy documentation requirements;
e.    Requirements for protecting security and privacy documentation;
f.    Description of the system development environment and environment in which the system is
      intended to operate;
g.    Allocation of responsibility or identification of parties responsible for information security,
      privacy, and supply chain risk management; and
h.    Acceptance criteria.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-4(1) Functional Properties of Controls

<blockquote>Require the developer of the system, system component, or system service to provide a
description of the functional properties of the controls to be implemented.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_4_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-4(2) Design and Implementation Information for Controls

<blockquote>Require the developer of the system, system component, or system service to provide design and
implementation information for the selected controls that includes: [Selection (one or more): security-relevant external system interfaces; high-level design; low-level design; source code or hardware schematics; &lt;1&gt;]
at [Assignment: organization-defined level of detail].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_4_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_4_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-4(3) Development Methods, Techniques, and Practices

<blockquote>Require the developer of the system, system component, or system service to demonstrate the use
of a system development life cycle process that includes [Assignment: organization-defined systems engineering methods; [Selection (one or more): systems security engineering methods; privacy engineering methods]; software development methods; testing, evaluation, assessment,
verification, and validation methods; and quality control processes].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_4_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_4_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-4(5) System, Component, and Service Configurations

<blockquote>Require the developer of the system, system component, or system service to:
(d) Deliver the system, component, or service with [Assignment: organization-defined security configurations] implemented; and
(e)   Use the configurations as the default for any subsequent system, component, or service
      reinstallation or upgrade.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_4_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_4_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-4(6) Use of Information Assurance Products

<blockquote>(a)   Employ only government off-the-shelf or commercial off-the-shelf information assurance and
      information assurance-enabled information technology products that compose
an NSA-
      approved solution to protect classified information when the networks used
to transmit the
      information are at a lower classification level than the information being
transmitted; and (b) Ensure that these products have been evaluated and/or validated by NSA or in accordance
    with NSA-approved procedures.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_4_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_4_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-4(7) Niap-Approved Protection Profiles

<blockquote>(a)   Limit the use of commercially provided information assurance and information assurance-
      enabled information technology products to those products that have been
successfully
      evaluated against a National Information Assurance partnership (NIAP)-approved
Protection
      Profile for a specific technology type, if such a profile exists; and
(b) Require, if no NIAP-approved Protection Profile exists for a specific technology type but a
    commercially provided information technology product relies on cryptographic
functionality
    to enforce its security policy, that the cryptographic module is FIPS-validated
or NSA-
    approved.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_4_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_4_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-4(8) Continuous Monitoring Plan for Controls

<blockquote>Require the developer of the system, system component, or system service to produce a plan for
continuous monitoring of security and privacy control effectiveness that contains the following:
[Assignment: organization-defined level of detail].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_4_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_4_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-4(9) Functions, Ports, Protocols, and Services in Use

<blockquote>Require the developer of the system, system component, or system service to identify the
functions, ports, protocols, and services intended for organizational use.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_4_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_4_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-4(10) Use of Approved Piv Products

<blockquote>Employ only information technology products on the FIPS 201-approved products list for Personal
Identity Verification (PIV) capability implemented within organizational systems.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_4_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-5 System Documentation

<blockquote>a.    Obtain administrator documentation for the system, system component, or system service that
      describes:
      1.   Secure configuration, installation, and operation of the system, component,
or service;
      2.   Effective use and maintenance of security and privacy functions and
mechanisms; and
      3.   Known vulnerabilities regarding configuration and use of administrative
or privileged
           functions;
b.    Obtain user documentation for the system, system component, or system service that
      describes:
      1.   User-accessible security and privacy functions and mechanisms and how
to effectively
           use those functions and mechanisms;
      2.   Methods for user interaction, which enables individuals to use the
system, component, or
           service in a more secure manner and protect individual privacy; and
      3.   User responsibilities in maintaining the security of the system, component,
or service and
           privacy of individuals;
c.    Document attempts to obtain system, system component, or system service documentation
      when such documentation is either unavailable or nonexistent and takes [Assignment:
organization-defined actions] in response; d.    Protect documentation as required, in accordance with the organizational risk management
      strategy; and
e.    Distribute documentation to [Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-8 Security and Privacy Engineering Principles

<blockquote>Apply [Assignment: organization-defined systems security engineering principles] in the
specification, design, development, implementation, and modification of the system and system
components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-9 External System Services

<blockquote>a.    Require that providers of external system services comply with organizational security and
      privacy requirements and employ [Assignment: organization-defined security
and privacy controls]; b.    Define and document organizational oversight and user roles and responsibilities with regard
      to external system services; and
c.    Employ [Assignment: organization-defined processes, methods, and techniques] to monitor
      security and privacy control compliance by external service providers on
an ongoing basis.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_9_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-9(1) Risk Assessments and Organizational Approvals

<blockquote>(a)   Conduct an organizational assessment of risk prior to the acquisition or outsourcing of
      information security services; and
(b) Verify that the acquisition or outsourcing of dedicated information security services is
    approved by [Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_9_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_9_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-9(2) Identification of Functions, Ports, Protocols, and Services

<blockquote>Require providers of [Assignment: organization-defined external system services] to identify the
functions, ports, protocols, and other services required for the use of such services.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_9_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_9_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-9(3) Establish and Maintain Trust Relationship With Providers

<blockquote>Establish, document, and maintain trust relationships with external service providers based on
[Assignment: organization-defined security and privacy requirements, properties, factors, or conditions defining acceptable trust relationships].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_9_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_9_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-9(4) Consistent Interests of Consumers and Providers

<blockquote>Take [Assignment: organization-defined actions] to verify that the interests of [Assignment: organization-defined external service providers] are consistent with and reflect organizational
interests.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_9_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_9_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-9(5) Processing, Storage, and Service Location

<blockquote>Restrict the location of [Selection (one or more): information processing; information or data; system services] to [Assignment: organization-defined locations] based on [Assignment: organization-defined requirements or conditions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_9_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_9_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-9(6) Organization-Controlled Cryptographic Keys

<blockquote>Maintain exclusive control of cryptographic keys.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_9_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_9_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-9(7) Organization-Controlled Integrity Checking

<blockquote>Provide the capability to check the integrity of organizational information while it resides in the
external system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_9_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-10 Developer Configuration Management

<blockquote>Require the developer of the system, system component, or system service to:
a.    Perform configuration management during system, component, or service [Selection (one or more): design; development; implementation; operation; disposal];
b.    Document, manage, and control the integrity of changes to [Assignment: organization-defined configuration items under configuration management];
c.    Implement only organization-approved changes to the system, component, or service;
d.    Document approved changes to the system, component, or service and the potential security
      and privacy impacts of such changes; and
e.    Track security flaws and flaw resolution within the system, component, or service and report
      findings to [Assignment: organization-defined personnel].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_10_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-10(1) Software and Firmware Integrity Verification

<blockquote>Require the developer of the system, system component, or system service to enable integrity
verification of software and firmware components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_10_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_10_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-10(2) Alternative Configuration Management Processes

<blockquote>Provide an alternate configuration management process using organizational personnel in the
absence of a dedicated developer configuration management team.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_10_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_10_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-10(3) Hardware Integrity Verification

<blockquote>Require the developer of the system, system component, or system service to enable integrity
verification of hardware components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_10_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_10_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-10(4) Trusted Generation

<blockquote>Require the developer of the system, system component, or system service to employ tools for
comparing newly generated versions of security-relevant hardware descriptions, source code, and
object code with previous versions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_10_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_10_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-10(5) Mapping Integrity for Version Control

<blockquote>Require the developer of the system, system component, or system service to maintain the
integrity of the mapping between the master build data (hardware drawings and software/firmware
code) describing the current version of security-relevant hardware, software, and firmware and the
on-site master copy of the data for the current version.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_10_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_10_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-10(6) Trusted Distribution

<blockquote>Require the developer of the system, system component, or system service to execute procedures
for ensuring that security-relevant hardware, software, and firmware updates distributed to the
organization are exactly as specified by the master copies.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_10_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-11 Developer Testing and Evaluation

<blockquote>Require the developer of the system, system component, or system service, at all post-
design phases of the system development life cycle, to:
a.    Create and implement a security and privacy assessment plan;
b.    Perform [Selection (one or more): unit; integration; system; regression] testing/evaluation
      [Assignment: organization-defined frequency] at [Assignment: organization-defined depth and coverage];
c.    Produce evidence of the execution of the assessment plan and the results of the testing and
      evaluation;
d.    Implement a verifiable flaw remediation process; and
e.    Correct flaws identified during testing and evaluation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_11_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-11(1) Static Code Analysis

<blockquote>Require the developer of the system, system component, or system service to employ static code
analysis tools to identify common flaws and document the results of the analysis.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_11_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_11_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-11(2) Threat Modeling and Vulnerability Analyses

<blockquote>Require the developer of the system, system component, or system service to perform threat
modeling and vulnerability analyses at [Assignment: organization-defined breadth and depth]
during development and during the subsequent testing and evaluation of the system, component,
or service that:
(a)   Uses [Assignment: organization-defined information concerning impact, environment of operations, known or assumed threats, and acceptable risk levels];
(b) Employs [Assignment: organization-defined tools and methods]; and
(c)   Produces evidence that meets [Assignment: organization-defined acceptance criteria].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_11_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_11_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-11(3) Independent Verification of Assessment Plans and Evidence

<blockquote>(a)   Require an independent agent satisfying [Assignment: organization-defined independence criteria] to verify the correct implementation of the developer security and privacy assessment
      plans and the evidence produced during testing and evaluation; and
(b) Verify that the independent agent is provided with sufficient information to complete the
    verification process or granted the authority to obtain such information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_11_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_11_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-11(4) Manual Code Reviews

<blockquote>Require the developer of the system, system component, or system service to perform a manual
code review of [Assignment: organization-defined specific code] using [Assignment: organization-defined processes, procedures, and/or techniques].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_11_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_11_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-11(5) Penetration Testing

<blockquote>Require the developer of the system, system component, or system service to perform penetration
testing at [Assignment: organization-defined breadth and depth] and with [Assignment: organization-defined constraints].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_11_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_11_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-11(6) Attack Surface Reviews

<blockquote>Require the developer of the system, system component, or system service to perform attack
surface reviews.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_11_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_11_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-11(7) Verify Scope of Testing and Evaluation

<blockquote>Require the developer of the system, system component, or system service to verify that the scope
of testing and evaluation provides complete coverage of required security and privacy controls at
[Assignment: organization-defined depth of testing and evaluation].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_11_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_11_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-11(8) Dynamic Code Analysis

<blockquote>Require the developer of the system, system component, or system service to employ dynamic
code analysis tools to identify common flaws and document the results of the analysis.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_11_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12 Supply Chain Risk Management

<blockquote>a.    Employ [Assignment: organization-defined supply chain safeguards] to protect against supply
      chain risks to the system, system component, or system service and to limit
the harm or
      consequences from supply chain-related events; and
b.    Document the selected and implemented supply chain safeguards in [Selection: security and privacy plans; supply chain risk management plan; &lt;2&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(1) Acquisition Strategies, Tools, and Methods

<blockquote>Employ [Assignment: organization-defined acquisition strategies, contract tools, and procurement methods] to protect against, identify, and mitigate supply chain risks.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(2) Supplier Reviews

<blockquote>Review the supply chain-related risks associated with suppliers or contractors and the system,
system component, or system service they provide [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(5) Limitation of Harm

<blockquote>Employ [Assignment: organization-defined safeguards] to limit harm from potential adversaries
identifying and targeting the organizational supply chain.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(7) Assessments Prior to Selection, Acceptance, and Update

<blockquote>Assess the system, system component, or system service prior to selection, acceptance,
modification, or update.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(8) Use of All-Source Intelligence

<blockquote>Use all-source intelligence to assist in the analysis of supply chain risk.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(9) Operations Security

<blockquote>Employ [Assignment: organization-defined Operations Security (OPSEC) safeguards] to protect
supply chain-related information for the system, system component, or system service.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(10) Validate As Genuine and Not Altered

<blockquote>Employ [Assignment: organization-defined security safeguards] to validate that the system or
system component received is genuine and has not been altered.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(11) Penetration Testing and Analysis

<blockquote>Employ [Selection (one or more): organizational analysis, independent third-party analysis, organizational penetration testing, independent third-party penetration testing] of [Assignment: organization-defined supply chain elements, processes, and actors] associated with the system,
system component, or system service.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(12) Notification Agreements

<blockquote>Establish agreements and procedures with entities involved in the supply chain for the system,
system component, or system service for the [Selection (one or more): notification of supply chain compromises; results of assessments or audits; &lt;1&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(14) Identity and Traceability

<blockquote>Establish and maintain unique identification of [Assignment: organization-defined supply chain elements, processes, and personnel] associated with the [Assignment: organization-defined system, critical system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(15) Processes to Address Weaknesses or Deficiencies

<blockquote>Establish a process or processes to address weaknesses or deficiencies in supply chain elements
in coordination with [Assignment: organization-defined supply chain personnel].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_12_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-12(16) Provenance

<blockquote>Document, monitor, and maintain valid provenance of [Assignment: organization-defined systems, system components, and associated data].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_12_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-15 Development Process, Standards, and Tools

<blockquote>a.    Require the developer of the system, system component, or system service to follow a
      documented development process that:
      1.    Explicitly addresses security requirements;
      2.    Identifies the standards and tools used in the development process;
      3.    Documents the specific tool options and tool configurations used in
the development
            process; and
      4.    Documents, manages, and ensures the integrity of changes to the process
and/or tools
            used in development; and
b.    Review the development process, standards, tools, tool options, and tool configurations
      [Assignment: organization-defined frequency] to determine if the process,
standards, tools,
      tool options and tool configurations selected and employed can satisfy [Assignment:
organization-defined security and privacy requirements].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_15_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-15(1) Quality Metrics

<blockquote>Require the developer of the system, system component, or system service to:
(a)   Define quality metrics at the beginning of the development process; and
(b) Provide evidence of meeting the quality metrics [Selection (one or more): &lt;1&gt;; &lt;2&gt;; upon delivery].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_15_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_15_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-15(2) Security Tracking Tools

<blockquote>Require the developer of the system, system component, or system service to select and employ a
security tracking tool for use during the development process.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_15_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_15_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-15(3) Criticality Analysis

<blockquote>Require the developer of the system, system component, or system service to perform a criticality
analysis at [Assignment: organization-defined breadth/depth] and at [Assignment: organization-defined decision points in the system development life cycle].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_15_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_15_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-15(5) Attack Surface Reduction

<blockquote>Require the developer of the system, system component, or system service to reduce attack
surfaces to [Assignment: organization-defined thresholds].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_15_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_15_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-15(6) Continuous Improvement

<blockquote>Require the developer of the system, system component, or system service to implement an
explicit process to continuously improve the development process.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_15_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_15_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-15(7) Automated Vulnerability Analysis

<blockquote>Require the developer of the system, system component, or system service to:
(a)   Perform an automated vulnerability analysis using [Assignment: organization-defined tools];
(b) Determine the exploitation potential for discovered vulnerabilities;
(c)   Determine potential risk mitigations for delivered vulnerabilities; and
(d) Deliver the outputs of the tools and results of the analysis to [Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_15_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_15_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-15(8) Reuse of Threat and Vulnerability Information

<blockquote>Require the developer of the system, system component, or system service to use threat modeling
and vulnerability analyses from similar systems, components, or services to inform the current
development process.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_15_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_15_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-15(10) Incident Response Plan

<blockquote>Require the developer of the system, system component, or system service to provide, implement,
and test an incident response plan.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_15_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_15_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-15(11) Archive System or Component

<blockquote>Require the developer of the system or system component to archive the system or component to
be released or delivered together with the corresponding evidence supporting the final security
and privacy review.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_15_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-16 Developer-Provided Training

<blockquote>Require the developer of the system, system component, or system service to provide
[Assignment: organization-defined training] on the correct use and operation of the implemented
security and privacy functions, controls, and/or mechanisms.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_17_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-17 Developer Security Architecture and Design

<blockquote>Require the developer of the system, system component, or system service to produce a
design specification and security architecture that:
a.    Is consistent with and supportive of the organization’s security architecture which is
      established within and is an integrated part of the organization’s enterprise architecture;





b.    Accurately and completely describes the required security functionality, and the allocation of
      security controls among physical and logical components; and
c.    Expresses how individual security functions, mechanisms, and services work together to
      provide required security capabilities and a unified approach to protection.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_17_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_17_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-17(1) Formal Policy Model

<blockquote>Require the developer of the system, system component, or system service to:
(a)   Produce, as an integral part of the development process, a formal policy model describing the
      [Assignment: organization-defined elements of organizational security policy] to be enforced;
      and
(b) Prove that the formal policy model is internally consistent and sufficient to enforce the
    defined elements of the organizational security policy when implemented.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_17_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_17_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-17(2) Security-Relevant Components

<blockquote>Require the developer of the system, system component, or system service to:
(a)   Define security-relevant hardware, software, and firmware; and
(b) Provide a rationale that the definition for security-relevant hardware, software, and firmware is
    complete.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_17_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_17_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-17(3) Formal Correspondence

<blockquote>Require the developer of the system, system component, or system service to:
(a)   Produce, as an integral part of the development process, a formal top-level specification that
      specifies the interfaces to security-relevant hardware, software, and firmware in terms of
      exceptions, error messages, and effects;
(b) Show via proof to the extent feasible with additional informal demonstration as necessary,
    that the formal top-level specification is consistent with the formal policy model;
(c)   Show via informal demonstration, that the formal top-level specification completely covers the
      interfaces to security-relevant hardware, software, and firmware;
(d) Show that the formal top-level specification is an accurate description of the implemented
    security-relevant hardware, software, and firmware; and




(e)   Describe the security-relevant hardware, software, and firmware mechanisms not addressed
      in the formal top-level specification but strictly internal to the security-relevant hardware,
      software, and firmware.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_17_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_17_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-17(4) Informal Correspondence

<blockquote>Require the developer of the system, system component, or system service to:
(a)   Produce, as an integral part of the development process, an informal descriptive top-level
      specification that specifies the interfaces to security-relevant hardware,
software, and
      firmware in terms of exceptions, error messages, and effects;
(b) Show via [Selection: informal demonstration, convincing argument with formal methods as feasible] that the descriptive top-level specification is consistent with the formal policy model;
(c)   Show via informal demonstration, that the descriptive top-level specification completely
      covers the interfaces to security-relevant hardware, software, and firmware;
(d) Show that the descriptive top-level specification is an accurate description of the interfaces to
    security-relevant hardware, software, and firmware; and
(e)   Describe the security-relevant hardware, software, and firmware mechanisms not addressed
      in the descriptive top-level specification but strictly internal to the
security-relevant hardware,
      software, and firmware.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_17_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_17_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-17(5) Conceptually Simple Design

<blockquote>Require the developer of the system, system component, or system service to:
(a)   Design and structure the security-relevant hardware, software, and firmware to use a
      complete, conceptually simple protection mechanism with precisely defined semantics; and
(b) Internally structure the security-relevant hardware, software, and firmware with specific regard
    for this mechanism.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_17_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_17_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-17(6) Structure for Testing

<blockquote>Require the developer of the system, system component, or system service to structure security-
relevant hardware, software, and firmware to facilitate testing.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_17_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_17_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-17(7) Structure for Least Privilege

<blockquote>Require the developer of the system, system component, or system service to structure security-
relevant hardware, software, and firmware to facilitate controlling access with least privilege.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_17_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_18_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-18 Tamper Resistance and Detection

<blockquote>Implement a tamper protection program for the system, system component, or system
service.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_18_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_18_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-18(1) Multiple Phases of System Development Life Cycle

<blockquote>Employ anti-tamper technologies, tools, and techniques during multiple phases in the system
development life cycle including design, development, integration, operations, and maintenance.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_18_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_18_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-18(2) Inspection of Systems or Components

<blockquote>Inspect [Assignment: organization-defined systems or system components] [Selection (one or more): at random; at &lt;2&gt;, upon &lt;3&gt;] to detect tampering.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_18_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_19_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-19 Component Authenticity

<blockquote>a.    Develop and implement anti-counterfeit policy and procedures that include the means to
      detect and prevent counterfeit components from entering the system; and
b.    Report counterfeit system components to [Selection (one or more): source of counterfeit component; &lt;1&gt;; &lt;2&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_19_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_19_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-19(1) Anti-Counterfeit Training

<blockquote>Train [Assignment: organization-defined personnel or roles] to detect counterfeit system
components (including hardware, software, and firmware).
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_19_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_19_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-19(2) Configuration Control for Component Service and Repair

<blockquote>Maintain configuration control over [Assignment: organization-defined system components]
awaiting service or repair and serviced or repaired components awaiting return to service.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_19_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_19_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-19(3) Component Disposal

<blockquote>Dispose of system components using [Assignment: organization-defined techniques and methods].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_19_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_19_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-19(4) Anti-Counterfeit Scanning

<blockquote>Scan for counterfeit system components [Assignment: organization-defined frequency].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_19_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_20_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-20 Customized Development of Critical Components

<blockquote>Re-implement or custom develops [Assignment: organization-defined critical system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_20_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_21_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-21 Developer Screening

<blockquote>Require that the developer of [Assignment: organization-defined system, system component, or system service]:





a.    Have appropriate access authorizations as determined by assigned [Assignment: organization-defined official government duties];
b.    Satisfy [Assignment: organization-defined additional personnel screening criteria]; and
c.    Provide information that the access authorizations and screening criteria specified in a. and b.
      are satisfied.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_21_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_22_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-22 Unsupported System Components

<blockquote>Replace system components when support for the components is no longer available from
the developer, vendor, or manufacturer.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_22_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sa_22_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SA-22(1) Alternative Sources for Continued Support

<blockquote>Provide [Selection (one or more): in-house support; &lt;1&gt;] for unsupported system components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sa_22_1_impl|safe}}
{% endif %}
{% endfor %}

## SC - System and Communications Protection


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-1 System and Communications Protection Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A system and communications protection policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives,
regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the system and communications
protection
           policy and the associated system and communications protection controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     system and communications protection policy and procedures;
c.   Review and update the current system and communications protection:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the system and communications protection procedures implement the system and
     communications protection policy and controls; and
e.   Develop, document, and implement remediation actions for violations of the system and
     communications protection policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-2 Application Partitioning

<blockquote>Separate user functionality, including user interface services, from system management
functionality.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_2_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-2(1) Interfaces for Non-Privileged Users

<blockquote>Prevent the presentation of system management functionality at an interface for non-privileged
users.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_2_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-3 Security Function Isolation

<blockquote>Isolate security functions from nonsecurity functions.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-3(1) Hardware Separation

<blockquote>Use hardware separation mechanisms to implement security function isolation.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_3_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-3(2) Access and Flow Control Functions

<blockquote>Isolate security functions enforcing access and information flow control from nonsecurity
functions and from other security functions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_3_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_3_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-3(3) Minimize Nonsecurity Functionality

<blockquote>Minimize the number of nonsecurity functions included within the isolation boundary containing
security functions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_3_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_3_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-3(4) Module Coupling and Cohesiveness

<blockquote>Implement security functions as largely independent modules that maximize internal cohesiveness
within modules and minimize coupling between modules.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_3_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_3_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-3(5) Layered Structures

<blockquote>Implement security functions as a layered structure minimizing interactions between layers of the
design and avoiding any dependence by lower layers on the functionality or correctness of higher
layers.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_3_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-4 Information in Shared System Resources

<blockquote>Prevent unauthorized and unintended information transfer via shared system resources.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_4_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-4(2) Multilevel or Periods Processing

<blockquote>Prevent unauthorized information transfer via shared resources in accordance with [Assignment: organization-defined procedures] when system processing explicitly switches between different
information classification levels or security categories.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_4_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-5 Denial of Service Protection

<blockquote>Protect against or limit the effects of the following types of denial of service events:
[Assignment: organization-defined types of denial of service events or references to sources for such information] by employing [Assignment: organization-defined security safeguards].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_5_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-5(1) Restrict Internal Users

<blockquote>Restrict the ability of individuals to launch [Assignment: organization-defined denial of service attacks] against other systems.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_5_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_5_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-5(2) Capacity, Bandwidth, and Redundancy

<blockquote>Manage capacity, bandwidth, or other redundancy to limit the effects of information flooding denial
of service attacks.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_5_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_5_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-5(3) Detection and Monitoring

<blockquote>(a)   Employ [Assignment: organization-defined monitoring tools] to detect indicators of denial of
      service attacks against the system; and
(b) Monitor [Assignment: organization-defined system resources] to determine if sufficient
    resources exist to prevent effective denial of service attacks.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_5_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-6 Resource Availability

<blockquote>Protect the availability of resources by allocating [Assignment: organization-defined resources] by [Selection (one or more); priority; quota; &lt;2&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7 Boundary Protection

<blockquote>a.    Monitor and control communications at the external boundary of the system and at key
      internal boundaries within the system;
b.    Implement subnetworks for publicly accessible system components that are [Selection: physically; logically] separated from internal organizational networks; and
c.    Connect to external networks or systems only through managed interfaces consisting of
      boundary protection devices arranged in accordance with an organizational
security and
      privacy architecture.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(3) Access Points

<blockquote>Limit the number of external network connections to the system.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(4) External Telecommunications Services

<blockquote>(a)   Implement a managed interface for each external telecommunication service;
(b) Establish a traffic flow policy for each managed interface;
(c)   Protect the confidentiality and integrity of the information being transmitted across each
      interface;
(d) Document each exception to the traffic flow policy with a supporting mission/business need
    and duration of that need; and
(e)   Review exceptions to the traffic flow policy [Assignment: organization-defined frequency] and
      removes exceptions that are no longer supported by an explicit mission/business need.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(5) Deny by Default — Allow by Exception

<blockquote>Deny network communications traffic by default and allow network communications traffic by
exception at managed interfaces.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(7) Prevent Split Tunneling for Remote Devices

<blockquote>Prevent a remote device from simultaneously establishing non-remote connections with the
system and communicating via some other connection to resources in external networks.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(8) Route Traffic to Authenticated Proxy Servers

<blockquote>Route [Assignment: organization-defined internal communications traffic] to [Assignment: organization-defined external networks] through authenticated proxy servers at managed
interfaces.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(9) Restrict Threatening Outgoing Communications Traffic

<blockquote>(a)   Detect and deny outgoing communications traffic posing a threat to external systems; and
(b) Audit the identity of internal users associated with denied communications.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(10) Prevent Exfiltration

<blockquote>(a)   Prevent the exfiltration of information; and
(b) Conduct exfiltration tests [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(11) Restrict Incoming Communications Traffic

<blockquote>Only allow incoming communications from [Assignment: organization-defined authorized sources]
to be routed to [Assignment: organization-defined authorized destinations].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(12) Host-Based Protection

<blockquote>Implement [Assignment: organization-defined host-based boundary protection mechanisms] at
[Assignment: organization-defined system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(13) Isolation of Security Tools, Mechanisms, and Support Components

<blockquote>Isolate [Assignment: organization-defined information security tools, mechanisms, and support components] from other internal system components by implementing physically separate
subnetworks with managed interfaces to other components of the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(14) Protects Against Unauthorized Physical Connections

<blockquote>Protect against unauthorized physical connections at [Assignment: organization-defined managed interfaces].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(15) Route Privileged Network Accesses

<blockquote>Route all networked, privileged accesses through a dedicated, managed interface for purposes of
access control and auditing.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(16) Prevent Discovery of Components and Devices

<blockquote>Prevent the discovery of specific system components that represent a managed interface.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_17_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(17) Automated Enforcement of Protocol Formats

<blockquote>Enforce adherence to protocol formats.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_17_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_18_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(18) Fail Secure

<blockquote>Prevent systems from entering unsecure states in the event of an operational failure of a boundary
protection device.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_18_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_19_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(19) Block Communication From Non-Organizationally Configured Hosts

<blockquote>Block inbound and outbound communications traffic between [Assignment: organization-defined communication clients] that are independently configured by end users and external service
providers.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_19_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_20_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(20) Dynamic Isolation and Segregation

<blockquote>Provide the capability to dynamically isolate or segregate [Assignment: organization-defined system components] from other system components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_20_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_21_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(21) Isolation of System Components

<blockquote>Employ boundary protection mechanisms to separate [Assignment: organization-defined system components] supporting [Assignment: organization-defined missions and/or business functions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_21_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_22_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(22) Separate Subnets for Connecting to Different Security Domains

<blockquote>Implement separate network addresses to connect to systems in different security domains.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_22_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_23_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(23) Disable Sender Feedback on Protocol Validation Failure

<blockquote>Disable feedback to senders on protocol format validation failure.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_23_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_7_24_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-7(24) Personally Identifiable Information

<blockquote>For systems that process, store, or transmit personally identifiable information:
(a)   Apply [Assignment: organization-defined processing rules] to data elements of personally
      identifiable information;
(b) Monitor for permitted processing at the external boundary of the system and at key internal
    boundaries within the system;
(c)   Document each processing exception; and
(d) Review and remove exceptions that are no longer supported.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_7_24_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-8 Transmission Confidentiality and Integrity

<blockquote>Protect the [Selection (one or more): confidentiality; integrity] of transmitted information.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_8_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-8(1) Cryptographic Protection

<blockquote>Implement cryptographic mechanisms to [Selection (one or more): prevent unauthorized disclosure of information; detect changes to information] during transmission.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_8_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_8_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-8(2) Pre- and Post-Transmission Handling

<blockquote>Maintain the [Selection (one or more): confidentiality; integrity] of information during preparation
for transmission and during reception.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_8_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_8_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-8(3) Cryptographic Protection for Message Externals

<blockquote>Implement cryptographic mechanisms to protect message externals unless otherwise protected by
[Assignment: organization-defined alternative physical safeguards].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_8_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_8_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-8(4) Conceal or Randomize Communications

<blockquote>Implement cryptographic mechanisms to conceal or randomize communication patterns unless
otherwise protected by [Assignment: organization-defined alternative physical safeguards].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_8_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-10 Network Disconnect

<blockquote>Terminate the network connection associated with a communications session at the end of
the session or after [Assignment: organization-defined time-period] of inactivity.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-11 Trusted Path

<blockquote>a.    Provide a [Selection: physically; logically] isolated trusted communications path for
      communications between the user and the trusted components of the system;
and b.    Permit users to invoke the trusted communications path for communications between the user
      and the following security functions of the system, including at a minimum,
authentication
      and re-authentication: [Assignment: organization-defined security functions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_11_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-11(1) Logical Isolation

<blockquote>(a)   Provide a trusted communications path that is irrefutably distinguishable from other
      communications paths; and
(b) Initiate the trusted communications path for communications between the following security
    functions of the system and the user [Assignment: organization-defined security functions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_11_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-12 Cryptographic Key Establishment and Management

<blockquote>Establish and manage cryptographic keys for required cryptography employed within the
system in accordance with [Assignment: organization-defined requirements for key generation, distribution, storage, access, and destruction].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_12_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-12(1) Availability

<blockquote>Maintain availability of information in the event of the loss of cryptographic keys by users.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_12_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_12_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-12(2) Symmetric Keys

<blockquote>Produce, control, and distribute symmetric cryptographic keys using [Selection: NIST FIPS-compliant; NSA-approved] key management technology and processes.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_12_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_12_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-12(3) Asymmetric Keys

<blockquote>Produce, control, and distribute asymmetric cryptographic keys using [Selection: NSA-approved key management technology and processes; approved DoD PKI Class 3 certificates; prepositioned keying material; approved DoD PKI Class 3 or Class 4 certificates and hardware security tokens that protect the user’s private key; certificates issued in accordance with organization-defined requirements].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_12_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-13 Cryptographic Protection

<blockquote>       Implement the following cryptographic uses and type of cryptography for each use:

[Assignment: organization-defined cryptographic uses and type of cryptography required for each use].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-15 Collaborative Computing Devices and Applications

<blockquote>a.    Prohibit remote activation of collaborative computing devices and applications with the
      following exceptions: [Assignment: organization-defined exceptions where
remote activation is to be allowed]; and b.    Provide an explicit indication of use to users physically present at the devices.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_15_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-15(1) Physical Disconnect

<blockquote>Provide physical disconnect of collaborative computing devices in a manner that supports ease of
use.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_15_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_15_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-15(3) Disabling and Removal in Secure Work Areas

<blockquote>Disable or remove collaborative computing devices and applications from [Assignment: organization-defined systems or system components] in [Assignment: organization-defined secure work areas].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_15_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_15_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-15(4) Explicitly Indicate Current Participants

<blockquote>Provide an explicit indication of current participants in [Assignment: organization-defined online meetings and teleconferences].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_15_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-16 Transmission of Security and Privacy Attributes

<blockquote>Associate [Assignment: organization-defined security and privacy attributes] with
information exchanged between systems and between system components.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_16_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-16(1) Integrity Validation

<blockquote>Validate the integrity of transmitted security and privacy attributes.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_16_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_17_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-17 Public Key Infrastructure Certificates

<blockquote>Issue public key certificates under an [Assignment: organization-defined certificate policy] or obtain public key certificates from an approved service provider.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_17_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_18_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-18 Mobile Code

<blockquote>a.    Define acceptable and unacceptable mobile code and mobile code technologies;
b.    Establish usage restrictions and implementation guidance for acceptable mobile code and
      mobile code technologies; and
c.    Authorize, monitor, and control the use of mobile code within the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_18_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_18_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-18(1) Identify Unacceptable Code and Take Corrective Actions

<blockquote>Identify [Assignment: organization-defined unacceptable mobile code] and take [Assignment: organization-defined corrective actions].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_18_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_18_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-18(2) Acquisition, Development, and Use

<blockquote>Verify that the acquisition, development, and use of mobile code to be deployed in the system
meets [Assignment: organization-defined mobile code requirements].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_18_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_18_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-18(3) Prevent Downloading and Execution

<blockquote>Prevent the download and execution of [Assignment: organization-defined unacceptable mobile code].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_18_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_18_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-18(4) Prevent Automatic Execution

<blockquote>Prevent the automatic execution of mobile code in [Assignment: organization-defined software applications] and enforce [Assignment: organization-defined actions] prior to executing the code.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_18_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_18_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-18(5) Allow Execution Only in Confined Environments

<blockquote>Allow execution of permitted mobile code only in confined virtual machine environments.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_18_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_19_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-19 Voice Over Internet Protocol

<blockquote>a.    Establish usage restrictions and implementation guidelines for Voice over Internet Protocol
      (VoIP) technologies; and
b.    Authorize, monitor, and control the use of VoIP technologies within the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_19_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_20_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-20 Secure Name/Address Resolution Service (Authoritative Source)

<blockquote>a.    Provide additional data origin authentication and integrity verification artifacts along with the
      authoritative name resolution data the system returns in response to external
name/address
      resolution queries; and
b.    Provide the means to indicate the security status of child zones and (if the child supports
      secure resolution services) to enable verification of a chain of trust among
parent and child
      domains, when operating as part of a distributed, hierarchical namespace.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_20_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_20_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-20(2) Data Origin and Integrity

<blockquote>Provide data origin and integrity protection artifacts for internal name/address resolution queries.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_20_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_21_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-21 Secure Name/Address Resolution Service (Recursive or Caching Resolver)

<blockquote>       Request and perform data origin authentication and data integrity verification on the

name/address resolution responses the system receives from authoritative sources.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_21_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_22_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-22 Architecture and Provisioning for Name/Address Resolution Service

<blockquote>Ensure the systems that collectively provide name/address resolution service for an
organization are fault-tolerant and implement internal and external role separation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_22_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_23_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-23 Session Authenticity

<blockquote>Protect the authenticity of communications sessions.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_23_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_23_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-23(1) Invalidate Session Identifiers at Logout

<blockquote>Invalidate session identifiers upon user logout or other session termination.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_23_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_23_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-23(3) Unique Session Identifiers With Randomization

<blockquote>Generate a unique session identifier for each session with [Assignment: organization-defined randomness requirements] and recognize only session identifiers that are system-generated.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_23_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_23_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-23(5) Allowed Certificate Authorities

<blockquote>Only allow the use of [Assignment: organization-defined certificate authorities] for verification of
the establishment of protected sessions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_23_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_24_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-24 Fail in Known State

<blockquote>Fail to a [Assignment: organization-defined known system state] for [Assignment: organization-defined types of system failures] preserving [Assignment: organization-defined system state information] in failure.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_24_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_25_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-25 Thin Nodes

<blockquote>Employ [Assignment: organization-defined system components] with minimal
functionality and information storage.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_25_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_26_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-26 Honeypots

<blockquote>Include components within organizational systems specifically designed to be the target of
malicious attacks for detecting, deflecting, and analyzing such attacks.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_26_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_27_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-27 Platform-Independent Applications

<blockquote>       Include within organizational systems: [Assignment: organization-defined platform-independent applications].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_27_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_28_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-28 Protection of Information at Rest

<blockquote>       Protect the [Selection (one or more): confidentiality; integrity] of [Assignment: organization-defined information] at rest.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_28_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_28_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-28(1) Cryptographic Protection

<blockquote>Implement cryptographic mechanisms to prevent unauthorized disclosure and modification of
[Assignment: organization-defined information] when at rest on [Assignment: organization-defined system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_28_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_28_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-28(2) Off-Line Storage

<blockquote>Remove the following information from online storage and store off-line in a secure location:
[Assignment: organization-defined information].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_28_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_29_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-29 Heterogeneity

<blockquote>Employ a diverse set of information technologies for [Assignment: organization-defined system components] in the implementation of the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_29_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_29_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-29(1) Virtualization Techniques

<blockquote>Employ virtualization techniques to support the deployment of a diversity of operating systems
and applications that are changed [Assignment: organization-defined frequency].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_29_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_30_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-30 Concealment and Misdirection

<blockquote>Employ [Assignment: organization-defined concealment and misdirection techniques] for
[Assignment: organization-defined systems] at [Assignment: organization-defined time-periods] to
confuse and mislead adversaries.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_30_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_30_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-30(2) Randomness

<blockquote>Employ [Assignment: organization-defined techniques] to introduce randomness into
organizational operations and assets.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_30_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_30_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-30(3) Change Processing and Storage Locations

<blockquote>Change the location of [Assignment: organization-defined processing and/or storage] [Selection: &lt;2&gt;; at random time intervals]].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_30_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_30_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-30(4) Misleading Information

<blockquote>Employ realistic, but misleading information in [Assignment: organization-defined system components] about its security state or posture.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_30_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_30_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-30(5) Concealment of System Components

<blockquote>Employ [Assignment: organization-defined techniques] to hide or conceal [Assignment: organization-defined system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_30_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_31_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-31 Covert Channel Analysis

<blockquote>a.    Perform a covert channel analysis to identify those aspects of communications within the
      system that are potential avenues for covert [Selection (one or more): storage; timing]
      channels; and
b.    Estimate the maximum bandwidth of those channels.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_31_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_31_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-31(1) Test Covert Channels for Exploitability

<blockquote>Test a subset of the identified covert channels to determine which channels are exploitable.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_31_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_31_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-31(2) Maximum Bandwidth

<blockquote>Reduce the maximum bandwidth for identified covert [Selection (one or more); storage; timing]
channels to [Assignment: organization-defined values].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_31_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_31_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-31(3) Measure Bandwidth in Operational Environments

<blockquote>Measure the bandwidth of [Assignment: organization-defined subset of identified covert channels]
in the operational environment of the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_31_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_32_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-32 System Partitioning

<blockquote>Partition the system into [Assignment: organization-defined system components] residing
in separate physical domains or environments based on [Assignment: organization-defined circumstances for physical separation of components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_32_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_34_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-34 Non-Modifiable Executable Programs

<blockquote>At [Assignment: organization-defined system components]:
 a.   Load and execute the operating environment from hardware-enforced, read-only media; and
 b.   Load and execute [Assignment: organization-defined applications] from hardware-enforced,
      read-only media.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_34_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_34_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-34(1) no Writable Storage

<blockquote>Employ [Assignment: organization-defined system components] with no writeable storage that is
persistent across component restart or power on/off.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_34_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_34_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-34(2) Integrity Protection and Read-Only Media

<blockquote>Protect the integrity of information prior to storage on read-only media and control the media after
such information has been recorded onto the media.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_34_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_34_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-34(3) Hardware-Based Protection

<blockquote>(a)   Employ hardware-based, write-protect for [Assignment: organization-defined system firmware components]; and
(b) Implement specific procedures for [Assignment: organization-defined authorized individuals]
    to manually disable hardware write-protect for firmware modifications and
re-enable the write-
    protect prior to returning to operational mode.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_34_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_35_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-35 Honeyclients

<blockquote>       Include system components that proactively seek to identify network-based malicious

code, malicious websites, or web-based malicious code.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_35_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_36_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-36 Distributed Processing and Storage

<blockquote>Distribute [Assignment: organization-defined processing and storage components] across
multiple physical locations.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_36_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_36_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-36(1) Polling Techniques

<blockquote>(a)   Employ polling techniques to identify potential faults, errors, or compromises to [Assignment: organization-defined distributed processing and storage components]; and
(b) Take [Assignment: organization-defined action] in response to identified faults, errors, or
    compromises.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_36_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_37_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-37 Out-of-Band Channels

<blockquote>Employ [Assignment: organization-defined out-of-band channels] for the physical
delivery or electronic transmission of [Assignment: organization-defined information, system components, or devices] to [Assignment: organization-defined individuals or systems].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_37_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_37_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-37(1) Ensure Delivery and Transmission

<blockquote>Employ [Assignment: organization-defined security safeguards] to ensure that only [Assignment: organization-defined individuals or systems] receive the [Assignment: organization-defined information, system components, or devices].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_37_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_38_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-38 Operations Security

<blockquote>Employ [Assignment: organization-defined operations security safeguards] to protect key
organizational information throughout the system development life cycle.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_38_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_39_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-39 Process Isolation

<blockquote>Maintain a separate execution domain for each executing process with the system.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_39_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_39_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-39(1) Hardware Separation

<blockquote>Implement hardware separation mechanisms to facilitate process separation.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_39_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_39_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-39(2) Thread Isolation

<blockquote>Maintain a separate execution domain for each thread in [Assignment: organization-defined multi-threaded processing].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_39_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_40_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-40 Wireless Link Protection

<blockquote>Protect external and internal [Assignment: organization-defined wireless links] from
[Assignment: organization-defined types of signal parameter attacks or references to sources for such attacks].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_40_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_40_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-40(1) Electromagnetic Interference

<blockquote>Implement cryptographic mechanisms that achieve [Assignment: organization-defined level of protection] against the effects of intentional electromagnetic interference.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_40_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_40_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-40(2) Reduce Detection Potential

<blockquote>Implement cryptographic mechanisms to reduce the detection potential of wireless links to
[Assignment: organization-defined level of reduction].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_40_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_40_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-40(3) Imitative or Manipulative Communications Deception

<blockquote>Implement cryptographic mechanisms to identify and reject wireless transmissions that are
deliberate attempts to achieve imitative or manipulative communications deception based on
signal parameters.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_40_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_40_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-40(4) Signal Parameter Identification

<blockquote>Implement cryptographic mechanisms to prevent the identification of [Assignment: organization-defined wireless transmitters] by using the transmitter signal parameters.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_40_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_41_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-41 Port and I/O Device Access

<blockquote>[Selection: Physically or Logically] disable or remove [Assignment: organization-defined connection ports or input/output devices] on [Assignment: organization-defined systems or system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_41_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_42_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-42 Sensor Capability and Data

<blockquote>a.   Prohibit the remote activation of environmental sensing capabilities on organizational
     systems or system components with the following exceptions: [Assignment:
organization-defined exceptions where remote activation of sensors is allowed]; and b.   Provide an explicit indication of sensor use to [Assignment: organization-defined class of users].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_42_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_42_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-42(1) Reporting to Authorized Individuals or Roles

<blockquote>Verify that the system is configured so that data or information collected by the [Assignment: organization-defined sensors] is only reported to authorized individuals or roles.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_42_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_42_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-42(2) Authorized Use

<blockquote>Employ [Assignment: organization-defined measures] so that data or information collected by
[Assignment: organization-defined sensors] is only used for authorized purposes.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_42_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_42_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-42(3) Prohibit Use of Devices

<blockquote>Prohibit the use of devices possessing [Assignment: organization-defined environmental sensing capabilities] in [Assignment: organization-defined facilities, areas, or systems].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_42_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_42_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-42(4) Notice of Collection

<blockquote>Employ the following measures to facilitate an individual’s awareness that personally identifiable
information is being collected by [Assignment: organization-defined sensors]: [Assignment: organization-defined measures].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_42_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_42_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-42(5) Collection Minimization

<blockquote>Employ [Assignment: organization-defined sensors] that are configured to minimize the collection
of information about individuals that is not needed.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_42_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_43_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-43 Usage Restrictions

<blockquote>a.    Establish usage restrictions and implementation guidelines for [Assignment: organization-defined system components]; and
b.    Authorize, monitor, and control the use of such components within the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_43_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_sc_44_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SC-44 Detonation Chambers

<blockquote>Employ a detonation chamber capability within [Assignment: organization-defined system, system component, or location].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_sc_44_impl|safe}}
{% endif %}
{% endfor %}

## SI - System and Information Integrity


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-1 System and Information Integrity Policy and Procedures

<blockquote>a.   Develop, document, and disseminate to [Assignment: organization-defined personnel or roles]:
     1.    A system and information integrity policy that:
           (a) Addresses purpose, scope, roles, responsibilities, management commitment,
               coordination among organizational entities, and compliance; and
           (b) Is consistent with applicable laws, Executive Orders, directives,
regulations, policies,
               standards, and guidelines; and
     2.    Procedures to facilitate the implementation of the system and information
integrity policy
           and the associated system and information integrity controls;
b.   Designate an [Assignment: organization-defined senior management official] to manage the
     system and information integrity policy and procedures;
c.   Review and update the current system and information integrity:
     1.    Policy [Assignment: organization-defined frequency]; and
     2.    Procedures [Assignment: organization-defined frequency];
d.   Ensure that the system and information integrity procedures implement the system and
     information integrity policy and controls; and
e.   Develop, document, and implement remediation actions for violations of the system and
     information integrity policy.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-2 Flaw Remediation

<blockquote>a.   Identify, report, and correct system flaws;
b.   Test software and firmware updates related to flaw remediation for effectiveness and potential
     side effects before installation;




c.    Install security-relevant software and firmware updates within [Assignment: organization-defined time-period] of the release of the updates; and
d.    Incorporate flaw remediation into the organizational configuration management process.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_2_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-2(1) Central Management

<blockquote>Centrally manage the flaw remediation process.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_2_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_2_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-2(2) Automated Flaw Remediation Status

<blockquote>Employ automated mechanisms [Assignment: organization-defined frequency] to determine the
state of system components with regard to flaw remediation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_2_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_2_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-2(3) Time to Remediate Flaws and Benchmarks for Corrective Actions

<blockquote>(a)   Measure the time between flaw identification and flaw remediation; and
(b) Establish [Assignment: organization-defined benchmarks] for taking corrective actions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_2_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_2_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-2(5) Automatic Software and Firmware Updates

<blockquote>Install [Assignment: organization-defined security-relevant software and firmware updates]
automatically to [Assignment: organization-defined system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_2_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_2_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-2(6) Removal of Previous Versions of Software and Firmware

<blockquote>Remove previous versions of [Assignment: organization-defined software and firmware components] after updated versions have been installed.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_2_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_2_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-2(7) Personally Identifiable Information

<blockquote>(a)    Identify and correct flaws related to the collection, usage, processing, or dissemination of
       personally identifiable information;
(b)    Report flaws related to personally identifiable information to the Senior Agency Official for
       Privacy;
(c)    Receive approval for correction of privacy-related flaws from the Senior Agency Official for
       Privacy;
(d)    Prior to installation, assess software and firmware updates related to flaw remediation for
       effectiveness and consistency with terms agreed upon in the privacy impact
assessment; (e)    Install privacy-relevant software and firmware updates within [Assignment: organization-defined time-period] of the release of the updates; and
(f)    Incorporate flaw remediation of personally identifiable information into the organizational
       configuration management process.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_2_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-3 Malicious Code Protection

<blockquote>a.    Implement [Selection (one or more): signature based; non-signature based] malicious code
      protection mechanisms at system entry and exit points to detect and eradicate
malicious code; b.    Automatically update malicious code protection mechanisms whenever new releases are
      available in accordance with organizational configuration management policy
and procedures; c.    Configure malicious code protection mechanisms to:
      1.    Perform periodic scans of the system [Assignment: organization-defined
frequency] and
            real-time scans of files from external sources at [Selection (one
or more); endpoint; network entry/exit points] as the files are downloaded, opened, or executed in accordance
            with organizational policy; and
      2.    [Selection (one or more): block malicious code; quarantine malicious
code; send alert to administrator; &lt;2&gt;] in response to malicious code
            detection; and
d.    Address the receipt of false positives during malicious code detection and eradication and the
      resulting potential impact on the availability of the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_3_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-3(1) Central Management

<blockquote>Centrally manage malicious code protection mechanisms.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_3_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_3_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-3(4) Updates Only by Privileged Users

<blockquote>Update malicious code protection mechanisms only when directed by a privileged user.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_3_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_3_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-3(6) Testing and Verification

<blockquote>(a)   Test malicious code protection mechanisms [Assignment: organization-defined frequency] by
      introducing a known benign, non-spreading test case into the system; and
(b) Verify that the detection of the test case and the associated incident reporting occur.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_3_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_3_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-3(8) Detect Unauthorized Commands

<blockquote>Detect [Assignment: organization-defined unauthorized operating system commands] through the
kernel application programming interface at [Assignment: organization-defined system hardware components] and [Selection (one or more): issue a warning; audit the command execution; prevent the execution of the command].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_3_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_3_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-3(9) Authenticate Remote Commands

<blockquote>Implement [Assignment: organization-defined security safeguards] to authenticate [Assignment: organization-defined remote commands].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_3_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_3_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-3(10) Malicious Code Analysis

<blockquote>(a)   Employ [Assignment: organization-defined tools and techniques] to analyze the
      characteristics and behavior of malicious code; and
(b) Incorporate the results from malicious code analysis into organizational incident response
    and flaw remediation processes.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_3_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4 System Monitoring

<blockquote>a.   Monitor the system to detect:
     1.    Attacks and indicators of potential attacks in accordance with [Assignment:
organization-defined monitoring objectives]; and
     2.    Unauthorized local, network, and remote connections;
b.   Identify unauthorized use of the system through [Assignment: organization-defined techniques and methods];
c.   Invoke internal monitoring capabilities or deploy monitoring devices:
     1.    Strategically within the system to collect organization-determined
essential information;
           and
     2.    At ad hoc locations within the system to track specific types of transactions
of interest to
           the organization;
d.   Protect information obtained from intrusion-monitoring tools from unauthorized access,
     modification, and deletion;
e.   Adjust the level of system monitoring activity when there is a change in risk to organizational
     operations and assets, individuals, other organizations, or the Nation;
f.   Obtain legal opinion regarding system monitoring activities; and
g.   Provide [Assignment: organization-defined system monitoring information] to [Assignment: organization-defined personnel or roles] [Selection (one or more): as needed; &lt;5&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(1) System-Wide Intrusion Detection System

<blockquote>Connect and configure individual intrusion detection tools into a system-wide intrusion detection
system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(2) Automated Tools and Mechanisms for Real-Time Analysis

<blockquote>Employ automated tools and mechanisms to support near real-time analysis of events.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(3) Automated Tool and Mechanism Integration

<blockquote>Employ automated tools and mechanisms to integrate intrusion detection tools and mechanisms
into access control and flow control mechanisms.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(4) Inbound and Outbound Communications Traffic

<blockquote>Monitor inbound and outbound communications traffic [Assignment: organization-defined frequency] for unusual or unauthorized activities or conditions.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(5) System-Generated Alerts

<blockquote>Alert [Assignment: organization-defined personnel or roles] when the following system-generated
indications of compromise or potential compromise occur: [Assignment: organization-defined compromise indicators].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(7) Automated Response to Suspicious Events

<blockquote>Notify [Assignment: organization-defined incident response personnel (identified by name and/or by role)] of detected suspicious events and take [Assignment: organization-defined least-disruptive actions to terminate suspicious events].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(9) Testing of Monitoring Tools and Mechanisms

<blockquote>Test intrusion-monitoring tools and mechanisms [Assignment: organization-defined frequency].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(10) Visibility of Encrypted Communications

<blockquote>Make provisions so that [Assignment: organization-defined encrypted communications traffic] is
visible to [Assignment: organization-defined system monitoring tools and mechanisms].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(11) Analyze Communications Traffic Anomalies

<blockquote>Analyze outbound communications traffic at the external boundary of the system and selected
[Assignment: organization-defined interior points within the system] to discover anomalies.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(12) Automated Organization-Generated Alerts

<blockquote>Employ automated mechanisms to alert [Assignment: organization-defined personnel or roles]
when the following organization-generated indications of inappropriate or unusual activities with
security or privacy implications occur: [Assignment: organization-defined activities that trigger alerts].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(13) Analyze Traffic and Event Patterns

<blockquote>(a)   Analyze communications traffic and event patterns for the system;
(b) Develop profiles representing common traffic and event patterns; and
(c)   Use the traffic and event profiles in tuning system-monitoring devices to reduce the number of
      false positives and false negatives.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(14) Wireless Intrusion Detection

<blockquote>Employ a wireless intrusion detection system to identify rogue wireless devices and to detect
attack attempts and potential compromises or breaches to the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(15) Wireless to Wireline Communications

<blockquote>Employ an intrusion detection system to monitor wireless communications traffic as the traffic
passes from wireless to wireline networks.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(16) Correlate Monitoring Information

<blockquote>Correlate information from monitoring tools and mechanisms employed throughout the system.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_17_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(17) Integrated Situational Awareness

<blockquote>Correlate information from monitoring physical, cyber, and supply chain activities to achieve
integrated, organization-wide situational awareness.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_17_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_18_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(18) Analyze Traffic and Covert Exfiltration

<blockquote>Analyze outbound communications traffic at the external boundary or perimeter of the system and
at [Assignment: organization-defined interior points within the system] to detect covert exfiltration
of information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_18_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_19_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(19) Individuals Posing Greater Risk

<blockquote>Implement [Assignment: organization-defined additional monitoring] of individuals who have been
identified by [Assignment: organization-defined sources] as posing an increased level of risk.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_19_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_20_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(20) Privileged Users

<blockquote>Implement [Assignment: organization-defined additional monitoring] of privileged users.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_20_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_21_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(21) Probationary Periods

<blockquote>Implement [Assignment: organization-defined additional monitoring] of individuals during
[Assignment: organization-defined probationary period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_21_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_22_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(22) Unauthorized Network Services

<blockquote>Detect network services that have not been authorized or approved by [Assignment: organization-defined authorization or approval processes] and [Selection (one or more): audit; alert &lt;2&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_22_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_23_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(23) Host-Based Devices

<blockquote>Implement [Assignment: organization-defined host-based monitoring mechanisms] at
[Assignment: organization-defined system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_23_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_24_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(24) Indicators of Compromise

<blockquote>Discover, collect, and distribute to [Assignment: organization-defined personnel or roles],
indicators of compromise.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_24_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_4_25_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-4(25) Personally Identifiable Information Monitoring

<blockquote>Employ automated mechanisms to monitor:
(a)   For unauthorized access or usage of personally identifiable information; and
(b) The collection, creation, accuracy, relevance, timeliness, impact, and completeness of
    personally identifiable information.
                     Monitoring the collection, creation, accuracy, relevance, timeliness,
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_4_25_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-5 Security Alerts, Advisories, and Directives

<blockquote>a.    Receive system security alerts, advisories, and directives from [Assignment: organization-defined external organizations] on an ongoing basis;
b.    Generate internal security alerts, advisories, and directives as deemed necessary;
c.    Disseminate security alerts, advisories, and directives to: [Selection (one or more): &lt;2&gt;; &lt;3&gt;; &lt;4&gt;]; and
d.    Implement security directives in accordance with established time frames, or notify the
      issuing organization of the degree of noncompliance.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_5_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-5(1) Automated Alerts and Advisories

<blockquote>Employ automated mechanisms to make security alert and advisory information available
throughout the organization.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_5_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-6 Security and Privacy Function Verification

<blockquote>a.    Verify the correct operation of [Assignment: organization-defined security and privacy functions];





b.    Perform this verification [Selection (one or more): &lt;2&gt;; upon command by user with appropriate privilege; &lt;3&gt;];
c.    Notify [Assignment: organization-defined personnel or roles] of failed security and privacy
      verification tests; and
d.    [Selection (one or more): Shut the system down; Restart the system; &lt;5&gt;] when anomalies are discovered.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_6_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-6(2) Automation Support for Distributed Testing

<blockquote>Implement automated mechanisms to support the management of distributed security and privacy
function testing.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_6_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_6_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-6(3) Report Verification Results

<blockquote>Report the results of security and privacy function verification to [Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_6_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7 Software, Firmware, and Information Integrity

<blockquote>Employ integrity verification tools to detect unauthorized changes to [Assignment: organization-defined software, firmware, and information].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(1) Integrity Checks

<blockquote>Perform an integrity check of [Assignment: organization-defined software, firmware, and information] [Selection (one or more): at startup; at &lt;2&gt;; &lt;3&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(2) Automated Notifications of Integrity Violations

<blockquote>Employ automated tools that provide notification to [Assignment: organization-defined personnel or roles] upon discovering discrepancies during integrity verification.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(3) Centrally Managed Integrity Tools

<blockquote>Employ centrally managed integrity verification tools.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(5) Automated Response to Integrity Violations

<blockquote>Automatically [Selection (one or more): shut the system down; restart the system; implement &lt;1&gt;] when integrity violations are discovered.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(6) Cryptographic Protection

<blockquote>Implement cryptographic mechanisms to detect unauthorized changes to software, firmware, and
information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(7) Integration of Detection and Response

<blockquote>Incorporate the detection of the following unauthorized changes into the organizational incident
response capability: [Assignment: organization-defined security-relevant changes to the system].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(8) Auditing Capability for Significant Events

<blockquote>Upon detection of a potential integrity violation, provide the capability to audit the event and
initiate the following actions: [Selection (one or more): generate an audit record; alert current user; alert &lt;1&gt;; &lt;2&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_9_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(9) Verify Boot Process

<blockquote>Verify the integrity of the boot process of [Assignment: organization-defined system components].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_9_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(10) Protection of Boot Firmware

<blockquote>Implement [Assignment: organization-defined security safeguards] to protect the integrity of boot
firmware in [Assignment: organization-defined system components].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(11) Confined Environments With Limited Privileges

<blockquote>Require that [Assignment: organization-defined user-installed software] execute in a confined
physical or virtual machine environment with limited privileges.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(12) Integrity Verification

<blockquote>Require that the integrity of [Assignment: organization-defined user-installed software] be verified
prior to execution.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(13) Code Execution in Protected Environments

<blockquote>Allow execution of binary or machine-executable code only in confined physical or virtual machine
environments and with the explicit approval of [Assignment: organization-defined personnel or roles] when such code is:
(a)   Obtained from sources with limited or no warranty; and/or



 (b) Without the provision of source code.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(14) Binary or Machine Executable Code

<blockquote>(a)   Prohibit the use of binary or machine-executable code from sources with limited or no
      warranty and without the provision of source code; and
(b) Provide exceptions to the source code requirement only for compelling mission or operational
    requirements and with the approval of the authorizing official.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(15) Code Authentication

<blockquote>Implement cryptographic mechanisms to authenticate [Assignment: organization-defined software or firmware components] prior to installation.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_7_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-7(16) Time Limit on Process Execution Without Supervision

<blockquote>Prohibit processes from executing without supervision for more than [Assignment: organization-defined time-period].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_7_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-8 Spam Protection

<blockquote>a.     Employ spam protection mechanisms at system entry and exit points to detect and act on
       unsolicited messages; and
b.     Update spam protection mechanisms when new releases are available in accordance with
       organizational configuration management policy and procedures.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_8_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_8_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-8(1) Central Management

<blockquote>Centrally manage spam protection mechanisms.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_8_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_8_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-8(2) Automatic Updates

<blockquote>Automatically update spam protection mechanisms.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_8_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_8_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-8(3) Continuous Learning Capability

<blockquote>Implement spam protection mechanisms with a learning capability to more effectively identify
legitimate communications traffic.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_8_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_10_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-10 Information Input Validation

<blockquote>Check the validity of [Assignment: organization-defined information inputs].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_10_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_10_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-10(1) Manual Override Capability

<blockquote>(a)   Provide a manual override capability for input validation of [Assignment: organization-defined inputs];
(b) Restrict the use of the manual override capability to only [Assignment: organization-defined authorized individuals]; and
(c)   Audit the use of the manual override capability.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_10_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_10_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-10(2) Review and Resolve of Errors

<blockquote>Review and resolve input validation errors within [Assignment: organization-defined time-period].</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_10_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_10_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-10(3) Predictable Behavior

<blockquote>Verify that the system behaves in a predictable and documented manner when invalid inputs are
received.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_10_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_10_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-10(4) Timing Interactions

<blockquote>Account for timing interactions among system components in determining appropriate responses
for invalid inputs.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_10_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_10_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-10(5) Restrict Inputs to Trusted Sources and Approved Formats

<blockquote>Restrict the use of information inputs to [Assignment: organization-defined trusted sources] and/or
[Assignment: organization-defined formats].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_10_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_11_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-11 Error Handling

<blockquote>a.    Generate error messages that provide information necessary for corrective actions without
      revealing information that could be exploited; and
b.    Reveal error messages only to [Assignment: organization-defined personnel or roles].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_11_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_12_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-12 Information Management and Retention

<blockquote>Manage and retain information within the system and information output from the system
in accordance with applicable laws, Executive Orders, directives, regulations, policies, standards,
guidelines and operational requirements.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_12_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_12_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-12(1) Limit Personally Identifiable Information Elements in Testing, Training, and Research

<blockquote>Limit personally identifiable information being processed in the information life cycle to the
[Assignment: organization-defined elements] identified in the privacy risk assessment.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_12_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_12_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-12(2) Minimize Personally Identifiable Information

<blockquote>Use [Assignment: organization-defined techniques] to minimize the use of personally identifiable
information for research, testing, or training, in accordance with the privacy risk assessment.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_12_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_13_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-13 Predictable Failure Prevention

<blockquote>a.    Determine mean time to failure (MTTF) for [Assignment: organization-defined system components] in specific environments of operation; and
b.    Provide substitute system components and a means to exchange active and standby
      components at [Assignment: organization-defined MTTF substitution criteria].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_13_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_13_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-13(1) Transferring Component Responsibilities

<blockquote>Takes system components out of service by transferring component responsibilities to substitute
components no later than [Assignment: organization-defined fraction or percentage] of mean time
to failure.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_13_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_13_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-13(3) Manual Transfer Between Components

<blockquote>Manually initiate transfers between active and standby system components when the use of the
active component reaches [Assignment: organization-defined percentage] of the mean time to
failure.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_13_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_13_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-13(4) Standby Component Installation and Notification

<blockquote>If system component failures are detected:
(a)   Ensure that the standby components are successfully and transparently installed within
      [Assignment: organization-defined time-period]; and
(b) [Selection (one or more): Activate &lt;2&gt;; Automatically shut down the system; &lt;3&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_13_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_13_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-13(5) Failover Capability

<blockquote>Provide [Selection: real-time; near real-time] [Assignment: organization-defined failover capability]
for the system.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_13_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_14_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-14 Non-Persistence

<blockquote>Implement non-persistent [Assignment: organization-defined system components and services] that are initiated in a known state and terminated [Selection (one or more): upon end of session of use; periodically at &lt;2&gt;].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_14_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_14_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-14(1) Refresh From Trusted Sources

<blockquote>Obtain software and data employed during system component and service refreshes from
[Assignment: organization-defined trusted sources].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_14_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_15_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-15 Information Output Filtering

<blockquote>Validate information output from [Assignment: organization-defined software programs and/or applications] to ensure that the information is consistent with the expected content.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_15_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_15_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-15(1) Limit Personally Identifiable Information Dissemination

<blockquote>Limit the dissemination of personally identifiable information to [Assignment: organization-defined elements] identified in the privacy risk assessment and consistent with authorized purposes.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_15_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_16_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-16 Memory Protection

<blockquote>      Implement [Assignment: organization-defined security safeguards] to protect the system

memory from unauthorized code execution.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_16_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_17_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-17 Fail-Safe Procedures

<blockquote>Implement [Assignment: organization-defined fail-safe procedures] when [Assignment: organization-defined failure conditions occur].
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_17_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_18_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-18 Information Disposal

<blockquote>Use [Assignment: organization-defined techniques or methods] to dispose of, destroy, or
erase information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_18_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_19_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-19 Data Quality Operations

<blockquote>a.   Upon collection or creation of personally identifiable information, check for the accuracy,
     relevance, timeliness, impact, completeness, and de-identification of that information across
     the information life cycle; and
b.   Check for and correct as necessary [Assignment: organization-defined frequency] and across
     the information life cycle:
     1.    Inaccurate or outdated personally identifiable information;
     2.    Personally identifiable information of incorrectly determined impact; or



      3.   Incorrectly de-identified personally identifiable information.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_19_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_19_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-19(1) Updating and Correcting Personally Identifiable Information

<blockquote>Employ technical controls to correct personally identifiable information used in organizational
programs and systems that is inaccurate or outdated, incorrectly determined regarding impact, or
incorrectly de-identified.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_19_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_19_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-19(2) Data Tags

<blockquote>Employ data tags to automate tracking of personally identifiable information across the
information life cycle within organizational systems.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_19_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_19_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-19(3) Personally Identifiable Information Collection

<blockquote>Collect personally identifiable information directly from the individual.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_19_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_20_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-20 De-Identification

<blockquote>Remove personally identifiable information from datasets.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_20_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_20_1_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-20(1) Collection

<blockquote>De-identify the dataset upon collection by not collecting personally identifiable information.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_20_1_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_20_2_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-20(2) Archiving

<blockquote>Refrain from archiving personally identifiable information elements if those elements in a dataset
will not be needed after the dataset is archived.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_20_2_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_20_3_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-20(3) Release

<blockquote>Remove personally identifiable information elements from a dataset prior to its release if those
elements in the dataset do not need to be part of the data release.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_20_3_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_20_4_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-20(4) Removal, Masking, Encryption, Hashing, or Replacement of Direct Identifiers

<blockquote>Remove, mask, encrypt, hash, or replace direct identifiers in a dataset.</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_20_4_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_20_5_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-20(5) Statistical Disclosure Control

<blockquote>Manipulate numerical data, contingency tables, and statistical findings so that no person or
organization is identifiable in the results of the analysis.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_20_5_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_20_6_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-20(6) Differential Privacy

<blockquote>Prevent disclosure of personally identifiable information by adding non-deterministic noise to the
results of mathematical operations before the results are reported.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_20_6_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_20_7_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-20(7) Validated Software

<blockquote>Perform de-identification using validated algorithms and software that is validated to implement
the algorithms.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_20_7_impl|safe}}
{% endif %}
{% endfor %}


{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp" in question.protocol and answer and 'ssp_nistsp80053r5_control_si_20_8_impl' in answer.output_documents %}
{% if not ns.has_control_impl %}

### SI-20(8) Motivated Intruder

<blockquote>Perform a motivated intruder test on the de-identified dataset to determine if the identified data
remains or if the de-identified data can be re-identified.
</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.ssp_nistsp80053r5_control_si_20_8_impl|safe}}
{% endif %}
{% endfor %}

