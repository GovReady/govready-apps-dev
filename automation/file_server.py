# GovReady Automation Example
#############################

# This Python script demonstrates how to automatically push information
# gathered from a live system to a GovReady Q Compliance App.
#
# This script can push data to any app that satisfies the protocol
# named `govready.com/apps/compliance/2017/file-server`, such as the
# macOS File Server app.

########################################################################

# Configuration.

qhost = 'http://localhost:8000'
organization = 'test'
project = '47'
api_key = '.....'

motd_filenames = ["/etc/issue", "/etc/motd", "/run/motd.dynamic"]

# Gather data...

# Get the system's hostname.
import socket
hostname = socket.gethostname()

# Get login messages from various files likely to be used
# by the system in a login message. Concatenate the files.
# Wrap each in ```...``` because the Q question type treats
# its answer as Markdown.
import os.path
login_message = ""
for filename in motd_filenames:
    if os.path.exists(filename):
        login_message += \
           filename \
         + ":\n\n```" \
         + open(filename).read().strip().replace("```", "` ` `") \
         + "```\n\n"

# Get a list of UNIX users excluding users who cannot login
# since they are probably system users, and primary group
# membership.
users = set()
groups = dict()
for line in open("/etc/passwd"):
    username, _, uid, gid, fullname, homedir, shell = line.rstrip().split(":")
    if shell in ("/bin/false", "/usr/sbin/nologin"): continue
    users.add(username)
    gid = int(gid)
    if gid not in groups: groups[gid] = { "name": None, "users": set() }
    groups[gid]["users"].add(username)

# Get a list of UNIX groups and the non-system users within them.
for line in open("/etc/group"):
    groupname, _, gid, users = line.rstrip().split(":")
    gid = int(gid)
    for user in users.split(","):
        if user != "":
            if gid not in groups: groups[gid] = { "name": None, "users": set() }
            groups[gid]["users"].add(user)
    if gid in groups: groups[gid]["name"] = groupname

# Describe the groups.
security_groups_description = "There are %d UNIX groups: %s" % (
        len(groups),
        ", ".join(sorted(
            "`%s` (%d user%s: %s)" % (
                group["name"],
                len(group["users"]),
                "s" if len(group["users"]) != 1 else "", # plural 's'
                ", ".join("`%s`" % u for u in group["users"])
            )
            for group in groups.values()
        ))
    )

# Form object to push.
payload = {
  "schema": "GovReady Q Project API 1.0",
  "project": {
    "file_server": {
        "hostname": hostname,
        "login_message": login_message,
        "using_security_groups": "yes",
        "security_groups_description": security_groups_description,
    }
  }
}

#############################

import json
import requests

# Construct API URL.
api_url = qhost + '/api/v1/organizations/' + organization + '/projects/' + project + '/answers'

# POST the new data.
resp = requests.post(
    api_url,
    headers={
        "Authorization": api_key,
        "Content-Type": "application/json" },
    data=json.dumps(payload))
print(resp.text)

# GET the current data.
print(json.dumps(requests.get(api_url,
    headers={ "Authorization": api_key },
).json(), indent=2))
