"""Unit tests for stack abstract data type"""

import sys
sys.path.append('data')

from stack_adt import Stack

def test_should_create_stack_object_from_stack_class():
	stack_object = Stack()
	assert stack_object is not None


def test_should_have_stack_object_that_is_instance_of_stack_class():
	stack_object = Stack()
	assert isinstance(stack_object, Stack)