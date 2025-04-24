# 0x00. Python - Variable Annotations

## Description
This project focuses on learning Python variable annotations, type hints, and how to use them to specify function signatures and variable types. It covers basic annotations, complex types, duck typing, and validation with mypy.

## Learning Objectives
At the end of this project, you should be able to explain to anyone, without the help of Google:
- Type annotations in Python 3
- How to use type annotations for function signatures and variable types
- Duck typing in Python
- How to validate code with mypy

## Requirements
- **OS**: Ubuntu 18.04 LTS
- **Python**: 3.7
- All files must end with a new line
- The first line of all files should be `#!/usr/bin/env python3`
- Code should follow pycodestyle (version 2.5)
- All files must be executable
- Documentation is mandatory for modules, classes, and functions

## Project Tasks

| **Task** | **Description** | **File** |
|----------|----------------|----------|
| **0. Basic annotations - add** | Add two floats with type annotations | `0-add.py` |
| **1. Basic annotations - concat** | Concatenate two strings with type annotations | `1-concat.py` |
| **2. Basic annotations - floor** | Return floor of float with type annotations | `2-floor.py` |
| **3. Basic annotations - to string** | Convert float to string with type annotations | `3-to_str.py` |
| **4. Define variables** | Define and annotate variables with specified values | `4-define_variables.py` |
| **5. Complex types - list of floats** | Sum list of floats with type annotations | `5-sum_list.py` |
| **6. Complex types - mixed list** | Sum mixed list of ints and floats with type annotations | `6-sum_mixed_list.py` |
| **7. Complex types - string and int/float to tuple** | Return tuple with string and squared number | `7-to_kv.py` |
| **8. Complex types - functions** | Return function that multiplies float by multiplier | `8-make_multiplier.py` |
| **9. Duck typing - iterable object** | Annotate function with duck-typed parameters | `9-element_length.py` |
| **10. Duck typing - first element** | Annotate function with sequence duck-typing | `100-safe_first_element.py` |
| **11. More involved type annotations** | Add advanced type annotations using TypeVar | `101-safely_get_value.py` |
| **12. Type Checking** | Validate code with mypy and apply fixes | `102-type_checking.py` |

## How to Validate with mypy
To check type annotations with mypy:
```bash
mypy *.py
```

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
