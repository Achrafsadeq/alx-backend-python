# 0x03. Python - Unittests and Integration Tests

## Description

This project focuses on writing unit tests and integration tests in Python. You'll learn how to use the `unittest` framework, mock external dependencies, parameterize tests, and write both unit tests (isolated tests) and integration tests (tests that combine multiple components). The project covers testing techniques including patching, mocking, and parameterization.

## Requirements

| Category | Details |
|----------|---------|
| Python Version | 3.7 (Ubuntu 18.04 LTS) |
| File Endings | All files should end with a new line |
| Shebang | First line should be `#!/usr/bin/env python3` |
| README | Mandatory README.md at project root |
| Style Guide | pycodestyle (version 2.5) |
| Executables | All files must be executable |
| Documentation | Modules, classes, and functions require docstrings |
| Type Annotations | All functions and coroutines must be type-annotated |

## Required Files

- `utils.py` (provided)
- `client.py` (provided)
- `fixtures.py` (provided)

## Project Structure

| Task | Description | File |
|------|-------------|------|
| 0 | Parameterize a unit test for nested map access | `test_utils.py` |
| 1 | Test nested map access exception cases | `test_utils.py` |
| 2 | Mock HTTP calls for get_json function | `test_utils.py` |
| 3 | Test memoization decorator | `test_utils.py` |
| 4 | Test GithubOrgClient.org with patching | `test_client.py` |
| 5 | Mock a property to test _public_repos_url | `test_client.py` |
| 6 | More patching to test public_repos | `test_client.py` |
| 7 | Parameterize test for has_license | `test_client.py` |
| 8 | Integration test with fixtures | `test_client.py` |
| 9 | Advanced integration tests | `test_client.py` |

## Learning Objectives

By completing this project, you will be able to:

* Write unit tests using Python's `unittest` framework
* Use parameterized tests to test multiple cases efficiently
* Mock external dependencies using `unittest.mock`
* Understand the difference between unit tests and integration tests
* Patch functions and properties in tests
* Test exception cases properly
* Write integration tests that combine multiple components
* Use fixtures for test data
* Test memoization functionality
* Mock HTTP requests and responses
* Write tests for class methods and properties

## Testing Concepts Covered

- Unit testing with `unittest`
- Test parameterization with `parameterized`
- Mocking with `unittest.mock.patch`
- Patching functions and properties
- Testing exceptions
- Integration testing
- Using fixtures
- Testing memoization
- Mocking HTTP requests
- Assertion methods (`assertEqual`, `assertRaises`, etc.)

## Mission Director
This project is supervised by the ALX Software Engineering Program.

## Developer
**Codename**: Achraf Sadeq

## Acknowledgments
Holberton School, in collaboration with the ALX Software Engineering Program, developed this project for educational purposes.
