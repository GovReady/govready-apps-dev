id: ssp_nist80053r4_PS_7
title: NIST 800-53r4 PS-7 Third-Party Personnel Security
format: markdown
...
{% if project.general_info.exists != "yes" %}The following controls will be in place with the completion of the Rules of Behavior.{% endif %}
All contractor support personnel are required to meet the same personnel security policy requirements as {{organization}} personnel who have privileged access to the IT System. Third party providers {% if project.general_info.exists == "yes" %}are required{% else %}will be required{% endif %} to review and sign the Rules of Behavior found in the document officially titled _{{project.general_info.official_name}}_ prior to being granted access to the system.

