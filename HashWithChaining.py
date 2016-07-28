#Here we are using a psuedo privately nested class. In python, a nested class does not inherit any of its parents methods.
# so we have to either refer to nested class constructor or other methods as OuterClass.NestedClass(). Also, calling the 
#outer class constructor does not cal the inner class constructor. They behave like two sperate classes infact.  
class HashWithChaining:
	class _HashCell:
		def __init__(self,key,value):
			self.key = key
			self.value = value
			self.next = None
			self.prev = None	
	
		def isEmpty(self):
			return self.key==None
		
		def setValue(self,key,value):
			self.value = value
		
		def setNext(self,next):
			self.next = next
		
		def setPrev(self,prev):
			self.prev = prev
			
		def setHashCellForKey(self,key,value):
			current = self
			newCell = HashWithChaining._HashCell(key,value)
			while current.next!=None:
				current = current.next
				
			current.setNext(newCell)
			current.next.setPrev(current)
				
				
		def getHashCellForKey(self,key):
			current = self
			while current!=None:
				if current.key==key:
					return current
				current = current.next
			return None
		
	def __init__(self,capacity):
		self.items = []
		self.capacity=capacity
		
		for i in range(0,capacity):
			self.items.append(None)
			
	def put(self,key,value):
		hIndex = self.hashAKey(key)
		if self.items[hIndex] == None:
			self.items[hIndex] = HashWithChaining._HashCell(key,value)
		else:
			current = self.items[hIndex]
			current.setHashCellForKey(key,value)
			
	def remove(self,key):
		hIndex = self.hashAKey(key)
		if self.items[hIndex] == None:
			return False
		else:
			hCell = self.items[hIndex].getHashCellForKey(key)
			if hCell!=None:
				#if head
				if hCell.prev ==None:
					self.items[hIndex] = hCell.next
					if hCell.next!=None:
						hCell.next.setPrev(None)
				elif hCell.next==None: #tail
					hCell.prev.setNext(None)
				else:	#middle
					hCell.prev.setNext(hCell.next)
					hCell.next.setPrev(hCell.prev)
				hCell.setNext(None)
				hCell.setPrev(None)
		return True
			
	def search(self,key):
		hIndex = self.hashAKey(key)
		if self.items[hIndex] !=None:
			hCell = self.items[hIndex].getHashCellForKey(key)
			return hCell!=None
		return False	
			
	def hashAKey(self,key):
		return key%(len(self.items))
			
	def display(self):
		counter =0
		for i in self.items:
			print counter,"==>",
			counter+=1
			
			current = i
			while current!=None:
				print (current.key,current.value),"->",
				current = current.next
			print " "
		print " "
			
			
HM = HashWithChaining(10)
HM.put(145,"Dog")
HM.put(278,"Cat")
HM.put(345,"Fish")
HM.put(47,"Baby")
HM.put(23,"Bird")

HM.display()
HM.remove(47)
HM.display()
print HM.search(400)
HM.remove(145)
HM.display()
			
	
