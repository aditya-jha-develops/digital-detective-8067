# Mission 4 — How programs run

## 1. Task / objective

Run a one-line Python program and compare a compiler with an interpreter.

## 2. Work completed

Created `hello.py` with one `print()` call. Ran it from its folder and observed the expected output.

```text
Hello from Python
```

## 3. Commands / tools used

- `python3 hello.py` ran the source file with Python 3.
- `print()` wrote the message to standard output.

## 4. My understanding

| Point | Compiler | Interpreter |
| --- | --- | --- |
| When translation or execution happens | Translates a program or unit of code before that code executes. | Carries out instructions while the program runs. |
| Typical output | An object file, executable or another representation of the program. | Effects of execution, such as text on the screen or a returned value. |
| Example | Clang can compile a C program to a native executable. | CPython executes Python bytecode. |
| Advantage | Can optimise a program before it runs and produce a reusable binary. | Offers a short edit-and-run loop during development. |

A compiler translates source into a different representation before that code executes. An interpreter runs instructions and produces the program's effects at runtime. CPython combines both ideas by compiling source to bytecode and then interpreting the bytecode in its virtual machine. Running `python3 hello.py` made that process visible as the printed greeting.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

[hello.py](hello.py) contains the exact program. Its output is recorded above.

## 8. Commit details

**Compare compilers and interpreters** is the Mission 4 checkpoint on GitHub's `main` branch.
