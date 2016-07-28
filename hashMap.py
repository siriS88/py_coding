class hashMap:
	def __init__(self,size):
		self.slots = [None]*size
		self.data = [None]*size
		
	def put(self,key,value):
		index = self.hashFunction(key)
		if self.slots[index] == None:
			self.slots[index] = key
			self.data[index] = value
		elif self.slots[index] == key:
			self.data[index] = value
		else:
			while self.slots[index] !=None and self.slots[index]!=key:
				index = self.rehash(index)
			if self.slots[index] == None:
				self.slots[index] = key
				self.data[index] = value		
			else:
				self.data[index] = value
				
	def hashFunction(self,key):
		return key%len(self.slots)
		
	def rehash(self,oldHash):
		return (oldHash+1)%len(self.slots)
		
	def get(self,key):
		index = self.hashFunction(key)
		startIndex = index
		stop = False
		data = None
		
		if self.slots[index] == key:
			data = self.data[index]
		else:
			while self.slots[index]!=key and not stop:
				index = self.rehash(index)
				if index == startIndex:
					stop = True
				elif self.slots[index] == key:
					data =  self.data[index]	
		return data
		
	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,data):
		self.put(key,data)
		
	def __len__(self):
		return len(self.slots)
		
	def delete(self,key):
		index = self.hashFunction(key)
		startIndex = index
		stop = False
		data = None
		
		if self.slots[index] == key:
			del(self.slots[index])
			del(self.data[index])
		else:
			while self.slots[index]!=key and not stop:
				index = self.rehash(index)
				if index == startIndex:
					stop = True
					print "Iem not found in hashMap"
				elif self.slots[index] == key:
					del(self.slots[index])
					del(self.data[index])	
					
	def __contains__(self,item):
		value = self.get(item)
		if value == None:
			return False
		else:
			return True
	
	def display(self):
		for i in range(len(self.slots)):
			print self.slots[i],self.data[i]
			
#map = hashMap(11)
#map.put(20,"Lion")
#map.put(45,"Tiger")
#map.put(56,"Lemur")
#map.put(102,"Dog")
#map.put(456,"Monkey")
#map.put(345,"Bee")
#map.put(678,"Bear")
#map.put(23,"Kiwi")
#map.display()

#print " "
#print map.get(456) 
#print " "
#print map[354]
#print " " 
#print len(map) 
#print " "

#map[23] = "Cat"

#map.delete(678)
#map.display()
#print " "
#print 23 in map
#print " "
#print 100 in map
#print " "		
		