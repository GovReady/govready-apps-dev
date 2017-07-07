# Generate a Jinja template file from OpenControl data.
#
# usage:
# python3 opencontrol2jinja.py https://github.com/owner/repo opencontrol.yaml
#
# ex:
# python3 opencontrol2jinja.py https://github.com/18F/cg-compliance ../modules/drupal_website/ssp_temp.txt

import sys
import datetime
import re
import collections
import os.path

import pytz
import rtyaml
import compliancelib

# Fetch the OpenControl data including any referenced OpenControl files.
sp = compliancelib.SystemCompliance()
sp.load_system_from_opencontrol_repo(sys.argv[1])

# Collate the component data by control.
controls = collections.defaultdict(lambda : "")
for component_name, component_data in sp.system["components"].items():
    for control in component_data["satisfies"]:

        # control_key = re.sub("[^a-z0-9]", "_", control["control_key"].lower()).strip("_")
        control_key = control["control_key"]

        control_text = "## " + component_name.strip() + "\n\n"
        for narrative_block in control["narrative"]:
            if not isinstance(narrative_block, dict): continue # some upstream data problem
            if not narrative_block["text"].strip(): continue
            if narrative_block.get("key"):
                control_text += "### Part " + narrative_block["key"].strip() + "\n\n"
            control_text += narrative_block["text"].strip() + "\n\n"

        controls[control_key] += control_text.strip() + "\n" # one final \n gives better YAML output

# Create empty string to store template text
template_text = ""

# Sort by control_key in tuple
controls_sorted = sorted([item for item in controls.items()], key=lambda x: x[0])

for control_key, control_text in controls_sorted:

    control_key_str = re.sub("[^a-z0-9]", "_", control_key.lower()).strip("_")

    template_text += """
      <h3>{control_key}</h3>
      <table class="table" style="margin-top: 1.5em">
        <thead>
          <th colspan="2">
            <div class="row">
              <div class="col-xs-3">
                {control_key}
              </div>
              <div class="col-xs-9">
                Control Summary Information
              </div>
            </div>
          </th>
        </thead>
        <tbody>
          <tr>
            <td width="30%">Responsible Role:</th>
            <td>
                ...
            </td>
          </tr>
          <tr>
            <td>Parameter:</th>
            <td>
                ...
            </td>
          </tr>
          <tr>
            <td colspan="2">
              <div style="margin-bottom: .5em">Implementation Status:</div>
              +% for key, text in [
      ["implemented", "Implemented"],
      ["partially_implemented", "Partially Implemented"],
      ["planned", "Planned"],
      ["alternative_implementation", "Alternative Implementation"],
      ["not_applicable", "Not Applicable"]] %~
              <div class="radio">
                <label>
                  <input type="checkbox" disabled="disabled"> ++text~~
                </label>
              </div>
              +% endfor %~
            </td>
          </tr>
          <tr>
            <td colspan="2">
              <div style="margin-bottom: .5em">Control Origination:</div>
              +% for key, text in [["service_provider_corporate", "Service Provider Corporate"],
      ["service_provider_system_specific", "Service Provider System Specific"],
      ["service_provider_hybrid", "Service Provider Hybrid (Corporate and System Specific)"],
      ["configured_by_customer", "Configured by Customer (Customer System Specific)"],
      ["provided_by_customer", "Provided by Customer (Customer System Specific)"],
      ["shared", "Shared (Service Provider and Customer Responsibility)"],
      ["inherited", "Inherited from enterprise IT service"]] %~
              <div class="radio">
                <label>
                  <input type="checkbox" disabled="disabled"
                    > ++text~~
                </label>
              </div>
              +% endfor %~
            </td>
          </tr>
        </body>
      </table>
      <table class="table">
        <thead>
          <th colspan="2">
            {control_key} What is the solution and how is it implemented?
          </th>
        </thead>
        <tbody>
          <tr>
            <td colspan="2">
                +% if not project.infrastructure %~
                  There will be infrastructure.
                +% else %~
                  ++project.infrastructure.output_documents.ssp_template_{control_key_str}|safe~~
                +% endif %~
            </td>
          </tr>
        </tbody>
      </table>
      """.format(
        control_key=control_key,
        control_key_str=control_key_str,
    ).replace("+","{").replace("~","}")

    #template_text += "{}".format(control_text)

    # for doc in outputs:
    #     if doc.get("id") == "ssp_template_" + control_key:
    #         break
    # else:
    #     doc = collections.OrderedDict()
    #     doc["id"] = "ssp_template_" + control_key
    #     outputs.append(doc)

    # doc["format"] = "markdown"
    # doc["template"] = control_text

with open(sys.argv[2], "w") as f:
    print(template_text, file=f)
