from stack_Q3 import Stack3

class StackOfPlates():
	def __init__(self,capacity):
		self.stackList = []
		self.capacity = capacity
		 
	def push(self,item):
		lastStack = self.getLastStack()
		if lastStack and not lastStack.length() == self.capacity:
			lastStack.push(item)
		else:
			newStack = Stack3()
			newStack.push(item)
			self.stackList.append(newStack)
	
	def pop(self):
		lastStack = self.getLastStack()
		if not lastStack: #equal to lastStack==None or stackList is empty
			raise NameError("Can't pop empty stack")
		item = lastStack.pop()
		if lastStack.isEmpty():
			self.stackList.remove(lastStack)
		return item
		
	def getLastStack(self):
		if len(self.stackList) == 0:
			return None
		else:
			return self.stackList[len(self.stackList)-1]
			
	def isEmpty(self):
		return len(self.stackList)==0
		
	def display(self):
		for i in range(0,len(self.stackList)):
			self.stackList[i].display()
			
	def popAt(self,index):
		return self.leftShift(index,True)
		
	def leftShift(self,index,removeTop):
		if removeTop:
			item = self.stackList[index].pop()
		else:
			item = self.stackList[index].removeBottom()
		if self.stackList[index].isEmpty():
			self.stackList.remove(stackList[index])
		else: #recursion to move bottom of previous stack into the stack where we poped at index
			if index < len(self.stackList)-1:
				v = self.leftShift(index+1,False)
				self.stackList[index].push(v)
		return item
					
				
	

S = StackOfPlates(4)
S.push(12)
S.push(14)
S.push(15)
S.push(16)
S.display()
print "&&&&&&&&"
S.push(18)
S.push(20)
S.display()
print "&&&&&&&&"
S.pop()
S.display()
print "&&&&&&&&"
S.pop()
S.display()
print "&&&&&&&&"
S.pop()
S.display()
print "&&&&&&&&"
S.push(125)
S.push(147)
S.push(158)
S.push(160)
S.display()
print "&&&&&&&&"
S.popAt(0)
S.display()
	