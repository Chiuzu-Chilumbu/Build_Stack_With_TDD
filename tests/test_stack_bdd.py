"""Behavioral tests for stack abstract datatype"""

import sys 
sys.path.append('data')
sys.path.append('stack/Build_Stack_With_TDD/tests')

import pytest 
from pytest_bdd import scenarios, given, when, then
from stack_adt import Stack

scenarios('features/create_stack.feature')

@pytest.fixture
@given('a stack class exists')
def stack_class():
    return Stack

@pytest.fixture
@when('a stack object is instantiated with the stack capacity')
def stack_object(stack_class):
    return stack_class(100)

@then('the instantiated stack object should contain an empty list')
def test_stack_with_given_capacity(stack_object):
    assert len(stack_object) == 100
