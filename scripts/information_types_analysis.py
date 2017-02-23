from collections import OrderedDict
import rtyaml
import re

infotypes = rtyaml.load(open("information_types.yaml"))

all_info_types = []
seen_infotype_parent_q = set()
infotype_questions = OrderedDict([
	("information_types_categories", OrderedDict([
		("id", "information_types_categories"),
		("title", "Which categories of information does your system contain?"),
		("prompt", "Check all that apply."),
		("type", "multiple-choice"),
		("choices", []),
	])),
])

def process_information_types(infotypes, path=[]):
	for subtype in infotypes:
		if "subtypes" not in subtype:
			# Base case.

			if not len(path): continue

			# Ensure the top-level category is an option.
			parent_q = path[0]
			if parent_q["code"][0] == "C":
				parent_q = path[1]
			if parent_q["code"] not in seen_infotype_parent_q:
				infotype_questions["information_types_categories"]["choices"].append(OrderedDict([
					("key", parent_q["code"]),
					("text", parent_q["title"]), # + " (" + parent_q["code"] + ")"),
				]))
				seen_infotype_parent_q.add(parent_q["code"])

			# Add this to the category's sub-choices.
			p_key = "information_type_category_" + parent_q["code"].replace(".", "_")
			infotype_questions.setdefault(p_key,
				OrderedDict([
					("id", p_key),
					("title", "Which types of %s information does your system contain?" % parent_q["title"]),
					("prompt", "Check all that apply."),
					("type", "multiple-choice"),
					("choices", []),
					("impute", [
						OrderedDict([
							("condition", "\"" + parent_q["code"] + "\" not in information_types_categories"),
							("value", []),
						])
					]),
				]))["choices"].append(
					OrderedDict([
						("key", subtype["code"]),
						("text", subtype["title"]),
						("help", subtype["description"]["text"].strip() + " (NIST 800-60 Vol 2 " + subtype["code"] + ")\n"),
					])			
			)

			# Remember it.
			all_info_types.append(subtype)

		else:
			# Recurse.
			process_information_types(subtype["subtypes"], path=path+[subtype])

# Recurse.
process_information_types(infotypes)

# Add a final question that collects all of the infotypes selected using an impute condition.
infotype_questions_actual = [q for q in infotype_questions.values() if q["id"] != "information_types_categories"]
infotype_questions["information_types"] = OrderedDict([
	("id", "information_types"),
	("title", "Which information types does your system contain?"),
	("prompt", "[not used, always imputed]"),
	("type", "multiple-choice"),
	("choices", sum([[{ "key": c["key"], "text": c["text"] } for c in q["choices"]] for q in infotype_questions_actual], [])),
	("impute", [
		OrderedDict([
			("condition", "True"),
			("value-mode", "expression"),
			("value", " + ".join(q["id"] for q in infotype_questions_actual)),
		])
	]),
])

# Add a hidden question for each of confidentiality/integrity/availability that computes the high water
# mark provisional impact level across the selected information types.
# Jinja2 has some limits on the length of an expression, so we chunk some of the tests.
def grouper(iterable, n):
	bucket = []
	for item in iterable:
		bucket.append(item)
		if len(bucket) == n:
			yield bucket
			bucket = []
	if len(bucket) > 0:
		yield bucket
for impact_type in ("confidentiality", "integrity", "availability"):
	def infotypes_for(level):
		infotypes = [
			infotype["code"]
			for infotype in all_info_types
			if impact_type in infotype and infotype[impact_type]["level"] == level
		]
		return grouper(infotypes, 25)
	infotype_questions["information_types_%s_provisional" % impact_type] = OrderedDict([
		("id", "information_types_%s_provisional" % impact_type),
		("title", "What is the provisional %s impact level?" % impact_type),
		("prompt", "[not used, always imputed]"),
		("type", "text"),
		("impute",
			[OrderedDict([
				("condition", " or ".join(("('%s' in information_types)" % code) for code in infotypes)),
				("value", "High"),
			]) for infotypes in infotypes_for("High")]
			+ [OrderedDict([
				("condition", " or ".join(("('%s' in information_types)" % code) for code in infotypes)),
				("value", "Moderate"),
			]) for infotypes in infotypes_for("Moderate")]
			# fallback
			+ [OrderedDict([
				("condition", "True"),
				("value", "Low"),
			])]
		),
	])

# Update the module file in place.
module = rtyaml.load(open("../modules/fisma_level.yaml"))

# Add/replace the information type questions.
for q in infotype_questions.values():
	for q_existing in module["questions"]:
		if q["id"] == q_existing["id"]:
			q_existing.update(q)
			break
	else:
		# Not found - add it.
		module["questions"].append(q)

# For each of confidentiality, integrity, and availability, we have to ask if
# the user wants to downgrade or upgrade from (the high water mark across their
# information types of) the provisional categorization given by NIST 800-60 vol2.
# We insert guidance from the information types the user selected.

for impact_type in ("confidentiality", "integrity", "availability"):
	# Add the provisional impact level and special factors.
	prompt = ""
	for infotype in all_info_types:
		if impact_type not in infotype: continue
		prompt += """{{% if "{code}" in information_types %}}

## {title} ({code})

The provisional {impact_type} impact level of {title} information is **{level}**:

> {explanation}

{special_factors}{{% endif %}}\n""".format(
	impact_type=impact_type,
	code=infotype["code"],
	title=infotype["title"],
	level=infotype[impact_type]["level"],
	explanation=re.sub(r"\s+", " ", infotype[impact_type]["text"]).strip(),
	special_factors=("Examples why you may need to change the level:\n\n> " + re.sub(r"\s+", " ", infotype[impact_type]["special_factors"]).strip() + "\n\n") if infotype[impact_type].get("special_factors") else ""
	)

	# Update question.
	q = [q for q in module["questions"] if q["id"] == "information_types_" + impact_type][0]
	q["prompt"] = re.sub(
		r"{# INFOTYPES #}([\s\S]*?){# END OF INFOTYPES #}\n",
		"{# INFOTYPES #}\n" + prompt + "{# END OF INFOTYPES #}\n",
		q["prompt"])

# Save the module back out.
with open("../modules/fisma_level.yaml", "w") as f:
	f.write(rtyaml.dump(module))

