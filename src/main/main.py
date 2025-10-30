from .jira_client import get_month_issues
from datetime import datetime


def main():

    now = datetime.now()
    year = now.year
    month = now.month
    
    print(f"Fetching issues for {year}-{month:02d}...")
    issues = get_month_issues(year, month)
    
    print(f"\n Found {len(issues)} issues\n")
    
   
    for i, issue in enumerate(issues, 1):
        print(f"\n{i}. [{issue['key']}] {issue['summary']}")
        print(f"   Status: {issue['status']}")
        print(f"   Bank: {issue['bank_name'] or 'N/A'}")
        print(f"   Assignee: {issue['assignee'] or 'Unassigned'}")
        print(f"   Priority: {issue['priority']}")
        print(f"   Created: {issue['created'][:10]}")
        if issue['resolved']:
            print(f"   Resolved: {issue['resolved'][:10]}")
        print(f"   URL: {issue['url']}")
        
       
        if issue.get('description'):
            desc = issue['description'][:200] 
            print(f"\n   Description: {desc}...")
        else:
            print(f"\n   Description: (none)")
        
     
        comments = issue.get('comments', [])
        if comments:
            print(f"\n   Comments ({len(comments)}):")
            for j, comment in enumerate(comments[:3], 1): 
                author = comment.get('author', 'Unknown')
                created = comment.get('created', '')[:10]
                body = comment.get('body', '')[:150]  
                print(f"      {j}. {author} ({created}): {body}...")
            
    
    print(f"Total: {len(issues)} issues")