"""behavoural tests for stack abstract datatype"""

import sys 
sys.path.append('data')
sys.path.append('stack/Build_Stack_With_TDD/tests')

import pytest 
from pytest_bdd import scenario, given, when, then

@scenario('features/create_stack.feature', 'Create a stack object from a stack class')
def test_create_stack_object_from_class_stack():
	pass


@given('a stack class exists')
def test_should_contain_a_stack_class():
	pass

@when('a stack object is instanciated')
def test_should_contain_an_object_created_from_stack_class():
	stack_object = Stack()
	assert stack_object is not None

@then('the instanciated stack object should be an instance of the class')
def test_should_contain_an_object_that_is_an_instance_of_the_stacak_class():
	stack_object = Stack()
	assert isinstance(stack_object, Stack)

