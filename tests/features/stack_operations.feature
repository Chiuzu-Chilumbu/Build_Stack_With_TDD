"""Feature file to ensure stack operations"""

Feature: After having created the stack, we should be able to perform basic stack operations

  Scenario: the stack class object should be able to push data and onto the created list
    Given a stack object with provided capacity
	When the data is pushed onto the the stack
	Then the data pushed should be seen or peeked as the most recent data