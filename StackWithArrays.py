class StackUsingArray:
	
	def __init__(self,numStacks,stackCapacity):
		self.stackCapacity = stackCapacity
		self.numStacks = numStacks
		self.values = [None]*self.numStacks*self.stackCapacity
		self.numElements = [0]*self.numStacks
		
	def push(self,stackNum,data):
		if self.isStackFull(stackNum):
			raise NameError("Can't push as Stack is full")
		i_index = self.returnEmptyIndexOfStack(stackNum)
		self.values[i_index] = data
		self.numElements[stackNum] = self.numElements[stackNum] +1
			
	def pop(self,stackNum):
		if self.isEmpty(stackNum):
			raise NameError("Can't pop from an empty stack")
		top_i = self.returnEmptyIndexOfStack(stackNum)-1
		val = self.values[top_i]
		self.values[top_i] = None
		self.numElements[stackNum] = self.numElements[stackNum]-1
		return val
		
	def peek(self,stackNum):
		if self.isEmpty(stackNum):
			raise NameError("Can't peek from an empty stack")
		top_i = self.returnEmptyIndexOfStack(stackNum)-1
		return self.values[top_i]
		
	def isEmpty(self,stackNum):
		return self.numElements[stackNum]==0
		
	def isStackFull(self,stackNum):
		return self.numElements[stackNum]==self.stackCapacity
	
	def returnEmptyIndexOfStack(self,stackNum):
		offset = stackNum*self.stackCapacity
		size = self.numElements[stackNum]
		return offset+size
		
	def display(self):
		print self.values
		print "Num Elements:",self.numElements
		
S = StackUsingArray(3,4)
print S.isEmpty(1)
S.push(0,12)
S.display()
S.push(1,14)
S.push(2,134)
S.display()
print S.peek(2)
S.pop(1)
S.pop(0)
S.pop(2)
S.display()
		