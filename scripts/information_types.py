# Extracts information types from NIST Special Publication 800-60 Volume II
# Revision 1: Appendices to Guide for Mapping Types of Information and Information
# Systems to Security Categories.
#
# Before running this script, acquire the PDF and convert it to text:
#
# $ wget -O SP800-60v2r1.pdf http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-60v2r1.pdf
# $	pdftotext SP800-60v2r1.pdf
#
# Then run this script:
#
# python3 information_types.py SP800-60v2r1.txt > information_types.yaml

from collections import OrderedDict
import sys
import re
import rtyaml

text = open(sys.argv[1]).read()

# Chop off start and end.

i = text.find("C.2 Rationale and Factors for Services Delivery Support Information\nServices")
text = text[i:]

i = text.find("[This Page Intentionally Left Blank]\n\n231")
text = text[:i]

# Remove page numbers and the subsequent form feed character page delimiters.
# TODO: Unfortunately it's hard to identify footnotes. Maybe we can do that
# manually.

text = re.sub(r"\s*\d+\s*\x0c", "\n", text)

# Remove tables that break parsing.

text = re.sub(r"Table D-1: [\w\W]*?Civilian Operations", "", text)
text = re.sub(r"Table D-2: [\w\W]*?(\nD.1 Defense and National Security)", r"\1", text)

# Parse content - split up the text by information type.

# transition matrix between expected headings so we can parse strictly.
TM = { "description": "Confidentiality", "confidentiality": "Integrity", "integrity": "Availability" }

information_types = []
parse_mode = None

for line in text.split("\n"):
	# Look for a line that starts a new information type.
	m = re.match(r"(?P<code>[CD][\.0-9]+)\s(?P<title>.*)", line)
	if m:
		information_types.append(OrderedDict([
			("code", m.group("code")),
			("title", re.sub(" Information Type$|^Rationale and Factors for ", "", m.group("title"))),
			("description", { "text": "" }),
		]))
		parse_mode = "description"
		security_category = None
		continue

	# Look for the Security Category. There are footnotes in these lines.
	# In one case there is a typo and a paren is missing. We don't omit
	# this line from the description text because the text before it
	# often ends with a colon, i.e. the text content really does include
	# this line for the user to read.
	m = re.match(r"Security Category = \{\(confidentiality, (?P<confidentiality>Low|Moderate|High|N/A)(\s*(?P<confidentiality_footnote>\d+)\s*)?\), \(integrity, (?P<integrity>Low|Moderate|High|N/A)(\s*(?P<integrity_footnote>\d+)\s*)?\)?, \(availability, (?P<availability>Low|Moderate|High|N/A)(\s*(?P<availability_footnote>\d+)\s*)?\)\}$", line)
	if m:
		security_category = m.groupdict()

	# Look for a second-level heading. There is a strict order of headings. So we are testing
	# for a heading line that is known to be the next heading, given where we are.
	if parse_mode in TM and line.strip() == TM[parse_mode]:
		if not security_category: raise ValueError(information_types[-1])
		parse_mode = line.strip().lower()
		information_types[-1][parse_mode] = { "text": "", "level": security_category[parse_mode] }
		continue

	# This line of text continues the last recognized information type.
	information_types[-1][parse_mode]["text"] += line + "\n"

# Clean up text.

for information_type in information_types:
	for key in information_type:
		if isinstance(information_type[key], dict):
			if "text" in information_type[key]:
				text = information_type[key]["text"]

				# Remove leading spaces and trailing spaces besides a final newline.
				text = text.strip() + "\n"

				# Remove nonsignificant line breaks. Look for line breaks before words
				# that would have exceeded a column limit. This works reasonably well
				# but doesn't seem quite right. Something in the logic here isn't right.
				def line_break_remover(m):
					next_word = re.compile(r"\S+").search(text, m.end())
					keep_newline = not next_word or (len(m.group(1) + next_word.group(0)) < 90)
					return m.group(1) + ("\n" if keep_newline else " ")
				text = re.sub(r"(.*)\n", line_break_remover, text)

				information_type[key]["text"] = text

# Group subsections under sections.

# Make a mapping from codes to the dicts that hold metadata on that information type.
section_by_code = {
	information_type["code"]: information_type
	for information_type in information_types
}

# Add sections into their parents.
can_remove = set()
for information_type in information_types:
	parent_code = ".".join(information_type["code"].split(".")[:-1])
	if parent_code in section_by_code:
		assert "confidentiality" not in section_by_code[parent_code]
		can_remove.add(information_type["code"])
		section_by_code[parent_code].setdefault("subtypes", []).append(information_type)

# Remove the sections that got associated with parents from the main list.
information_types = list(filter(lambda information_type : information_type["code"] not in can_remove, information_types))

print(rtyaml.dump(information_types))