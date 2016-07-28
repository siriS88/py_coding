from LinkedList import LinkedList
from abc import ABCMeta

class Animal:
	__metaclass__ = ABCMeta
	positionInQ = None
	name = None
	
	def __init__(self,str): 
		self.name = str
	def setPosition(self,position):
		self.positionInQ = position
	def getPosition(self):
		return self.positionInQ
	def isOlderThan(self,a):
		return self.positionInQ<a.getPosition()
		
		
class AnimalQueue:
	def __init__(self):
		self.dogList = LinkedList(None)
		self.catList = LinkedList(None)
		self.order = 0
	
	def enqueue(self,animal):
		animal.setPosition(self.order)
		self.order = self.order + 1
		
		if type(animal) is dog:
			d = dog(animal.name) #cast this animal to dog subclass
			d.setPosition(animal.getPosition())
			self.dogList.add(d) 
		elif type(animal) is cat:
			c = cat(animal.name) #cast this animal to cat subclass
			c.setPosition(animal.getPosition())
			self.catList.add(c) 

	def dequeueAny(self):
		if self.dogList.size() == 0:
			item = self.dequeCat()
		elif self.catList.size() ==0:
			item = self.dequeueDog()
		
		if self.getTail(self.dogList).getData().isOlderThan(self.getTail(self.catList).getData()):
			item = self.dequeueDog()
		elif self.getTail(self.catList).getData().isOlderThan(self.getTail(self.dogList).getData()):
			item = self.dequeCat()
		return item
		
	def dequeueDog(self):
		item = self.getTail(self.dogList).getData()
		self.dogList.remove(item)
		return item.name
		
	def dequeueCat(self):
		item = self.getTail(self.catList).getData()
		self.catList.remove(item)
		return item.name
		
	def displayList(self,llist):
		current = llist.head
		while current.getData() !=None:
			print current.getData().name,"(",current.getData().getPosition(),")->",
			current = current.getNext()
		print None
		
	def disp(self):
		self.displayList(self.dogList)
		self.displayList(self.catList)
		
	def getTail(self,llist):
		current = llist.head
		while current.getNext().getData() !=None:
			current = current.getNext()
		return current

class dog(Animal):
	def __init__(self,str):
		Animal.__init__(self,str)
		
class cat(Animal):
	def __init__(self,str):
		Animal.__init__(self,str)		
			
				
A = AnimalQueue()
X = dog("Tommy")
V = cat("sylvester")
Y = dog("Jimmy")
Z = cat("garfield")

A.enqueue(X)

A.enqueue(V)
A.enqueue(Y)
A.enqueue(Z)
A.disp()
print "%%%%%%%%%%%%%"
print A.dequeueAny()
A.disp()
print "%%%%%%%%%%%%%"
A.dequeueDog()
A.disp()
print "%%%%%%%%%%%%%"
A.dequeueCat()
A.disp()
