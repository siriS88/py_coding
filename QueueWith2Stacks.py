from stack_orig import Stack

class MyQueue:

	def __init__(self):
		self.Stack_oldest = Stack()
		self.Stack_newest = Stack()
	
	def add(self,item):
		self.Stack_newest.push(item)
	
		
	def shiftStacks(self):
		if 	self.Stack_oldest.isEmpty():
			while not self.Stack_newest.isEmpty():
				self.Stack_oldest.push(self.Stack_newest.pop())
				
	def remove(self):
		self.shiftStacks()
		if self.Stack_oldest.isEmpty():
			raise NameError("Can't remove from empty queue")
		return self.Stack_oldest.pop()
			
	def peek(self):
		self.shiftStacks()
		if self.Stack_oldest.isEmpty():
			raise NameError("Can't peek empty queue")
		return self.Stack_oldest.peek()
	
	def display(self):
		front = self.Stack_oldest.returnTop()
		while front!=None:
			print "Stack_oldest:",front.data,"->",
			front = front.next
		print " " 
		frontN = self.Stack_newest.returnTop()
		while frontN!=None:
			print "Stack_newest",frontN.data,"->",
			frontN = frontN.next
		print " " 
		
Q = MyQueue()
Q.add(12)
Q.display()
Q.add(14)
Q.add(33)
Q.add(56)
Q.add(78)
Q.add(900)
Q.display()
Q.remove()
Q.display()
Q.remove()
print Q.peek()