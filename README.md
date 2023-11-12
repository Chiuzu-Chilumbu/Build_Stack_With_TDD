# Build_Stack_With_TDD
Building the stack data structure using TDD &amp; BDD methodologies

---

## Phase One

In the initial phase of our project, we laid the groundwork for behavior-driven development (BDD) by writing basic scenarios using `pytest-bdd`. We focused on defining the expected behaviors of our Stack ADT (Abstract Data Type) through simple and direct test functions for each Given/When/Then step. This allowed us to quickly prototype our features and establish a baseline for our testing framework.

Here's what our `phase_one` tests accomplished:

- Ensured that the stack class could be instantiated.
- Verified that the resulting object was indeed an instance of the stack class.

## Phase Two: Refactoring and Expansion

As we moved into `phase_two`, our goal was to refine our tests and expand our feature set. This involved several improvements:

1. **Refactoring Tests**: We refactored our tests to better utilize `pytest-bdd` fixtures, which allowed for more reusable and modular test code. This setup enables us to maintain a cleaner and more scalable test suite.

2. **Introducing Fixtures**: We leveraged `pytest` fixtures to manage test setup and teardown more effectively. This approach ensures that each scenario starts with a fresh state, avoiding side effects between tests.

3. **Enhanced Assertions**: Our tests now include more robust assertions, checking for specific conditions like the capacity of the stack. This gives us more confidence in the functionality and reliability of our ADT implementation.

4. **New Features**: We introduced new features and scenarios to our BDD framework, ensuring comprehensive coverage of our stack's behavior. These additional features are designed to test our stack under a wider variety of conditions and use cases.

5. **Improved Documentation**: We documented the changes and the reasoning behind them to provide clear guidance to our team and contributors on how the testing strategy evolves over time.

By adopting these changes, we have not only made our test codebase more maintainable but also set a precedent for writing future tests as our project grows. The `phase_two` branch represents our commitment to continuous improvement and best practices in software development.

--- 
