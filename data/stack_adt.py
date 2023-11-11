"""Implementation of Stack abstract data type"""

class Stack:
	def __init__(self, capacity):
		if not isinstance(capacity, int):
			raise TypeError('Stack Capacity must be an integer')

		self.capacity = capacity
		self.stack = []

	def __len__(self):
		return self.capacity

