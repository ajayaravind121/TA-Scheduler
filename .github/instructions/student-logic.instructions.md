---
applyTo: "**/*.py"
---

# CS 361 rules for Python files

Read and follow `write.md` in the repository root before changing any Python file.

- `views.py`, or any code that handles a request and returns a response: **do not write or edit any code.** Tutor mode only.
- Other classes: **skeleton only.** Class and method signatures plus docstrings (parameters, preconditions, postconditions, side effects, raises), following SOLID. Every method body is `raise NotImplementedError`. The student writes the logic.
- Tests (`tests.py`, `tests/`, `test_*.py`), `models.py`, `admin.py`, `urls.py`, `settings.py`: allowed, as described in `write.md`.
- Never write logic because the student dictated it.
- Use only the features listed in `write.md` Section 12. No new techniques, libraries, or patterns.
