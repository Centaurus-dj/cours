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

sys("git add .")
sys(f"git commit {auto_commit_txt}")

try:
    sys(f"git push {gitlab_link}")
except Exception as e:
    print(f"During push to Gitlab, an error occurred:\n\t- {e}")
    exit()

try:
    sys("git checkout github-main")
except Exception as e:
    print(f"During checkout, an error occurred:\n\t- {e}")
    exit()

try:
    sys(f"git pull {gitlab_link}")
    sys(f"git push {github_link}")
except Exception as e:
    print(f"During pull then push, an error occurred:\n\t- {e}")
    exit()
