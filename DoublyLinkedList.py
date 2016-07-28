class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None
	def getData(self):
		return self.data
	def setData(self,newData):
		self.data = newData
	def getNext(self):
		return self.next
	def setNext(self,newNext):
		self.next = newNext
	def getPrev(self):
		return self.prev
	def setPrev(self,newPrev):
		self.prev = newPrev
		
class DoublyLinkedList:
	def __init__(self,initData):
		self.head = Node(initData)
		
	def isEmpty(self):
		return self.head == None
		
	def add(self,newData):
		temp = Node(newData)
		current = self.head
		while current.getNext() !=None:
			current = current.getNext()
		current.setNext(temp)
		temp.setPrev(current)
		temp.setNext(None)
		
	def insert(self,newData,index):
		found = False
		count = 1
		current = self.head
		while current !=None:
			if count == index:
				found = True
				newNode = Node(newData)
				if current.getPrev() == None:
					newNode.setNext(self.head)
					current.setPrev(newNode)
					self.head = newNode
				elif current.getNext()==None:
					current.setNext(newNode)
					newNode.setPrev(current)
					newNode.setNext(None)
				else:
					current.getPrev().setNext(newNode)
					newNode.setNext(current)
					newNode.setPrev(current.getPrev())
					current.setPrev(newNode)
				break
			count = count+1
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
				if current.prev == None:
					self.head = current.getNext()
					current.getNext().setPrev(None)
				elif current.getNext()==None:
					current.getPrev().setNext(None)
				else:
					current.getPrev().setNext(current.getNext())
					current.getNext().setPrev(current.getPrev())
			else:
				current = current.getNext()
		if not found:
			print "item",data,"Not found in the linked list"
			
	def display(self):
		current = self.head
		while current !=None:
			print current.getData(),"<=>",
			current = current.getNext()
		print None
			
lst = DoublyLinkedList(4)
print lst.isEmpty()
lst.display()
lst.add(12)
lst.add(100)
lst.add(566)
print lst.size()
print lst.search(12)
lst.display()
lst.remove(100)
lst.display()
lst.add(200)
lst.display()
lst.remove(200)
lst.display()
lst.add(145)
lst.display()
lst.remove(12)
lst.display()
lst.remove(788)

lst.insert(4556,2)
lst.display()
lst.insert(9999,1)
lst.display()
lst.insert(67677,lst.size())
lst.display()
