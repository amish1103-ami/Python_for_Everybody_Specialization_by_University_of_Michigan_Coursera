# Day 1 — Python Fundamentals Notes

These notes summarize the concepts practised in Day 1 of my Python learning journey.

## 1. Python

Python is a high-level, general-purpose programming language known for readable syntax. It is used in areas such as automation, web development, data analysis, and artificial intelligence.

## 2. Variables

Variables are names that refer to values.

```python
name = "Amish"
hours_studied = 2
```

Use descriptive variable names so code is easier to understand. For example, `favourite_language` is clearer than `fpl`.

## 3. Basic Data Types

- `str`: text, such as `"Python"`
- `int`: whole numbers, such as `5`
- `float`: numbers with decimal places, such as `45.50`
- `bool`: Boolean values, either `True` or `False`

## 4. Getting User Input with `input()`

`input()` displays a prompt and returns the user's response as a string.

```python
name = input("What is your name? ")
```

Even when a user types digits, `input()` returns text. Convert the result before doing arithmetic.

## 5. Type Conversion

Use `int()` to convert suitable input to a whole number and `float()` to convert suitable input to a decimal number.

```python
hours = int(input("Hours studied: "))
price = float(input("Price: "))
```

Invalid text such as `"hello"` cannot be converted to an integer and raises `ValueError`.

## 6. Displaying Output with `print()`

`print()` displays text and values in the console.

```python
print("Hello!")
print(hours)
```

## 7. F-Strings and New Lines

An f-string makes it easy to insert variable values into text. Put `f` before the opening quotation mark and enclose expressions in curly braces.

```python
name = "Amish"
print(f"Hello, {name}!")
```

Use `\n` inside a string to start a new line.

```python
print(f"Hello, {name}.\nWelcome to Python!")
```

## 8. Arithmetic and the Study-Time Calculation

Common arithmetic operators include:

| Operator | Purpose | Example |
|---|---|---|
| `+` | Addition | `2 + 3` gives `5` |
| `-` | Subtraction | `5 - 2` gives `3` |
| `*` | Multiplication | `2 * 60` gives `120` |
| `/` | Division | `5 / 2` gives `2.5` |
| `//` | Floor division | `125 // 60` gives `2` |
| `%` | Remainder | `125 % 60` gives `5` |
| `**` | Exponentiation | `2 ** 3` gives `8` |

The total study time in minutes is calculated as:

```python
total_minutes = (hours * 60) + minutes
```

To convert total minutes into hours and remaining minutes:

```python
display_hours = total_minutes // 60
display_minutes = total_minutes % 60
```

For example, 125 minutes is 2 hours and 5 minutes.

## 9. Input Validation and Conditions

A conditional statement lets a program make decisions.

```python
if hours < 0:
    print("Hours cannot be negative.")
```

Comparison operators include `==`, `!=`, `<`, `>`, `<=`, and `>=`. Comparisons evaluate to `True` or `False`.

## 10. Loops, `break`, and `continue`

A `while` loop can repeat a prompt until valid input is provided.

- `break` exits the loop.
- `continue` skips to the next loop iteration.

These controls are useful when asking users to try again after entering invalid data.

## 11. Handling Errors with `try` and `except`

`try` and `except` let a program handle expected errors without terminating unexpectedly.

```python
try:
    hours = int(input("Hours studied: "))
except ValueError:
    print("Please enter a whole number.")
```

A `ValueError` can occur when converting text that is not a valid integer, such as `"abc"`, using `int()`.

## 12. Formatting Prices

Use `:.2f` in an f-string to display a number with two digits after the decimal point.

```python
price = 45.5
print(f"Price: ₹{price:.2f}")
```

Output:

```text
Price: ₹45.50
```

## 13. Testing and Debugging

Testing means checking a program with different inputs, including edge cases. Day 1 study-time calculator tests included:

- Normal values, such as 2 hours and 30 minutes
- Zero values
- Extra minutes, such as 2 hours and 90 minutes
- Negative hours or minutes
- Non-numeric input

When debugging, compare actual output with expected output and fix the cause of a problem rather than only changing the displayed message.

## Reflection

Day 1 practised collecting user input, storing values in variables, formatting output, performing calculations, validating input, handling `ValueError`, and testing different scenarios.

A useful next step is to keep writing small programs, test them systematically, and commit meaningful updates to GitHub.

## Bug or challenge encountered

During the study-time calculator exercise, invalid and negative input needed to be handled. I used `try`/`except ValueError` to catch non-numeric input and conditions inside `while` loops to reject negative values and prompt again.
