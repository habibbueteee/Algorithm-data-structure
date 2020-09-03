
class Node:
	
	def __init__(self, data):
		self.data = data
		self.nextNode = None
		
class LinkedList:
	
	def __init__(self):
		self.head = None
		self.numOfNodes = 0

#We can add new data at the beginning in o(1)/ ortho 1 running time complexity		
	def insert_start(self, data):
		
		self.numOfNodes = self.numOfNodes+1
		new_node = Node(data)
		
		if not self.head:
			self.head = new_node
			
		else:
			new_node.nextNode = self.head
			self.head = new_node
#Linear running time o (N)			
	def insert_end(self, data):
		
		self.numOfNodes = self.numOfNodes+1
		new_node = Node(data)
		
		actual_node = self.head
		
		while actual_node.nextNode is not None:
			actual_node = actual_node.nextNode
		
		actual_node.nextNode = new_node
		
	def remove(self, data):
		if self.head is None:
			return	
		actual_node = self.head
		previous_node = None
			
		while actual_node is not None and actual_node.data != data:
			previous_node = actual_node
			actual_node = actual_node.nextNode
				
		# the item is not present in the linked list
		if actual_node is None:
			return
		self.numOfNodes = self.numOfNodes-1	
		#removing data is the head data
		if previous_node is None:
			self.head = actual_node.nextNode
		
		else:
			previous_node.nextNode = actual_node.nextNode
			
			
# 0 (1)
	def size_of_linkedList(self):
		
		return self.numOfNodes

# 0(N)	
	def traverse(self):
	
		actual_node = self.head
		
		while actual_node is not None:
			print(actual_node.data)
			actual_node = actual_node.nextNode


Linked_list = LinkedList()
Linked_list.insert_start(4)
Linked_list.insert_start(3)
Linked_list.insert_start(7.5)

Linked_list.insert_end(10)
Linked_list.insert_end('Adam')

Linked_list.traverse()
print('Size: ' + str(Linked_list.size_of_linkedList()))
print('\n')

Linked_list.remove(7.5)

Linked_list.traverse()

print('Size: ' + str(Linked_list.size_of_linkedList()))
