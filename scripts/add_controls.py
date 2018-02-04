# Adds controls to the SSP, Control Matrix, and POAMs modules.

import html
import re
import urllib.request
import rtyaml

# Get the controls.
nist_standard_url = "https://raw.githubusercontent.com/GovReady/nist-sp-800-53-r5-data/master/opencontrol-standard.yaml"
niststandard = rtyaml.load(urllib.request.urlopen(nist_standard_url).read())
protocol = "govready.com/apps/compliance/2018/nist-sp-800-53-r5-ssp"

def slug(control_number):
  return "ssp_nistsp80053r5_control_" + control_number.replace(".", "_").replace("-", "_").replace("(", "_").replace(")", "").lower() + "_impl"

# Get the controls by family.
controls_by_family = []
prev_family = None
for control_number, control_data in niststandard.items():
  if not isinstance(control_data, dict): continue
  if control_data["family"] != prev_family:
    controls_by_family.append({
      "name": control_data["family"],
      "controls": [] })
    prev_family = control_data["family"]
  controls_by_family[-1]["controls"].append((control_number, control_data))

# Fix up the SSP.
with open("../apps/govready-q-ato/ssp.yaml", "r+") as f:
  # Read.
  module = rtyaml.load(f)

  # Get template.
  templ = [doc for doc in module["output"] if doc["id"] == "ssp"][0]

  # Split on a sentinel.
  parts = re.split("\s*{# BEGIN CONTROLS #}\s*", templ["template"])
  if len(parts) == 1:
    parts.append("")

  # Construct the second part of the document.
  parts[1] = ""
  controlfam = None
  for control_number, control_data in niststandard.items():

    # Add a second-level heading for control families.
    if not isinstance(control_data, dict): continue # skip metadata
    if control_data.get("family") != controlfam:
      parts[1] += "## " + control_data["family"] + "\n\n"
      controlfam = control_data.get("family")

    # Add a third-level heading for the control, then the control
    # text, and the loop over all control implementations.
    parts[1] += """
{% set ns = namespace(has_control_impl=false) %}
{% for question, answer in project.questions %}{% if "protocol" in question and "PROTOCOL" in question.protocol and answer and 'CONTROL_QID' in answer.output_documents %}
{% if not ns.has_control_impl %}

### HEADING

<blockquote>CONTROL_TEXT</blockquote>

{% endif %}
{% set ns.has_control_impl = true %}
{{answer.output_documents.CONTROL_QID|safe}}
{% endif %}
{% endfor %}

"""\
   .replace("HEADING", control_number + " " + control_data["name"])\
   .replace("CONTROL_TEXT", html.escape(control_data["description"]))\
   .replace("PROTOCOL", protocol)\
   .replace("CONTROL_QID", slug(control_number))

  templ["template"] = "\n\n\n{# BEGIN CONTROLS #}\n\n\n".join(parts)

  # Update.
  f.seek(0)
  f.truncate()
  f.write(rtyaml.dump(module))


# Create the control matrix. The columns are control families and the rows are
# controls, with the cells listing which controls are implemented by that app.
with open("../apps/govready-q-ato/matrix.yaml", "r+") as f:
  # Read.
  module = rtyaml.load(f)

  # Get template.
  templ = [doc for doc in module["output"] if doc["id"] == "control_matrix"][0]

  ret = """
  <div style="overflow-x: auto">
  <table class="table">
    <thead>
      <tr>
"""
  # Create a column for each control family, in the order the families appear
  # in the full control list. Repeat the component name column every so many
  # columns because the table is wide and we don't have a way to lock the
  # first col.
  def should_do_component_col_here(i):
    return (i % 5) == 0
  for i, family in enumerate(controls_by_family):
    if should_do_component_col_here(i):
      ret += """        <th>Component</th>\n"""
    ret += """        <th>{}</th>\n""".format(html.escape(family["name"]))

  ret += """    </thead>
    <tbody>"""

  # Create a row for each component - each answered question that implements the
  # standard protocol. This loop is performed during template execution.

  ret += """
  {% for question, answer in project.questions %}
    {% if "protocol" in question and "PROTOCOL" in question.protocol and answer %}
      <tr>
""".replace("PROTOCOL", protocol)

  # For each control family, create a cell.
  for i, family in enumerate(controls_by_family):
    if should_do_component_col_here(i):
      ret += """    <th scope="row">{{answer}}</th>\n"""

    ret += """
    <td>"""

    for control_number, control_data in family["controls"]:
      ret += """
      {% if 'CONTROLQID' in answer.output_documents %}
        {% if answer.output_documents.CONTROLQID %}
          <div data-toggle="popover" data-placement="bottom" data-title="CONTROLNUM: CONTROLNAME" data-content="{{answer.output_documents.CONTROLQID|forceescape}}" data-html="true">
            CONTROLNUM
          </div>
        {% endif %}
      {% endif %}"""\
        .replace("CONTROLQID", slug(control_number))\
        .replace("CONTROLNUM", control_number)\
        .replace("CONTROLNAME", html.escape(control_data["name"]))

    ret += """
    </td>
"""

  ret += """
        </td>
      </tr>
    {% endif %}
  {% endfor %}"""

  # Add a row for controls that are not implemented. This is tricky. Since we can't
  # know now whether a control is implemented by a component, we have to do it during
  # template execution. We need to check if a control number is implemented by *any*
  # components. Jinja2 doesn't have an obvious way to do it. The non-obvious way is
  # by using a {% set %} to collect all of the controls that are implemente, and then
  # checking if a control is listed in the set (using a string comparison) for each
  ret += """
  <tr><th scope=row>Controls Not Implemented</th>"""

  # Create a list of all output document IDs that are present across all controls.
  ret += """
  {% set implemented_controls_document_ids %}
  {% for question, answer in project.questions %}
  {% if "protocol" in question and "PROTOCOL" in question.protocol and answer %}
    {% for doc in answer.output_documents %}
      {{doc}}
    {% endfor %}
  {% endif %}
  {% endfor %}
  {% endset %}""".replace("PROTOCOL", protocol)

  # For each control family, create a cell.
  prev_family = None
  for control_number, control_data in niststandard.items():
    if not isinstance(control_data, dict): continue
    if control_data["family"] != prev_family:
      if prev_family: ret += "</td>" # not first in row
      ret += """
      <td>"""
    prev_family = control_data["family"]

    # For each control, test if any component implements it.
    ret += """
  {% if 'CONTROLQID' not in implemented_controls_document_ids %}
    <div data-content="CONTROLTEXT" data-placement="bottom" data-title="CONTROLNUM CONTROLNAME" data-toggle="popover" style="cursor: pointer;">
      CONTROLNUM
    </div>
  {% endif %}"""\
    .replace("CONTROLQID", slug(control_number))\
    .replace("CONTROLNUM", control_number)\
    .replace("CONTROLNAME", html.escape(control_data["name"]))\
    .replace("CONTROLTEXT", html.escape(control_data["description"].strip()))

  ret += """
        </td>
      </tr>"""

  # Close the table.

  ret += """
  </tbody>
  </table>
  </div>"""

  templ["template"] = ret.strip()

  # Update.
  f.seek(0)
  f.truncate()
  f.write(rtyaml.dump(module))
