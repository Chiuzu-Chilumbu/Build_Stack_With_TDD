"""Implementation of Stack abstract data type"""

class Stack:
	def __init__(self, capacity):
		if not isinstance(capacity, int):
			raise TypeError('Stack Capacity must be an integer')

		self.capacity = capacity
		self.stack = []

	def push(self, data):
		if len(self.stack) == self.capacity:
			raise Exception('Stack is full')
		else:
			self.stack.append(data)

	def pop(self):
		if len(self.stack) == 0:
			raise Exception('stack is empty')
		else:
			removed_item = self.stack.pop()
		return removed_item

	def size(self):
		return len(self.stack)

	def peek(self):
		return self.stack[-1]

	def isEmpty(self):
		return self.stack == []

	def isFull(self):
		return len(self.stack) == self.capacity

	
