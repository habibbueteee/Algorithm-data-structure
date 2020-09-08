#FIFO first item we insert is the first item one we take out

class Queue:
	
	def __init__(self):
		self.queue = []
		
	# 0(1)
	def is_emty(self):
		return self.queue == []
		
	#0(1)
	def enqueue(self, data):
		self.queue.append(data)
		
	#0(N) liner running time complexity 
	def dequeue(self):
		if self.queue_size() < 1:
			return
		
		data = self.queue[0]
		del self.queue[0]
		return data
	
	#0(n)
	def peek(self):
		data = self.queue[0]
		return data
	
	#0(1)
	def queue_size(self):
		return len(self.queue)
		
		
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)		
queue.enqueue(3)		

print('Size: ' + str(queue.queue_size()))
print("Dequeue item: "+ str(queue.dequeue()))


print("Size: " + str(queue.queue_size()))
print("Peek item: "+ str(queue.peek()))

print("Size: " + str(queue.queue_size()))








	
		
