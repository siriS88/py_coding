class Queue:
	class _Node:
		data = None
		next = None
		def __init__(self,data):
			self.data = data
			
	def __init__(self):
		self._front = None
		self._end = None
	
	def remove(self):
		if self._front == None:
			raise NameError("Can't remove from an empty stack")
		item = self._front
		self._front=self._front.next

		if self._front == None:
			self._end = self._front
			
		return item.data
		
	def add(self,item):
		item = Queue._Node(item)
		if self._end !=None:
			self._end.next = item
		self._end = item
			
		if self._front == None:
			self._front = self._end
		return item
			
	def peek(self):
		if self._front == None:
			raise NameError("Can't peek into an empty stack")
		return self._end
		
	def isEmpty(self):	
		return self._front == None	
		
	def display(self):
		curr = self._front 
		while curr != None:
			print curr.data,"->",
			curr = curr.next
		print " "
			
			
#Q = Queue()
#print Q.isEmpty()
#Q.add(12)
#Q.display()
#Q.add(14)
#Q.display()
#Q.remove()
#Q.display()
#Q.remove()
#Q.display()
#print Q.isEmpty()
			
		