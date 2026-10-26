# Day 1 — Python Fundamentals

This folder contains my Day 1 exercises from my 45-day Python learning journey, alongside the **Python for Everybody Specialization**.

## Goals

- Practise collecting user input with `input()`
- Store and reuse values with variables
- Format personalised output using f-strings
- Perform arithmetic calculations
- Validate input and handle invalid values
- Test programs with normal and edge-case inputs
- Document what I learn and track progress using GitHub

## Exercises

### Exercise 1 — Personal Introduction

Prompts the user for their name, profession, and favourite programming language, then prints a personalised introduction.

Concepts: `input()`, variables, `print()`, f-strings, and `\n`.

### Exercise 2 — Study Time Calculator

Asks how many hours and minutes were studied, calculates total minutes, and displays normalized hours and minutes when the minutes value is 60 or greater. It rejects negative values and handles non-numeric input.

Concepts: `int()`, arithmetic, `while`, `if`, `continue`, `break`, `try`/`except`, `ValueError`, `//`, and `%`.

Example:

```text
Enter the number of hours studied: 2
Enter the number of minutes studied: 90

You entered: 2 hour(s) and 90 minute(s)
Normalized time: 3 hour(s) and 30 minute(s)
Total study time: 210 minutes
```

### Exercise 3 — Shopping Calculator

A small shopping calculation exercise that calculates a purchase total and presents the result as a receipt. Update this section if your final submitted version has different features.

Concepts practised include numeric input, multiplication, formatted output, and input validation where implemented.

## Files

Add or keep your exercise files in this folder using clear names, for example:

```text
day-01-fundamentals/
├── README.md
├── notes.md
├── exercise1_personal_intro.py
├── exercise2_study_time_calculator.py
└── exercise3_shopping_calculator.py
```

Keep the filenames aligned with the actual files in your repository.

## Testing

The study-time calculator was checked with normal values, zero, extra minutes, negative hours, negative minutes, and non-numeric input. The observed results matched the intended behavior for those cases.

## Learning notes

See [`notes.md`](notes.md) for explanations of the main concepts, examples, testing, and a short reflection.

## Progress

- [x] Exercise 1 code reviewed
- [x] Exercise 2 code reviewed and test screenshots reviewed
- [x] Exercise 3 code reviewed
- [x] Day 1 learning notes drafted
- [ ] Confirm all exercise files are committed to the repository

This README describes the work completed so far. I will update the progress section as repository files and commits are verified.
