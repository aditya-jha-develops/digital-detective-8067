# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective

Use the command line to navigate, manage text files, compare listing options, join commands with a pipe and inspect the existing package manager.

## 2. Work completed

Ran the operations below in order. All file creation, editing and cleanup took place in the assignment checkout. The final practice folder contains the two-line note and its backup.

## 3. Commands / tools used

| Operation | Command | What it does and what was observed |
| --- | --- | --- |
| Current directory | `pwd` | Printed the path from the filesystem root to the assignment checkout. |
| List contents | `ls` | Printed visible item names, including the mission folders. |
| Detailed list | `ls -l` | Included permissions, link counts, ownership, size and modification time. |
| Change directory | `cd mission-02-terminal`, then `cd ..` | The first command entered the mission folder and the second returned to its parent. |
| Create a directory | `mkdir terminal-practice` | Made a place for the practice files. |
| Create an empty file | `touch notes.txt` | Created a file with zero bytes because the file did not yet exist. |
| Copy a file | `cp notes.txt copy.txt` | Created a second file while keeping the original. |
| Rename a file | `mv copy.txt renamed-copy.txt` | Gave the copy a new name. Its previous name disappeared from the listing. |
| Read a file | `cat notes.txt` | Printed nothing while the file was empty and both lines after it was edited. |
| Write and append | `printf … > notes.txt`, then `printf … >> notes.txt` | Wrote line one and then added line two at the end. |
| Verify a backup | `cp notes.txt backup.txt`, `mv backup.txt notes-backup.txt`, `cmp notes.txt notes-backup.txt` | Copied and renamed the backup. `cmp` exited successfully because the bytes matched. |
| Clean up test files | `rm renamed-copy.txt .listing-example` | Removed the two disposable practice items by their exact names. |
| Inspect Homebrew | `brew --version`, `brew list --formula`, `brew list --cask` | Reported Homebrew 7.0.16 and listed 103 installed formulae and 3 casks. |

## 4. My understanding

`>` opens a file for replacement, so writing again with it clears the previous contents. `>>` adds bytes at the end, which kept the first line intact. `cp` leaves an independent copy. `mv` changes the location or name of the existing item. `pwd` shows the directory commands are currently relative to. `ls` helps check which files are available before changing them.

The plain `ls` listing showed names only. `ls -lah` used `-l` for details, `-a` to include dot-prefixed items such as `.listing-example`, and `-h` to format sizes in readable units. `ls -l | head -n 3` sent the listing to `head` through the pipe. The command on the left produced the lines, and the command on the right kept the first three.

A package manager keeps track of installed software and its dependencies. It can apply updates and remove software through the same interface, which makes it easier to see what is installed and manage it consistently.

## 5. Difficulties faced

A newly created empty file produces no visible output with `cat`, which can look like the command did nothing.

## 6. How I resolved them

Added the two lines and ran `cat` again. Compared the note and its backup with `cmp`.

## 7. Evidence / files

- [Practice note](terminal-practice/notes.txt)
- [Renamed backup](terminal-practice/notes-backup.txt)

## 8. Commit details

**Complete Terminal and file management mission** is the Mission 2 checkpoint on GitHub's `main` branch.
