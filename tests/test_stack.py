"""Unit tests for stack abstract data type"""

import sys
sys.path.append('data')

import pytest
from stack_adt import Stack

def test_should_create_instance_of_stack_with_given_capacity():
	# Arrange
	size = 100
	# Act 
	stack_object = Stack(size)
	# Assert 
	assert len(stack_object) == 100


def test_should_provide_capacity_only_with_int_data_type():
	# Arrange
	bad_size = "one_hundred"
	# Act & Assert 
	with pytest.raises(TypeError):
		stack_object = Stack(bad_size)


def test_should_contain_no_elements_in_created_stack_list():
	# Arrange & Act 
	stack_object = Stack(100)
	# Assert
	assert len(stack_object) == 100