from stack_orig import Stack

class stackWithMin2(Stack):

	def __init__(self):
		self.stack2 = Stack()
		Stack.__init__(self)
		
	def push(self,data):
		if data<self.getMin():
			self.stack2.push(data)
		Stack.push(self,data)
		
	def pop(self):
		if self.peek() == self.getMin():
			self.stack2.pop()
		return Stack.pop(self)
						
	def getMin(self):
		if self.stack2.isEmpty():
			return 10**8
		else:
			return self.stack2.peek()
		

S = stackWithMin2()
print S.isEmpty()
S.push(12)
S.display()
S.push(14)
print S.getMin()
S.display()
S.pop()
print S.getMin()
S.display()