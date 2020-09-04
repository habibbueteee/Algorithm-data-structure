
class Node:
	
	def __init__(self, data):
		
		self.data = data
		self.nextNode = None
		self.previousNode = None
		
class LinkedList_d:
	
	def __init__(self):
		self.head = None
		self.numberOfNodes = 0
		
	def insert_start(self, data):
		
		self.numberOfNodes = self.numberOfNodes+1
		newnode = Node(data)
		
		if self.head is None:
			self.head = newnode
			
		else:
			newnode.nextNode = self.head
			self.head.previousNode = newnode
			self.head = newnode

	def traverse(self):
	
		actual_node = self.head
		
		while actual_node is not None:
			print(actual_node.data)
			actual_node = actual_node.nextNode
	
		
	
	
	
	
			
double_linked_list_1 = LinkedList_d()
double_linked_list_1.insert_start(5) 
double_linked_list_1.insert_start(7) 
double_linked_list_1.insert_start(9) 

print(double_linked_list_1.traverse())

		
