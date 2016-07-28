class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	def getData(self):
		return self.data
	def setData(self,newData):
		self.data = newData
	def getNext(self):
		return self.next
	def setNext(self,newNext):
		self.next = newNext
		
class LinkedList:
	def __init__(self,initData):
		self.head = Node(initData)
	def isEmpty(self):
		return self.head == None
	def add(self,newData):
		temp = Node(newData)
		temp.setNext(self.head)
		self.head = temp
	def insert(self,newData,index):
		found = False
		count = 1
		previous = None
		current = self.head
		while current !=None:
			if count == index:
				found = True
				newNode = Node(newData)
				if previous == None:
					newNode.setNext(self.head)
					self.head = newNode
				else:
					
					previous.setNext(newNode)
					newNode.setNext(current)
				break
			count = count+1
			previous = current
			current = current.getNext()
		if not found:
			print "item",index,"Index Not found in the linked list"
		
	def size(self):
		count = 0
		current = self.head
		while current !=None:
			count = count+1
			current = current.getNext()
		return count
	def search(self,data):
		found = False
		current = self.head
		while not found and (current!=None):
			if current.getData() == data:
				found = True
			else:
				current = current.getNext()
			return found
	def remove(self,data):
		found = False
		previous = None
		current = self.head
		while not found and (current!=None):
			if current.getData() == data:
				found = True
				if previous == None:
					self.head = current.getNext()
				else:
					previous.setNext(current.getNext())
			else:
				previous = current
				current = current.getNext()
		if not found:
			print "item",data,"Not found in the linked list"
	
	
	def display(self):
		current = self.head
		while current !=None:
			print current.getData(),"->",
			current = current.getNext()
		print None
			
# lst = LinkedList(4)
# print lst.isEmpty()
# lst.display()
# lst.add(12)
# lst.add(100)
# lst.add(566)
# print lst.size()
# print lst.search(12)
# lst.display()
# lst.remove(100)
# lst.display()
# lst.add(200)
# lst.display()
# lst.remove(200)
# lst.display()
# lst.add(145)
# lst.display()
# lst.remove(12)
# lst.display()
# lst.remove(788)

# lst.insert(4556,2)
# lst.display()