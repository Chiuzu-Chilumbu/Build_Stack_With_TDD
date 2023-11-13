
---

# Build Stack with TDD and BDD

This repository details the development of a stack data structure, adhering to Test-Driven Development (TDD) and Behavior-Driven Development (BDD) methodologies.

## Overview

A stack is a fundamental data structure that follows a Last In, First Out (LIFO) principle. Our stack implementation has been progressively enhanced through various phases of development, each focusing on expanding functionality, increasing test coverage, and ensuring code quality.

## Phase Four: Advanced Functionalities and Testing

In `phase_four`, we have introduced advanced functionalities to the stack, making it a comprehensive and fully-functional data structure:

- **Pop**: Removes and returns the top element of the stack.
- **isEmpty**: Checks if the stack is empty, providing an immediate check for stack underflow.
- **isFull**: Determines if the stack has reached its maximum capacity, preventing stack overflow.

These methods ensure our stack is versatile and robust, ready for integration into larger applications or systems.

## Testing Enhancements

Testing remains a cornerstone of our development process. We have refined our testing suite to encompass both unit tests and BDD tests, providing a rigorous validation for our stack's behavior:

- Unit tests can be found in the `tests/` directory. They ensure the reliability of individual stack operations and can be executed using the `pytest` command.
- BDD tests, formulated with `pytest-bdd` and Gherkin syntax, validate the stack's behavior in scenarios that mimic real-world use cases. These tests are also located within the `tests/` directory.

To run the entire test suite and verify the functionality of the stack, use the command:

```bash
pytest tests/
```

## Acknowledgments

This project was inspired by RealPython's tutorial on building a hash table with TDD. A special thanks to the tutorial for laying the groundwork for this repository's approach to TDD and BDD.

---
