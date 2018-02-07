# Usage:
#
# python3 make_control_selection_list.py https://github.com/GovReady/nist-sp-800-53-r5-data/raw/master/control-metadata.yaml

import urllib.request
import sys

import rtyaml

controls = rtyaml.load(urllib.request.urlopen(sys.argv[1]))

for control in controls:
  if not control["baseline"]:
    if not control["attributes"]["privacy-related"]:
      baseline = "all baselines"
    else:
      baseline = "privacy-related"
  elif control["baseline"]["low"]:
    baseline = "Low"
  elif control["baseline"]["moderate"]:
    baseline = "Moderate"
  elif control["baseline"]["high"]:
    baseline = "High"
  else:
      # There is no baseline selected. Does that mean it's
      # up to the organization? Skip that for now.
      continue

  print("""{}: {} ({})\n\n""".format(
    control["control"],
    control["name"],
    baseline,
  ))
