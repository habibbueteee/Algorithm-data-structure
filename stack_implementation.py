
#LIFO: Last item insert is the first item we take out

class Stack:
	
	def __init__(self):
		self.stack = [] #1-D array
	
	# insert item into stack //0(1)
	def push(self, data):
		self.stack.append(data)
	
	#remove and return the last item from stack (LIFO)//0(1)
	def pop(self):
		
		if self.stack_size() < 1:
			return
		
		data = self.stack[-1]
		del self.stack[-1]
		return data
		
	#peek : it returns last item without removing it//0(1)
	
	def peek(self):
		return self.stack[-1]
		
	#has //0(1)
	def is_emty(self):
		return self.stack == []
		
	def stack_size(self):
		return len(self.stack)
		
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print('Size: ' + str(stack.stack_size()))
print("Popped item: "+ str(stack.pop()))


print("Size: " + str(stack.stack_size()))
print("Peek item: "+ str(stack.peek()))

print("Size: " + str(stack.stack_size()))






		
		
		
