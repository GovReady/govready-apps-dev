def create_issue_pack(q, answers):
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
        import subprocess
        output = subprocess.check_output([
            'issue-pack',
            '-t=jira',
            '-u=' + answers['jira_username'],
            '-p=' + answers['jira_password'],
            '-k=' + answers['jira_project_key'],
            '-b=' + answers['jira_project_base_uri'],
            '/codedata/code/Issue-Packs/examples/au_80053_audit_set1.yaml',
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
