from datetime import datetime, timezone
import json
import os

from jira import get_issues, JIRA_DOMAIN
from glitchtip import get_issue, GLITCHTIP_DATE_FORMAT, \
    get_issues as glitchtip_issues, GLITCHTIP_DOMAIN


DEFAULT_MAX_DAYS_OF_INACTIVITY = 7
MAX_DAYS_OF_INACTIVITY = int(os.environ.get(
    "MAX_DAYS_OF_INACTIVITY",
    DEFAULT_MAX_DAYS_OF_INACTIVITY))

TEMPLATE = """# Glitchtip <-> Jira integration checker

## Open Jira issues for Glitchtip events
```json:table
{}
```

## Glitchtip events with no Jira issues
```json:table
{}
```
"""


def get_last_seen_in_days(issue):
    try:
        last_seen = datetime.strptime(issue["lastSeen"], GLITCHTIP_DATE_FORMAT)
    except KeyError:
        return None

    diff = datetime.now(timezone.utc) - last_seen
    return diff.days


def get_jira_issues_with_last_seen_older_than(max_days_of_inactivity: int):
    """
    This function retrieves all Jira issues with Glitchtip last seen date
    greater than .
    """
    data = get_issues()

    out = {"issues": []}
    for issue in data["issues"]:
        glitchtip_url = None
        for label in issue["fields"]["labels"]:
            if "https://glitchtip.devshift.net" in label:
                glitchtip_url = label
                break
        issue_data = get_issue(glitchtip_url.split("/")[-1])

        last_seen_in_days = get_last_seen_in_days(issue_data)
        if last_seen_in_days is not None:
            if last_seen_in_days < max_days_of_inactivity:
                continue
        
        issue["glitchtip_url"] = glitchtip_url
        issue["last_seen_in_days"] = last_seen_in_days
        
        out["issues"].append(issue)

    return out

def format_issues(data):
    out = {
        "fields": [
            {"key": "issue_url", "label": "Jira"},
            {"key": "glitchtip_url", "label": "Glitchtip"},
            {"key": "diff", "label": "Days since last event"}
        ],
        "items": [],
        "filter": True
    }

    for issue in data["issues"]:
        out["items"].append(
            {
                "issue_url": f"https://{JIRA_DOMAIN}/browse/{issue['key']}",
                "glitchtip_url": issue["glitchtip_url"],
                "diff": issue["last_seen_in_days"]
            }
        )
    return out



def get_glitchtip_issues_with_no_jira(max_days_of_inactivity: int):
    out = {
        "fields": [
            {"key": "glitchtip_url", "label": "Glitchtip"},
            {"key": "diff", "label": "Days since last event"}
        ],
        "items": [],
        "filter": True
    }
    issues = glitchtip_issues()
    for issue in issues:
        last_seen_in_days = get_last_seen_in_days(issue)
        if last_seen_in_days >= max_days_of_inactivity:
            continue
        glitchtip_url = f"https://{GLITCHTIP_DOMAIN}/ccx/issues/{issue['id']}"
        jira_issues = get_issues(
            f'project = CCXDEV AND labels = "{glitchtip_url}" AND status != CLOSED')
        if len(jira_issues["issues"]) == 0:
            out["items"].append(
                {
                    "glitchtip_url": glitchtip_url,
                    "diff": last_seen_in_days
                })
    return out


if __name__ == "__main__":
    jira_issues_with_last_seen = get_jira_issues_with_last_seen_older_than(
        MAX_DAYS_OF_INACTIVITY)

    print(
        TEMPLATE.format(
            json.dumps(
                format_issues(jira_issues_with_last_seen),
                sort_keys=False,
                indent=4,
                separators=(',', ': ')
            ),
            json.dumps(
                get_glitchtip_issues_with_no_jira(MAX_DAYS_OF_INACTIVITY),
                sort_keys=False,
                indent=4,
                separators=(',', ': ')
            ),
        )
    )
