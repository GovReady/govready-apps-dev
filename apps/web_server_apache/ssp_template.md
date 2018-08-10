id: ssp_template
format: markdown
...
{% if not system_details.hostname %}
  The system will use an Apache web server.
{% else %}
  The system has an Apache web server at {{system_details.hostname}}.
{% endif %}
