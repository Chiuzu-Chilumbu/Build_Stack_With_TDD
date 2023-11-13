"""Implementation of Stack abstract data type"""

class Stack:
	def __init__(self, capacity):
		if not isinstance(capacity, int):
			raise TypeError('Stack Capacity must be an integer')

		self.capacity = capacity
		self.stack = []

	def __len__(self):
		return self.capacity

	def push(self, data):
		if len(self.stack) == self.capacity:
			raise Exception('Stack is full')
		else:
			self.stack.append(data)

	def size(self):
		return len(self.stack)

	def peek(self):
		return self.stack[-1]

	
