# Generate task yaml stubs based on content inside a project yaml file
#
# Usage:
# cd scripts
# python3 maketaskstubs.py
# 
# 

from collections import OrderedDict
import rtyaml

project_yaml_file = "../modules/_transparency.yaml"

questions = []
qcount = 0
report_tables = []


# Create project object from project yaml file
project = rtyaml.load(open(project_yaml_file))

# print(project)

# Write each task yaml file
def make_task_stub(yaml_file, task):
    with open(yaml_file, "w") as f:
        f.write(rtyaml.dump(task))

# Loop through tasks
for task in project["questions"]:

    # prepare task object
    filename = "../modules/{}.yaml".format(task["module-id"])
    print("preparing {}".format(filename))
    task = OrderedDict([
        ("id", task["module-id"]),
        ("title", task["title"]),
        ("introduction", {
            "format": "markdown",
            "template": "{}".format(task["title"]),
        }),
        ("questions", [{"id": "q1", "title": "TITLE", "prompt": "PROMPT", "type": "text"}]),
        ("output", [{
            "title": task["title"],
            "format": "markdown",
            "template": "{}".format(task["title"]),
            }]),
    ])

    make_task_stub(filename, task)

