id: ssp_template
format: markdown
...
{% if not fisma_level.fisma_level.text %}
  The team is currently working on determining the system impact level.

{% else %}
  Your system's FISMA Level is **{{fisma_level.fisma_level.text}}**.

  Information Types: {{fisma_level.information_types.text}}

  Impact Level based on Information Types: {{fisma_level.information_types_level.text}}

  PII Types: {{fisma_level.pii_types_collected.text}}

  PII Impact Level: {{fisma_level.pii_impact_level.text}}

  PHI? {{fisma_level.phi_has_any_phi.text}}

PHI Impact Level: {{fisma_level.phi_impact_level.text}}
{% endif %}
