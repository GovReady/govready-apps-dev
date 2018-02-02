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

# Gather data...

# Get the system's hostname.
import socket
hostname = socket.gethostname()

# Form object to push.
payload = {
  "schema": "GovReady Q Project API 1.0",
  "project": {
    "file_server": {
        "hostname": hostname
    }
  }
}

# Identify file to share
scanhtml = "/path/to/scan/file/report.png"

#############################

import json
import requests

# Construct API URL.
api_url = qhost + '/api/v1/organizations/' + organization + '/projects/' + project + '/answers'

# POST the new data.
# r = requests.post(url, files=files, data=values)
# NOTE: In this example, the target upload field is expecting an image
resp = requests.post(
    api_url,
    headers = {"Authorization": api_key},
    files = {"project.file_server.security_groups_evidence_screenshot":(scanhtml,"rb")} )
 
print(resp.text)

# GET the current data.
print("\nCurrent information for {}\n".format(api_url))

print(json.dumps(requests.get(api_url,
    headers={ "Authorization": api_key },
).json(), indent=2))
