# Requirements: pip install python-gitlab
#
# Environment variables:
#   GITLAB_URL: The URL of the Gitlab instance to use.
#   GITLAB_PRIVATE_TOKEN: Your Personal Access Token
#
# Usage:
#   export GITLAB_URL=https://gitlab.example.com
#   export GITLAB_PRIVATE_TOKEN=Zaq1Xsw2Cde3Vfr4Bgt5
#   python gitlab_dump_all_trees.py file_with_all_trees.txt

import gitlab
import os
import sys

if len(sys.argv) < 2:
    print("Path to out file expected")
    exit(1)

open(sys.argv[1], 'w').close()

def printLog(*args, **kwargs):
    print(*args, **kwargs)
    with open(sys.argv[1], 'a') as file:
        print(*args, **kwargs, file=file)

gl = gitlab.Gitlab(url=os.environ['GITLAB_URL'], private_token=os.environ['GITLAB_PRIVATE_TOKEN'])

gl.auth()

projects = gl.projects.list(iterator=True)
for project in projects:
    try:
        repository_tree = project.repository_tree(recursive=True, iterator=True)
        branches = project.branches.list(iterator=True)
        branch_name = ''
        for branch in branches:
            if branch.default:
                branch_name = branch.name
                break
    except:
        continue
    for node in repository_tree:
        if node['type'] == 'tree': continue
        printLog(f"{project.path_with_namespace}/-/blob/{branch_name}/{node['path']}")
