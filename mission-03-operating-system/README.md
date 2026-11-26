# Mission 3 — Understand the operating system

## 1. Task / objective

Inspect the operating system, account, storage, running processes, file paths and permissions. Explain how the operating system manages the computer.

## 2. Work completed

Collected a privacy-safe system snapshot and inspected the Terminal practice note. Opened Activity Monitor while Brave was running to compare application and helper processes.

| Information | What it tells you | Observation |
| --- | --- | --- |
| Operating system | The system and CPU architecture the programs are running on. | macOS 27.2.1, arm64 |
| Current account | The account under which the shell is running. | [redacted] |
| Storage | The occupied and available space on the volume containing the repository. | `df -h .` showed 298 GiB used and 136 GiB available. |
| System activity | A snapshot of how much work the system had on average over recent intervals. | `uptime` showed load averages of 8.33, 8.25 and 7.02 for 1, 5 and 15 minutes. |

## 3. Commands / tools used

- `sw_vers` displayed the macOS version and `uname -m` reported the architecture.
- `whoami` showed the active account. The value was removed from the report.
- `df -h .` reported storage for the volume containing the current folder.
- `uptime` displayed system activity averages.
- `ps -axo pid,comm` was attempted from the task shell. Activity Monitor showed the process list and the PID column.
- `pwd` and `cd` showed the path change. `ls -l` displayed the note's mode and size.

## 4. My understanding

A process is an active instance of a program. The operating system gives it a process identifier, or PID, for as long as it runs. Activity Monitor showed Brave Browser and a separate Brave Browser Helper process. A browser can split rendering and other work across processes with different PIDs.

An absolute path starts at the filesystem root, such as `/Users/[redacted]/…/digital-detective-8067/mission-03-operating-system`. A relative path starts from the active folder, such as `mission-03-operating-system/README.md` when the terminal is at the repository root. Entering the mission folder appended its name to the path shown by `pwd`.

The practice note showed `-rw-r--r--@`. The owner's three permissions are `rw-`, so the owner can read and edit the note. Direct execution is disabled. The last `@` is a macOS marker for extended attributes.

| Permission | Meaning | Example |
| --- | --- | --- |
| `r` | Read a file's contents. | Display a note with `cat`. |
| `w` | Change a file's contents. | Append another line to a note. |
| `x` | Run an executable file or traverse a directory. | Run an executable script or enter a folder. |

| OS responsibility | Explanation | Example |
| --- | --- | --- |
| Process management | Schedules work from active programs on the CPU. | Lets a browser and editor run together. |
| Memory management | Allocates memory and keeps one process from reading another process's private memory directly. | Gives the editor memory while it opens a file. |
| Device management | Provides interfaces for software to use hardware. | Routes keyboard events to the active app. |
| File management | Maintains names, directories and file contents on storage. | Finds a README when it is opened by path. |
| User interface / shell | Provides ways to issue commands and interact with running apps. | Finder opens a folder, and the shell changes into it with `cd`. |
| Security and permissions | Checks whether an account or process can use a resource. | Permits the owner to edit the practice note. |

## 5. Difficulties faced

The task shell returned an operation-permission error for the process-list command.

## 6. How I resolved them

Used Activity Monitor's CPU view to find the PID column and observe Brave and its helper process.

## 7. Evidence / files

The system snapshot is recorded above. The [Terminal practice note](../mission-02-terminal/terminal-practice/notes.txt) was the file used for the mode check.

## 8. Commit details

**Document operating system and file management** is the Mission 3 checkpoint on GitHub's `main` branch.
