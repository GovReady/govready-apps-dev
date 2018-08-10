id: ssp_nist80053r4_PL_4
title: NIST 800-53r4 PL-4 Rules of Behavior
format: markdown
...
{% if project.general_info.exists == 'yes' %}
{{organization}} implements Control PL-4 with its Rules of Behavior document officially titled _{{project.general_info.official_name}}_. The Rules of Behavior describes users' responsibilities and expected behavior when using {{organization}} IT resources. {{project.rob.applies_to}}
The Rules of Behavior doucement is maintained as a {{project.general_info.source_repo.text}}. {{project.general_info.source_repo_identifier}}
The {{project.general_info.role_owner}} maintains the Rules of Behavior and reviews the Rules of Behavior {{project.general_info.review_frequency.text}}. 

{{project.general_info.obtain}}
{% if project.general_info.source_public == 'yes' %} The Rules of Behavior is available publicly online at [{{project.general_info.source_public_url}}]({{project.general_info.source_public_url}}). {% else %} The Rules of Behavior is not available publicly online. {% endif %}
{% else %}
{{organization}} will implement Control PL-4 with Rules of Behavior document officially titled _{{project.general_info.official_name}}_. The Rules of Behavior will describe users' responsibilities and expected behavior when using {{organization}} IT resources. {{project.rob.applies_to}}
The Rules of Behavior doucement will be maintained as a {{project.general_info.source_repo.text}}. {{project.general_info.source_repo_identifier}}
The {{project.general_info.role_owner}} will maintain the Rules of Behavior and review them {{project.general_info.review_frequency.text}}. 

{{project.general_info.obtain}}
{% if project.general_info.source_public == 'yes' %} The Rules of Behavior will be available publicly online at [{{project.general_info.source_public_url}}]({{project.general_info.source_public_url}}). {% else %} The Rules of Behavior will not be available publicly online. {% endif %}
{% endif %}

