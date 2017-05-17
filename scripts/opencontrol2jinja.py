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
    <h2>{}</h2>""".format(control_key)

    template_text += """
    +% if not project.infrastructure %~
      There will be infrastructure.
    +% else %~
      ++project.infrastructure.output_documents.ssp_template_{}|safe~~
    +% endif %~\n""".format(control_key_str).replace("+","{").replace("~","}")

    template_text += "{}".format(control_text)

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
