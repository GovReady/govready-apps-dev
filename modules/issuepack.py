def match_jira_url(url):
    # Was a URL entered in the system name & details module?
    if url is None:
        return None

    # Does the URL look like Jira?
    import re
    m = re.match(r"(?P<baseurl>https://.+.atlassian.net)/projects/(?P<key>[^/]+)", url)
    if not m:
        return None

    # Return the URL components as a dict like
    # { "baseurl": "http://....atlassian.net", "key": "myproject" }
    return m.groupdict()

def create_issue_pack(q, answers):
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
    current_data = answers.get(q['id'])
    current_data_schema = 0
    if isinstance(current_data, dict) \
        and current_data["schema"] == current_data_schema \
        and current_data["status"] == "success" \
        and current_data["project"] == project_info \
        :
        
        # An IssuePack has already been created. Just update status so
        # we can tell user what just happened.
        current_data["log"] = "You already created an IssuePack."
        return current_data

    # Create a new IssuePack by executing an external command, which
    # runs as the same Unix user as the Django process.
    try:
        # TODO: Replace this. Using a subprocess is easy to get wrong
        # and then we have new vulnerabilities.
        import subprocess, os.path
        output = subprocess.check_output([
            'issue-pack',
            '-t=jira',
            '-u=' + answers['jira_username'],
            '-p=' + answers['jira_password'],
            '-k=' + answers['jira_project_key'],
            '-b=' + answers['jira_project_base_uri'],
            os.path.join(os.path.dirname(__file__), 'private-assets', 'au_80053_audit_set1.yaml'),
        ]).decode("utf8")
        status = "success"
    except Exception as e:
        output = "There was an error executing the IssuePack subprocess: " + str(e)
        status = "error"

    return {
        "schema": current_data_schema,
        "status": status,
        "log": output,
        "project": project_info,
    }
