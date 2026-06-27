# 🐍 Python Fundamentals Journey

Welcome to my personal playground for mastering Python! This repository serves as a code journal where I track my progress, experiment with core programming concepts, and document my learning milestones.

---

## 🛠️ Concepts Covered & Code Structure

### 📁 Chapter 1: Variables & Core Basics
* **`variable.py`** & **`data_types.py`** – Declaring variables and inspecting data types using the `type()` function.
* **`rules.py`** – Rules of Python syntax: variable naming conventions, case-sensitivity, and restricted keywords.
* **`print_statements.py`** – Mastering output formatting, working with strings, and using modern Python **f-strings**.
* **`type_conversion.py`** & **`input_from_user.py`** – Handling dynamic user interaction, type casting, and fixing default string input behaviors.

### 📁 Chapter 2: Operators & Control Logic
* **`1.escape sequence.py`** – Formatting text outputs cleanly using tokens like `\n` (New Line) and `\t` (Tab).
* **`2.arithmetic_operator.py`** – Math calculations including Floor Division (`//`), Exponentiation (`**`), and Modulus (`%`).
* **`3.comparison_operator.py`** – Comparing values (`==`, `!=`, `>`, `<`, `>=`, `<=`) for Boolean outputs.
* **`4.logical_operator.py`** – Combining multiple conditions using `and`, `or`, and `not`.
* **`5.practice_question1.py`** to **`8.practice_question4.py`** – Math challenges, Even/Odd detection, and decimal rounding shortcuts (`{average:.3f}`).

### 📁 Chapter 3: Conditional Logic (`if-elif-else`)
* **`1.basic_if_else.py`** – Basic decision-making paths using conditional checks.
* **`2.elif_statement.py`** – Handling multiple evaluation conditions (e.g., Grading systems from `A` down to `Fail`).
* **`3.nested_if_else.py`** – Placing decisions inside decisions (e.g., Checking age *and* qualification status).
* **`4.ternary_operator.py`** – Writing slick, single-line if-else statements: `status = "Adult" if age >= 18 else "Minor"`.
* **`q1.py`** & **`q2.py`** – Logic builders evaluating positive/negative/zero numbers and finding the greater of two inputs.
* **`q3.py`** – The classic **Leap Year** challenge solved using robust bracket grouping and modulus math.

### 📁 Chapter 4: Introduction to Loops (`while`)
* **`1.basic.py`** – Understanding iteration, loop entry criteria, and the critical importance of updating the iterator (`i += 1`).
* **`2.print1to10.py`** – Creating dynamic loops using user limits and modifying the `print()` behavior using `end=" "` to print horizontally.

---

## 💡 Key Takeaway: Elegant Logic I Mastered

### 1. The Single-Line Shortcut (Ternary Operator) ⚡
Instead of writing a bulky 4-line block to assign a value based on a condition, I learned to write it cleanly on a single line:
```python
status = "Adult" if age >= 18 else "Minor"