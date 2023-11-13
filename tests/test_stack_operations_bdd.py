"""Behavioral test to test the basic stack operations"""

import sys 
sys.path.append('data')
sys.path.append('stack/Build_Stack_With_TDD/tests')

import pytest 
from pytest_bdd import scenarios, given, when, then
from stack_adt import Stack

scenarios('features/stack_operations.feature')

@pytest.fixture(scope='function')
@given('a stack object with provided capacity')
def stack_class():
	return Stack(50)

@pytest.fixture
@when('the data is pushed onto the the stack')
def stack_push_data(stack_class):
	stack_class.push(10)
	return stack_class

@then('the data pushed should be seen or peeked as the most recent data')
def test_stack_should_contain_pushed_data(stack_push_data):
	assert stack_push_data.peek() == 10