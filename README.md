# Clean Python Workshop

Welcome to practice examples for the **Clean Python Workshop**!

I encourage you to challenge yourself and avoid peeking at the solution files (marked with `_clean`). ;)

---

## Environment

To participate in this workshop, you need **Python** installed on your system. The required version is:

```
python = "^3.12"
```

Dependencies are managed with **Poetry**, a dependency management tool for Python projects. The following dependencies are needed for the workshop:

```
scikit-learn = "^1.6.1"
pandas = "^2.2.3"
```

### Setting Up the Environment

> **Note:** While it is recommended, you do not _need_ to activate a Poetry environment for this workshop. All code will run using your system's Python environment or the global Poetry-managed environment, as long as the dependencies are installed.


1. Install Python (ensure it is version 3.12 or higher).
2. Install Poetry by running:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
   Alternatively, check the [official Poetry installation guide](https://python-poetry.org/docs/#installation) for platform-specific instructions.
3. Navigate to the project directory and install dependencies:
   ```bash
   poetry install
   ```
4. Make sure that you run the code using the correct interpreter. 
5. You may test if your env is set up correctly by running test_environment.py
---



**I recommend making sure that you can debug (i.e. step through) the code examples, it will help a lot if you're able to inspect variables**

## Session 1: Names, Comments, and Functions

In the first session, you'll work on improving Python code by focusing on naming conventions, comments, and functions. The session aims to:

- **Naming:** Replace the horrible, horrible names with good names!
- **Comments:** Remove as many comments as possible through choosing better names or extracting code into functions.
- **Functions:** Break up large functions, find better names, thinking about error handling

You will find unstructured code in the session folder. Your task is to:

1. Refactor the code to make it cleaner.
2. Follow best practices for Python coding.