# Take the NIST Special Publication 800-60 information types,
# as extracted by information_types.py, and construct a
# GovReady Q Module.

from collections import OrderedDict
import rtyaml

information_types = rtyaml.load(open("information_types.yaml"))

questions = []
final_logic = []

def construct_question(information_type, path):
	global questions
	global final_logic

	# General question metadata.
	q = OrderedDict([
		("id", information_type["code"].replace(".", "_").lower()),
		("title", information_type["title"] + " Type"),
		("prompt", information_type["description"]["text"]), # interpreted as Markdown
		("type", "choice"),
		("choices", []),
	])
	questions.append(q)

	# Choices and questions for any subtypes that have their own subtypes.
	for itype in information_type["subtypes"]:
		q["choices"].append({
			"key": itype["code"],
			"text": "%s (%s)" % (itype["title"], itype["code"]),
			"help": itype["description"]["text"],
		})
		subpath = path + [(q["id"], itype["code"])]
		if "subtypes" in itype:
			# This choice leads to other choices.
			construct_question(itype, subpath)
		else:
			# This is a leaf choice.
			final_logic.append((subpath, itype))

	# Skip this question if the user chooses something other than this
	# for the parent. Not applicable for the root question.
	if len(path) > 0:
		q["impute"] = [{
			# condition is a jinja2 template expression
			"condition": "%s != %s" % (path[-1][0], repr(path[-1][1])),
			"value": None,
		}]

root = {
	"code": "root",
	"title": "What Kind of Information Type?",
	"description": { "text": "What kind of information type is this?" },
	"subtypes": information_types,
}
construct_question(root, [])

# Construct a hidden question that computes the final values based on the choices made by the user.
# Since we can't go forward from questions to answer later questions, we have to construct
# a complex list of impute conditions to select values from the information type that the user chose.
def construct_final_logic_question(q, f):
	global questions

	q = OrderedDict(
		(k, q[k])
		for k in ("id", "title", "prompt")
	)

	q["type"] = "text"

	q["impute"] = []
	for path, information_type in final_logic:
		q["impute"].append({
			"condition": " and ".join(
				"%s==%s" % (parent_q, repr(child_value))
				for parent_q, child_value
				in path
			),
			"value": f(information_type),
		})

	questions.append(q)

# These questions are not intended to be answered by the user. They merely
# collect the chosen information type's values through imput conditions.

construct_final_logic_question({
	"id": "name",
	"title": "Information Type Name",
	"prompt": "What is the NIST SP 800-60 Information Type?",
	},
	lambda information_type : information_type["title"])

construct_final_logic_question({
	"id": "identifier",
	"title": "Information Type Identifier",
	"prompt": "What is the identifier of the NIST SP 800-60 Information Type?",
	},
	lambda information_type : information_type["code"])


for key in ("confidentiality", "integrity", "availability"):
	construct_final_logic_question({
		"id": "recommended_classification_%s" % key,
		"title": "Recommended classification for %s" % key,
		"prompt": "What is the recommended %s classification for {{name}}?" % key,
		},
		lambda information_type : information_type.get(key, {}).get("level"))

	# These questions are answered by the user.

	q = OrderedDict([
		("id", "change_classification_%s" % key),
		("title", "Change classification for %s?" % key),
		("prompt", "The recommended %s classification level for **{{name}}** is **{{recommended_classification_%s}}**. Do you want to change it?" % (key, key)),
		("type", "yesno"),
	])
	questions.append(q)

	q = OrderedDict([
		("id", "classification_%s" % key),
		("title", "Classification for %s" % key),
		("prompt", "The recommended %s classification level for **{{name}}** is **{{recommended_classification_%s}}**.\n\nWhat classification level is appropriate for your information system?" % (key, key)),
		("type", "choice"),
		("choices", [
			{
				"key": "Low",
				"text": "Low",
				"help": """The potential impact is low if— 

The loss of confidentiality, integrity, or availability could be expected to have a limited adverse effect on organizational operations, organizational assets, or individuals.  

A limited adverse effect means that, for example, the loss of confidentiality, integrity, or availability might: (i) cause a degradation in mission capability to an extent and duration that the organization is able to perform its primary functions, but the effectiveness of the functions is noticeably reduced; (ii) result in minor damage to organizational assets; (iii) result in minor financial loss; or (iv) result in minor harm to individuals.""",
			},
			{
				"key": "Moderate",
				"text": "Moderate",
				"help": 
"""The potential impact is moderate if— 

The loss of confidentiality, integrity, or availability could be expected to have a serious adverse effect on organizational operations, organizational assets, or individuals.  

A serious adverse effect means that, for example, the loss of confidentiality, integrity, or availability might: (i) cause a significant degradation in mission capability to an extent and duration that the organization is able to perform its primary functions, but the effectiveness of the functions is significantly reduced; (ii) result in significant damage to organizational assets; (iii) result in significant financial loss; or (iv) result in significant harm to individuals that does not involve loss of life or serious life threatening injuries.""",
			},
			{
				"key": "High",
				"text": "High",
				"help": """The potential impact is high if— 

The loss of confidentiality, integrity, or availability could be expected to have a severe or catastrophic adverse effect on organizational operations, organizational assets, or individuals.  

A severe or catastrophic adverse effect means that, for example, the loss of confidentiality, integrity, or availability might: (i) cause a severe degradation in or loss of mission capability to an extent and duration that the organization is not able to perform one or more of its primary functions; (ii) result in major damage to organizational assets; (iii) result in major financial loss; or (iv) result in severe or catastrophic harm to individuals involving loss of life or serious life threatening injuries. """,
			},
		]),
		("impute", [
			{
				"condition": "change_classification_%s == 'no'" % key,
				"value": "recommended_classification_%s" % key,
				"value-mode": "expression",
			}
		])
	])
	questions.append(q)

# Update the module file in place.
module = rtyaml.load(open("../modules/information_type.yaml"))
module["questions"] = questions
with open("../modules/information_type.yaml", "w") as f:
	f.write(rtyaml.dump(module))
