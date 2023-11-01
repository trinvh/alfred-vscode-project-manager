import json
import sys
import os

# read file
filePath = os.path.join(os.path.expanduser(
    '~'), 'Library/Application Support/Code/User/globalStorage/alefragnani.project-manager/projects_cache_git.json')

with open(filePath, 'r') as file:
    data = file.read()

# parse file
projects = json.loads(data)

# sort
projects = sorted(projects, key=lambda k: k['name'])
items = []
for project in projects:
    item = {
        "title": project['name'],
        "arg": project['fullPath']
    }
    if sys.argv[1]:
        if sys.argv[1].lower() in project['name'].lower():
            items.append(item)
    else:
        items.append(item)

result = {
    "items": items
}

output = json.dumps(result)
print(output)

sys.exit(0)
