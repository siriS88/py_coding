from abc import ABCMeta
from time import gmtime, strftime

class fileSystem:
	__metaclass__= ABCMeta
	def __init__(self,name,parent):
		self.name = name
		self.parentDir = parent
		self.createdOn = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		self.lastAccessed =strftime("%Y-%m-%d %H:%M:%S", gmtime())
		self.lastUpdated = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		
	def delete(self):
		if self.parentDir==None:
			return False
		else:
			self.parentDir.deleteEntry(self)
		return True
			
	def size(self):pass
	
	def getFullPath(self):
		if self.parentDir == None:
			return self.name
		else:
			return self.parentDir.getFullPath() + "/" + self.name
		
	def getCreationTime(self):
		return self.createdOn
		
	def getLastUpdatedTime(self):
		return self.lastUpdated
		
	def getLastAccessedTime(self):
		return self.lastAccessed
		
	def setLastUpdatedTime(self):
		self.lastUpdated = strftime("%Y-%m-%d %H:%M:%S", gmtime())	
	
	def setLastAccessedTime(self):
		self.lastAccessed =strftime("%Y-%m-%d %H:%M:%S", gmtime())
	
	def changeName(self,name):
		self.name = name
		
	def getName(self):
		return self.name
		
	def getTypeOfEntry(self):
		return type(self)
		
class Directory(fileSystem):
	def __init__(self,name,parent):
		super(Directory,self).__init__(name,parent)
		self.contents = []
		
	def addEntry(self,entry):
		self.setLastUpdatedTime()
		self.setLastAccessedTime()
		self.contents.append(entry)
	
	def deleteEntry(self,entry):
		self.setLastUpdatedTime()
		self.setLastAccessedTime()
		self.contents.remove(entry)
		
	def getContents(self):
		self.setLastUpdatedTime()
		self.setLastAccessedTime()
		return self.contents
		
	def size(self):
		sz =0
		for c in self.contents:
			if isinstance(c,Directory):
				sz = sz+c.size()
			else:
				sz = sz+c.size
		return sz
		
	def printContents(self):
		print self.size()
		for i in self.contents:
			print i.getFullPath(),i.getTypeOfEntry()
			if isinstance(i,Directory):
				i.printContents()
			
			
class File(fileSystem):
	def __init__(self,name,parent,size):
		super(File,self).__init__(name,parent)
		self.size = size
		self.content = None
		
	def setContents(self,content):
		self.setLastUpdatedTime()
		self.content = content
		
	def getContents(self):
		self.setLastAccessedTime()
		return self.content
		
	def size(self):
		return self.size
		
root = Directory("/",None)			
D1 = Directory("Pets",root)
root.addEntry(D1)
F= File("readme",D1,2)
D1.addEntry(F)
SB1 = Directory("Nines",D1)
SB2 = Directory("Birds",D1)
D1.addEntry(SB1)
D1.addEntry(SB2)
F1 = File("WhatIsAdog",SB1,15)
F2 = File("WhatIsACat",SB1,15)
SB1.addEntry(F1)
SB1.addEntry(F2)
F3 = File("WhatIsEagle",SB2,15)
F4 = File("WhatIsACuckoo",SB2,15)
SB2.addEntry(F3)
SB2.addEntry(F4)
D1.printContents()
	