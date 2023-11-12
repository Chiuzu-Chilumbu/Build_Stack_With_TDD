# Build_Stack_With_TDD
Building the stack data structure using TDD &amp; BDD methodologies

---

## Phase Three: Enhancing Functionality and Testing

In `phase_three`, our Stack ADT evolves with additional methods and features, significantly increasing its capabilities. This phase is characterized by the implementation of essential stack operations and the expansion of our test suite to ensure these new features behave as expected.

### New Stack Operations

We've extended the functionality of our `Stack` class to include the following operations:

- **Push**: Adds an element to the top of the stack.
- **Peek**: Returns the element at the top of the stack without removing it.

These operations are fundamental to the stack's behavior and allow for more complex use cases.

### BDD Test Expansion

To validate our new features, we've written a new set of BDD tests focusing on stack operations:

- Our feature file `stack_operations.feature` outlines scenarios that test the interaction with the stack through its operations.
- We've implemented new `Given`, `When`, `Then` steps in our BDD tests to ensure that pushing data onto the stack and peeking at the top element work correctly.

### Unit Test Refinement

Alongside our BDD tests, we've also refined our unit testing approach:

- New unit tests have been added to test the stack's capacity and ensure that exceptions are raised appropriately when exceeding this capacity.
- We continue to follow the Arrange-Act-Assert pattern to keep our tests clear and maintainable.

### How to Run the Tests

To run the new tests, navigate to the root directory of the project and use the following command:

```bash
pytest tests/
```

This will execute both the unit tests and the BDD scenarios, verifying the integrity of our stack implementation.

### Future Directions

With these enhancements, our stack is now more robust and ready for more complex applications. As we progress to the next phase, we'll look into implementing additional operations such as `pop`, and we'll further refine our testing strategy to cover edge cases and error handling.

---
