# Generate a YAML file from OpenControl data.
#
# usage:
# python3 opencontrol.py https://github.com/owner/repo opencontrol.yaml
#
# ex:
# python3 opencontrol.py https://github.com/18F/cg-compliance ../modules/cloud_dot_gov/app.yaml

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

        control_key = re.sub("[^a-z0-9]", "_", control["control_key"].lower()).strip("_")

        control_text = "## " + component_name.strip() + "\n\n"
        for narrative_block in control["narrative"]:
            if not isinstance(narrative_block, dict): continue # some upstream data problem
            if not narrative_block["text"].strip(): continue
            if narrative_block.get("key"):
                control_text += "### Part " + narrative_block["key"].strip() + "\n\n"
            control_text += narrative_block["text"].strip() + "\n\n"

        controls[control_key] += control_text.strip() + "\n" # one final \n gives better YAML output

# Open an existing YAML file.
if os.path.exists(sys.argv[2]):
    existing_yaml = rtyaml.load(open(sys.argv[2]))
else:
    existing_yaml = {
    }

# Store the date so we know when we fetched the opencontrol data.
existing_yaml["opencontrol_fetch_date"] = pytz.timezone("UTC").localize(datetime.datetime.utcnow()).isoformat()

# Put the control texts into output documents.
outputs = existing_yaml.setdefault("output", [])
for control_key, control_text in controls.items():
    for doc in outputs:
        if doc.get("id") == "ssp_template_" + control_key:
            break
    else:
        doc = collections.OrderedDict()
        doc["id"] = "ssp_template_" + control_key
        outputs.append(doc)

    doc["format"] = "markdown"
    doc["template"] = control_text

with open(sys.argv[2], "w") as f:
    rtyaml.dump(existing_yaml, f)
