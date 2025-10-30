from __future__ import annotations
from atlassian import Jira
import os
from dotenv import load_dotenv
from .timeutils import month_range
from datetime import date


load_dotenv()


JIRA_URL = os.environ["JIRA_URL"]
JIRA_USER = os.environ["JIRA_EMAIL"]
JIRA_TOKEN = os.environ["JIRA_API_TOKEN"]
PROJECT_KEY = os.getenv("PROJECT_KEY") 

_jira = Jira(url=JIRA_URL, username=JIRA_USER, password=JIRA_TOKEN, cloud=True)

def jql_for_month(year: int, month: int) -> str:
    start, end = month_range(year, month)
    
    start_str = start.strftime("%Y-%m-%d")
    end_str = end.strftime("%Y-%m-%d")
    clauses = [
        f'created >= "{start_str}"',
        f'created <= "{end_str}"',
    ]
    if PROJECT_KEY:
        clauses.append(f'project = {PROJECT_KEY}')
    return " AND ".join(clauses) + " ORDER BY priority DESC"

def get_month_issues(year: int, month: int, limit: int = 500):
    jql = jql_for_month(year, month)
    data = _jira.jql(jql, limit=limit)
    issues = []
    if not data:
        return issues
    for it in data.get("issues", []):
        f = it.get("fields", {})
        issue_key = it.get("key")
        
        
        comments = []
        try:
            comments_data = _jira.issue_get_comments(issue_key)
            if comments_data:
                for comment in comments_data.get("comments", []):
                    comments.append({
                        "author": comment.get("author", {}).get("displayName"),
                        "created": comment.get("created"),
                        "body": comment.get("body"),
                    })
        except Exception as e:
            print(f"Warning: Could not fetch comments for {issue_key}: {e}")


        issues.append({
            "key": issue_key,
            "url": f"{JIRA_URL}/browse/{issue_key}",
            "summary": f.get("summary"),
            "time_to_first_response": f.get("customfield_10072"),
            "description": f.get("description"),  
            "status": (f.get("status") or {}).get("name"),
            "assignee": (f.get("assignee") or {}).get("displayName"),
            "priority": (f.get("priority") or {}).get("name"),
            "created": f.get("created"),
            "resolved": f.get("resolutiondate"),
            "labels": f.get("labels") or [],
            
            "comments": comments, 
        })

        if PROJECT_KEY == "AMFM":
            issues[-1]["bank_name"] = f.get("customfield_10074")

    return issues

def test_connection() -> bool:
    try:
        _jira.myself()
        print("JIRA connection successful")
        return True
    except Exception as e:
        print(f"JIRA connection test failed: {e}")
        return False