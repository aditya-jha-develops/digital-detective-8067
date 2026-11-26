# Mission 6 — Git and GitHub

## 1. Task / objective

Stage and commit a specific README, inspect commit history, and use a separate branch and a pull request to propose a change.

## 2. Work completed

Checked the assignment repository status, staged this README and inspected the Git history. Created and published `update-about` with a separate root README change. Opened [pull request #1](https://github.com/aditya-jha-develops/digital-detective-8067/pull/1) into `main` and reviewed its one-file diff. The pull request remains open, as the merge is conditional on the instructor's direction. Returned to the local `main` branch.

## 3. Commands / tools used

| Git operation | What it does |
| --- | --- |
| `git init -b main` | Starts version history in the current project and gives its first branch the name `main`. |
| `git status --short --branch` | Shows the current branch and which files are staged, changed or untracked. |
| `git add <file>` | Places that file's current version in the staging area. |
| `git commit -m "message"` | Records the staged changes in the repository with a message. |
| `git log --oneline -5` | Displays the latest five commit abbreviations and messages. |
| `git branch --list` | Lists the local branches. |
| `git switch -c update-about origin/main` | Creates a branch from the published main checkpoint and switches to it. |
| `git switch main` | Changes the checkout back to the local main branch. |
| `git push` | Publishes commits and updates the corresponding remote branch. |
| `git fetch origin` | Retrieves remote history and updates remote-tracking references. |
| `git pull --ff-only` | Retrieves updates and moves the current branch forward if it can do so without a merge. |

## 4. My understanding

Staging selects the exact file changes for the next snapshot. Committing records those staged changes as a new point in the local history. A branch is a movable pointer to a commit, so work on a proposal can advance separately from the main branch. A pull request compares a branch with its target and gives collaborators a place to review the difference before deciding whether to merge it.

## 5. Difficulties faced

A branch created from `origin/main` initially tracked `origin/main`, even though the new branch needed its own remote branch.

## 6. How I resolved them

Removed the inherited tracking setting with `git branch --unset-upstream update-about`. Published `update-about` and checked that it now tracks `origin/update-about`.

## 7. Evidence / files

The [learning branch](https://github.com/aditya-jha-develops/digital-detective-8067/tree/update-about) contains the `My Learning` change. The [pull request diff](https://github.com/aditya-jha-develops/digital-detective-8067/pull/1/changes) shows the single changed file, the root README.

## 8. Commit details

**Record Git staging and command workflow** records the first Git exercise on `main`. **Add My Learning section to the project README** was pushed on `update-about`. **Complete Git and GitHub collaboration mission** is the Mission 6 checkpoint on GitHub's `main` branch.
