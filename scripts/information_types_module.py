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
		("title", information_type["title"]),
		("prompt", None), # set below
		("type", "choice"),
		("choices", []),
	])
	questions.append(q)

	# Choices and questions for any subtypes that have their own subtypes.
	has_leaf = False
	has_branch = False
	for itype in information_type["subtypes"]:
		# Append the choice.
		choice = OrderedDict([
			("key", itype["code"]),
			("text", "%s (%s %s)" % (
				itype["title"],
				"Category" if "subtypes" in itype else "Information Type",
				itype["code"])),
			("help", itype["description"]["text"]),
		])
		q["choices"].append(choice)

		# Add this answer to the 'path' passed to the next recursive call.
		subpath = path + [(q["id"], choice["key"])]

		# Do we go recursively?
		if "subtypes" in itype:
			# This choice leads to other choices. Construct the questions
			# for the subtypes.
			construct_question(itype, subpath)
			has_branch = True
		else:
			# This is a leaf choice.
			final_logic.append((subpath, itype))
			has_leaf = True

	# Set the prompt.
	if len(path) == 0: # root
		q["prompt"] = "What category of information type best describes the information you have in mind?"
	elif has_leaf and has_branch:
		q["prompt"] = "What information type or category within %s best describes the information you have in mind?" % information_type["title"]
	elif has_branch:
		q["prompt"] = "What category of information type within %s best describes the information you have in mind?" % information_type["title"]
	else:
		q["prompt"] = "Which information type within %s best describes the information you have in mind?" % information_type["title"]

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

# Construct a hidden question that houses the metadata about the information type selected by the user.
# We use a long list of impute conditions to determine which information type the user selected, and
# then the impute condition that matched yields a raw YAML/Python data structure with metadata about
# the information type.
metadata_q = OrderedDict([
	("id", "selected_information_type"),
	("title", "Selected Information Type"),
	("prompt", None), # not used
	("type", "raw"), # not really supported but flags that the answer value is a raw Python data structure
	("impute", []),
])
questions.append(metadata_q)
for path, information_type in final_logic:
	metadata_q["impute"].append({
		# the impute condition tests that the user made a certain set of choices down the
		# hierarchy of information type categories to a particular information type
		"condition": " and ".join(
			"%s==%s" % (parent_q, repr(child_value))
			for parent_q, child_value
			in path
		),

		# and then if so, yields a dict of information about that information type
		# -- in fact, the original information type data structure that we parsed
		# in the other script
		"value": information_type,
	})

# Now add three more pairs of questions for the user to override the recommended
# classification levels.
for key in ("confidentiality", "integrity", "availability"):
	q = OrderedDict([
		("id", "keep_classification_%s" % key),
		("title", "Keep classification for %s?" % key),
		("prompt", """The recommended **%s** classification level for {{selected_information_type.title}} is **{{selected_information_type.%s.level}}**.

[NIST Special Publication 800-60 Volume II](http://csrc.nist.gov/publications/nistpubs/800-60-rev1/SP800-60_Vol2-Rev1.pdf) explains:

> {{selected_information_type.%s.text}}

Is this classification level appropriate for your information system?"""
		 % (key, key, key)),
		("type", "yesno"),
	])
	questions.append(q)

	q = OrderedDict([
		("id", "classification_%s" % key),
		("title", "Classification for %s" % key),
		("prompt", "You said you wanted to change the **%s** classification level for {{selected_information_type.title}} from its recommended level **{{selected_information_type.%s.level}}**.\n\nWhat classification level is appropriate for the information system?" % (key, key)),
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
				"condition": "keep_classification_%s == 'yes'" % key,
				"value": "selected_information_type.%s.level" % key,
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
