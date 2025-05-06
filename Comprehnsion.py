team_members = [
    {"name": "Alice", "role": "Frontend Developer"},
    {"name": "Bob", "role": "Backend Developer"},
    {"name": "Carol", "role": "Project Manager"},
    {"name": "Dave", "role": "QA Engineer"}
]
 
tasks = [
    {"title": "Build login page", "priority": "High", "tags": ["frontend"], "status": "In Progress", "assignee": "Alice"},
    {"title": "Set up database", "priority": "Medium", "tags": ["backend"], "status": "Done", "assignee": "Bob"},
    {"title": "Write test cases", "priority": "High", "tags": ["qa", "backend"], "status": "In Review", "assignee": "Dave"},
    {"title": "Project plan creation", "priority": "Low", "tags": ["planning"], "status": "To Do", "assignee": "Carol"},
    {"title": "Fix navbar bug", "priority": "High", "tags": ["frontend", "bug"], "status": "To Do", "assignee": "Alice"},
    {"title": "API authentication", "priority": "Medium", "tags": ["backend", "security"], "status": "In Progress", "assignee": "Bob"}
]

def Print_member(team_members):
    for i in team_members:
        print(f"Name: {i['name']}, Role: {i['role']}")
Print_member(team_members)


def high_priority(tasks):
    priority_count = len([task for task in tasks if task["priority"].lower() == "high"])
    print(priority_count)
high_priority(tasks)


def frontend_tag():
    frontendTag= [task["title"] for task in tasks if "frontend" in task["tags"]]
    print(frontendTag)
frontend_tag()


status_count = {}
for task in tasks:
    status = task["status"]
    if status in status_count:
        status_count[status] += 1
    else:
        status_count[status] = 1
print(status_count)



def get_tasks_for_member(tasks, member_name):
    return [task for task in tasks if task["assignee"].lower() == member_name.lower()]

for member in team_members:
    name = member["name"]
    titles = [task["title"] for task in tasks if task["assignee"] == name]
    print(f"\nTasks for {name}:")
    for title in titles:
        print(f"- {title}")