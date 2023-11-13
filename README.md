---

# Stack ADT Built with TDD and BDD

This repository showcases the development of a Stack Abstract Data Type (ADT) following rigorous Test-Driven Development (TDD) and Behavior-Driven Development (BDD) practices.

## Overview

The Stack ADT implemented in this project adheres to the Last In, First Out (LIFO) principle. Throughout its development, we have adhered to a phased approach, progressively enhancing functionality, expanding test coverage, and refining code quality.

## Development Phases

- **Phase One**: Established the project's structure and created foundational BDD tests.
- **Phase Two**: Refined tests using `pytest-bdd` fixtures and enhanced assertions.
- **Phase Three**: Expanded stack functionalities with `push`, `pop`, `isEmpty`, and `isFull` methods, and corresponding unit and BDD tests.
- **Phase Four**: Added advanced functionalities and comprehensive tests, ensuring all stack operations are thoroughly validated.
- **Final Phase**: Focused on code quality with `pylint`, reinforcing adherence to Python's styling conventions.

## Features

The stack supports a variety of operations, making it a robust data structure suitable for numerous applications:

- **Push**: Add an element to the stack.
- **Pop**: Remove and return the top element.
- **Peek**: Return the top element without removing it.
- **isEmpty**: Check if the stack is empty.
- **isFull**: Check if the stack has reached its maximum capacity.
- **Size**: Get the number of elements in the stack.

## Testing

To ensure the reliability and correctness of the Stack ADT, a comprehensive test suite has been developed:

- **Unit Tests**: Run `pytest tests/` to execute unit tests which verify individual operations.
- **BDD Tests**: Implemented with `pytest-bdd`, allowing behavioral specifications to be written alongside the test code.

## Linting

Code quality is enforced through linting with `pylint`:

```bash
pylint stack_adt
```

Ensure to lint your code before committing changes to maintain a clean and consistent codebase.

## How to Use

Instructions on how to use the stack in your own projects are provided, including example code snippets and explanations of each method.

## Contributions

Contributions are welcome. We encourage contributors to adhere to the established practices:

- Maintain the TDD and BDD approach.
- Ensure all tests pass and add new tests for additional features.
- Follow Python style guidelines and pass `pylint` checks.

## Acknowledgments

Inspiration for this project came from RealPython's tutorial on TDD. We extend our gratitude for the guidance that shaped our testing approach.

---
