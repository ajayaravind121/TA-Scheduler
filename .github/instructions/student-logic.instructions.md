---
applyTo: "**/*.py"
---

# CS 361 rules for Python files

Read and follow `write.md` in the repository root before changing any Python file.

- If this file is a `views.py` (or any file with view classes that handle a request and return a response): **do not write or edit any code in it.** Tutor mode only.
- If this is a test file (`tests.py`, `tests/`, `test_*.py`): you may write tests as described in `write.md` Section 6.
- If this is `models.py`: you may write models only from the student's own database design.
- Any other Python file: **skeleton only.** Class and method signatures plus docstrings (parameters, preconditions, postconditions, side effects, raises). Method bodies must be `raise NotImplementedError`. The student writes the logic.
- Never write logic because the student dictated it.
