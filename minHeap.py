import math

class minHeap():
	def __init__(self):
		self.Heap = []
		self.size = 0
		self.root = None
	
	def setupHeap(self,arr):
		self.Heap = arr
		self.size = len(arr)
		self.root=arr[0]
		self.buildHeap()
		
	def minHeapify(self,i):
		l = 2*i+1 #additional 1 for 0 based indexing
		r = 2*i+2
		smallest =i
		if (l<self.size and self.Heap[l]<self.Heap[i]):
			smallest = l

		if (r<self.size and self.Heap[r]<self.Heap[smallest]):
			smallest = r
			
		if smallest !=i:
			temp = self.Heap[i]
			self.Heap[i] = self.Heap[smallest]
			self.Heap[smallest]=temp
			self.minHeapify(smallest)
				
	def buildHeap(self):
		s = int(math.floor(self.size/2))-1
		while s>=0:
			self.minHeapify(s)
			s -=1
		return self.Heap
			
	def insert(self,value):
		self.Heap.append(value)
		self.size+=1
		i = self.size-1 #point i to where the new element is added
		parent = int(math.floor((i-1)/2))
		while (i>0 and self.Heap[i]<self.Heap[parent]):
			#current node is less than its parent, so swap them
			temp = self.Heap[parent]
			self.Heap[parent] = self.Heap[i]
			self.Heap[i] = temp 
			i=parent #move up to parent
			parent = int(math.floor((i-1)/2)) #update parent to its parent so that while loop comparison is correct
			
	def deleteMin(self):
		min = self.Heap[0]
		self.Heap[0] = self.Heap[self.size-1]
		del(self.Heap[self.size-1])
		self.size-=1
		self.minHeapify(0)
		return min
	
	def decreaseKey(self,i,value):
		if self.Heap[i]<value:
			raise NameError("Aborting decreaseKey as value in heap is lower than what you want to decrease it to")
		self.Heap[i] = value
		parent = int(math.floor((i-1)/2))
		while (i>0 and self.Heap[i]<self.Heap[parent]):
			temp = self.Heap[parent]
			self.Heap[parent] = self.Heap[i]
			self.Heap[i] = temp 
			i=parent #move up to parent
			parent = int(math.floor((i-1)/2))
			
	def display(self):
		print self.Heap
		
		
H = minHeap()
H.setupHeap([14,16,10,8,7,9,6,2,4,1])
H.display()
print H.deleteMin()
H.display()
H.decreaseKey(5,1)
H.display()
H.insert(3)
H.display()