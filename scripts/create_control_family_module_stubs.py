# Create control family module templates.

import os.path, collections, rtyaml

control_families = {
  "AC": { "name": "Access Control" },
  "AU": { "name": "Audit and Accountability" },
  "AT": { "name": "Awareness and Training" },
  "CM": { "name": "Configuration Management" },
  "CP": { "name": "Contingency Planning" },
  "IA": { "name": "Identification and Authentication" },
  "IR": { "name": "Incident Response" },
  "MA": { "name": "Maintenance" },
  "MP": { "name": "Media Protection" },
  "PS": { "name": "Personnel Security" },
  "PE": { "name": "Physical and Environmental Protection" },
  "PL": { "name": "Planning" },
  "PM": { "name": "Program Management" },
  "RA": { "name": "Risk Assessment" },
  "CA": { "name": "Security Assessment and Authorization" },
  "SC": { "name": "System and Communications Protection" },
  "SI": { "name": "System and Information Integrity" },
  "SA": { "name": "System and Services Acquisition" },
}

template = open("control_family_module_template.yaml").read()
project = rtyaml.load(open("../modules/project2.yaml"))

for control_family, info in sorted(control_families.items()):
	fn = "../modules/controlfam_%s.yaml" % control_family.lower()
	if os.path.exists(fn): continue

	# Create the module file.
	with open(fn, "w") as f:
		f.write(template
			.replace("#CODE#", control_family)
			.replace("#CODE_LOWERCASE#", control_family.lower())	
			.replace("#NAME#", info["name"])
			)

	# Add to the project module.
	project["questions"].append(collections.OrderedDict([
		("id", "controlfam_" + control_family.lower()),
		("title", "%s - %s" % (control_family, info["name"])),
		("type", "module"),
		("module-id", "controlfam_" + control_family.lower()),
		("tab", "Controls"),
		("group", "Control Families"),
	]))

with open("../modules/project2.yaml", "w") as f:
	rtyaml.dump(project, f)
