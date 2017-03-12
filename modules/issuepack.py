def match_jira_url(url):
    # Was a URL entered in the system name & details module?
    if not isinstance(url, str):
        return None

    # Does the URL look like Jira?
    import re
    m = re.match(r"(?P<baseurl>https://.+.atlassian.net)/projects/(?P<key>[^/]+)", url)
    if not m:
        return None

    # Return the URL components as a dict like
    # { "baseurl": "http://....atlassian.net", "key": "myproject" }
    return m.groupdict()

def create_issue_pack_func(module, question, answers, project_name, project_url, **kwargs):
    for field in ('jira_username', 'jira_password', 'jira_project_key', 'jira_project_base_uri'):
        if answers[field] is None:
            raise ValueError("One of the preceding questions was skipped or your Jira password needs to be re-entered.")

    # Pull out the project info that we'll save in the database
    # (not user credentials). If the user re-submits this question,
    # and if the project info has changed, then we'll forget the
    # previous IssuePack created and create a new one.
    project_info = {
        "type": "jira",
        "base_uri": answers['jira_project_base_uri'],
        "project_key": answers['jira_project_key'],
    }

    # Get the last value we set as the answer to this question so we
    # can see if we've already created an IssuePack for this project.
    # If so, don't do it again, since the user probably doesn't want
    # duplicates.
    current_data = answers.get(question['id'])
    current_data_schema = 1
    if isinstance(current_data, dict) \
        and current_data["schema"] == current_data_schema \
        and current_data["status"] == "success" \
        and current_data["project"] == project_info \
        :
        
        # An IssuePack has already been created. Just update status so
        # we can tell user what just happened.
        current_data["log"] = ["You already created an IssuePack."]
        return current_data

    # Open the IssuePack YAML files and concatenate into a single YAML file.
    issuepack = {
        "milestone": "Milestone", # not used
        "issues": module["issuepack_issues"],
    }

    # Do string substitution on the issue text fields.
    for story in issuepack["issues"]:
        for field in ('title', 'body'):
            story[field] = story.get(field, "")\
                .replace("{{project_name}}", project_name)\
                .replace("{{project_url}}", project_url)

    # Form the answer data structure.
    answer = {
        "schema": current_data_schema,
        "project": project_info,
        "status": "error",
    }

    # Create a new IssuePack by executing an external command, which
    # runs as the same Unix user as the Django process.
    import json, rtyaml
    try:
        # TODO: Replace this. Using a subprocess is easy to get wrong
        # and then we have new vulnerabilities.
        import subprocess
        output = subprocess.check_output([
            'issue-pack',
            '-t=jira',
            '-u=' + answers['jira_username'],
            '-p=' + answers['jira_password'],
            '-k=' + answers['jira_project_key'],
            '-b=' + answers['jira_project_base_uri'],
            '--json',
            '/proc/self/fd/0', # STDIN
            ],
            input=rtyaml.dump(issuepack).encode("utf8")
        ).decode("utf8")
        
        try:
            answer.update(json.loads(output))
            if len(answer['issues']) > 0:
                answer["status"] = "success"
        except ValueError:
            answer["log"] = ["Invalid Issue Packs output: " + output]

    except Exception as e:
        answer["log"] = ["There was an error executing the IssuePack subprocess: " + str(e)]

    return answer
