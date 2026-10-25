# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 1
- Student name: Tey Xin Yi
- Group ID: n/a
- AI level: 1
- Tools cited: Google (2026). Gemini. Retrieved 25 October 2026 from [https://gemini.google.com](https://gemini.google.com)

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 2026-10-24 23:35
- Tool: Google (2026). Gemini. Retrieved 25 October 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "explain this environment for me to understand in simpler terms"
- Output: Explained the concept of Python virtual environments using an isolated toolbox analogy to clarify dependency isolation and interpreter selection in VS Code.
- Verified by: Inspected the VS Code interpreter path and verified the behavior of isolated libraries.
- My change: Used the conceptual explanation to understand how local environments isolate project dependencies from global system packages.
- Used in: Conceptual understanding for Task T1 and README setup.

## Entry 2

- Date: 2026-10-24 23:45
- Tool: Google (2026). Gemini. Retrieved 25 October 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: "what answer should i insert in these lines of questions [README.md template]"
- Output: Outlined the required terminal commands for virtual environment activation across platforms and summarized the rationale for excluding machine-specific binaries from version control.
- Verified by: Checked against lab brief criteria R4 and R5.
- My change: Drafted the README explanations and run commands based on the suggested structure.
- Used in: README.md

## Entry 3

- Date: 2026-10-24 23:55
- Tool: Google (2026). Gemini. Retrieved 25 October 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: "i dont know how to complete the code in step 2 because i just learned python, guide me on how to write the clause and give explanation [src/env_check.py]"
- Output: Clause guidance and explained how importlib.metadata.version handles package lookup, the syntax of catching PackageNotFoundError, and how platform attributes map to environment dictionary keys.
- Verified by: Executed python src/env_check.py in the terminal to verify the dictionary output.
- My change: Implemented the error handling and dictionary mapping logic in env_check.py using the guided concepts.
- Used in: src/env_check.py in package_version() and check_environment()

## Entry 4

- Date: 2026-10-25 00:00
- Tool: Google (2026). Gemini. Retrieved 25 October 2026 from https://gemini.google.com
- Purpose: explain
- Prompt: "I dont know how to use the clause of python, guide me to complete task 3 [src/basics.py]"
- Output: Explained the role of guard clauses in input validation, how true division (/) differs from floor division (//), and how to format floating-point values to one decimal place in f-strings.
- Verified by: Verified that guard clauses properly intercepted zero-total counts and negative values.
- My change: Implemented defensive checks for division by zero and input validation in basics.py.
- Used in: src/basics.py in gc_percent(), format_report(), and parse_counts()

## Entry 5

- Date: 2026-10-25 00:05
- Tool: Google (2026). Gemini. Retrieved 25 October 2026 from https://gemini.google.com
- Purpose: debug
- Prompt: "what does the following error means and what should i change: AssertionError in test_format_report_visible with extra space"
- Output: Diagnosed the pytest failure by pointing out an accidental extra whitespace character between 'GC' and the percentage value.
- Verified by: Re-ran python -m pytest in the terminal.
- My change: Corrected the string spacing inside format_report() to match the expected single-space pattern.
- Used in: src/basics.py in format_report()

## Entry 6

- Date: 2026-10-25 00:15
- Tool: Google (2026). Gemini. Retrieved 25 October 2026 from https://gemini.google.com
- Purpose: hint
- Prompt: "i dont understand the clause of test_visible.py, guide me to complete three tests of your own: one boundary case (for example all counts in G and C), one zero-total case and one invalid-input case and explain it"
- Output: Outlined testing strategies using pytest.raises for exception checking and explained how to design boundary tests for 100% GC content and invalid tokens.
- Verified by: Ran python -m pytest and ruff check src.
- My change: Wrote three custom unit tests covering boundary, zero-total, and invalid-input cases.
- Used in: tests/test_lab01_own.py


