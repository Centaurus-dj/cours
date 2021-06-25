#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system as sys





### Variables
gitlab_link = "https://gitlab.com/CentaurusDJ/import-cours.git"
github_link = "https://github.com/Centaurus-dj/import-cours.git"

auto_commit_txt = """
Auto commit before push on remotes (Github, Gitlab)
"""

### Execution
print("Hello World from Python!")


try:
    sys("git stash && git checkout main")
    sys(f"git pull {gitlab_link}")
    sys(f"git push {gitlab_link} HEAD:main")
    sys("git checkout github-main")
    sys(f"git pull {gitlab_link}")
    sys(f"git push {github_link} HEAD:main")
except Exception as e:
    print(f"During execution, an error occurred:\n\t- {e}")
    exit()