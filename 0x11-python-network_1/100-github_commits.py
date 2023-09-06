#!/usr/bin/python3
"""
Python script that uses the GITHUB_API and
shows the last 10 commits of a repository in GitHub
displaying it in the format: `<sha>: <author name>`
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    repo = sys.argv[1]
    repo_owner = sys.argv[2]
    url = "https://api.github.com/repos/{:s}/{:s}/commits".format(
        repo_owner, repo)
    res = requests.get(url)
    commits = res.json()
    for commit in commits[:10]:
        git_sha = commit.get('sha')
        git_name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(git_sha, git_name))
