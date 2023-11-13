"""unit tests designed to test the basic operations of a stack abstract data type"""

import sys
sys.path.append('data')

import pytest
from stack_adt import Stack

@pytest.fixture(scope='function')
def stack_object_instance():
	stack = Stack(100)
	return stack


def test_should_should_be_able_to_push_item_onto_stack_without_increasing_capacity(stack_object_instance):
	# Arrange & Act
	stack_object_instance.push(5) 
	# Assert
	assert stack_object_instance.size() == 1
	assert len(stack_object_instance) == 100


def test_should_raise_exception_if_pushed_data_exceeds_stack_capacity(stack_object_instance):
	# Arrange & Act
	for i in range(100):
		stack_object_instance.push(i)

	# Assert
	with pytest.raises(Exception):
		stack_object_instance.push(101)

