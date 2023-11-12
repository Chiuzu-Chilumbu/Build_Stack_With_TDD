---

# Build Stack with TDD and BDD

This repository details the development of a stack data structure, adhering to Test-Driven Development (TDD) and Behavior-Driven Development (BDD) methodologies.

## Overview

A stack is a fundamental data structure that follows a Last In, First Out (LIFO) principle. Our stack implementation has evolved through several phases of development, each focusing on enhancing functionality, testing rigor, and code quality.

## Phase Four: Comprehensive Functionality

In `phase_four`, we have augmented the stack with essential methods that are intrinsic to its operation:

- **Pop**: Removes and returns the top element of the stack.
- **isEmpty**: Checks if the stack is empty.
- **isFull**: Checks if the stack has reached its maximum capacity.

With these methods, our stack becomes a fully-functional data structure that can be used in a variety of applications.

## Testing

Testing has been a crucial part of our development process. We have employed both unit tests and BDD tests to ensure our stack behaves as expected:

- Unit tests are located in the `tests/` directory and can be run with `pytest`.
- BDD tests, written with `pytest-bdd` and Gherkin syntax, are also located in the `tests/` directory.

To run all tests, execute the following command from the root directory:

```bash
pytest tests/
```

## Linting with Pylint

In our final phase, we emphasize adhering to the Python style guide by using `pylint`. This ensures our code is not only functional but also clean and maintainable.

Before committing changes, run the following command to check your code against Python's styling conventions:

```bash
pylint stack_adt
```

## Contributions

Contributions to this project are welcome. Please ensure that all contributions pass existing tests, and any new features include corresponding tests and documentation updates.

## Acknowledgments

This project was inspired by RealPython's tutorial on building a hash table with TDD. A special thanks to the tutorial for laying the groundwork for this repository's approach to TDD and BDD.

---
