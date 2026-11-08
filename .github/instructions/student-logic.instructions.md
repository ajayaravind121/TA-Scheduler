---
applyTo: "**/*.py"
---

# CS 361 rules for Python files

Read and follow `write.md` in the repository root before changing any Python file.

- `views.py`, or any code that handles a request and returns a response: **do not write or edit any code.** Tutor mode only.
- Any other method or function: before writing or changing its body, check that its docstring (written by the student) has **preconditions, postconditions, and side effects**. If any is missing, do not implement it; ask the student to add it.
- Never write or edit docstrings. Suggest and review only.
- Implementations must check the stated preconditions, make every postcondition true, and cause no side effects beyond those listed.
- Tests (`tests.py`, `tests/`, `test_*.py`) are allowed and come from the student's contracts. Test methods do not need contracts.
- Use only the features listed in `write.md` Section 12. No new techniques, libraries, or patterns.
