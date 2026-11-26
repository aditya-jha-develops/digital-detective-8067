# Mission 6 — Git and GitHub

## 1. Task / objective

Stage and commit a specific README, inspect commit history, and use a separate branch and a pull request to propose a change.

## 2. Work completed

Checked the assignment repository status, staged this README and inspected the Git history.

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

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

Git history records the staging and branch exercises.

## 8. Commit details

**Record Git staging and command workflow** records the first Git exercise.
