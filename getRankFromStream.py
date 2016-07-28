
class Node:
	def __init__(self,data):
		self.value = data
		self.left = None
		self.right = None
		self.leftSize =0
		
class BinarySearchTree:
	def __init__(self):
		self.root = None
		
	def isTreeEmpty(self):
		return self.root==None
	
	def insert(self,data):
		if self.isTreeEmpty():
			self.root = Node(data)
		else:
			self._insert(self.root,data)
		
	def _insert(self,node,data):
		if data <= node.value: #browse the left subtree
			if node.left!=None:
				self._insert(node.left,data)
			else:
				node.left = Node(data)
			node.leftSize+=1
		elif data > node.value: #browse the right subtree
			if node.right!=None:
				self._insert(node.right,data)
			else:
				node.right = Node(data)
				
def track(x,T):
	if x==None:
		return
	else:
		T.insert(x)
	return T

def getRankOfNumber(x):
	return getRank(root,x)
	
def getRank(node,x):
	if node==None:
		return -1
	if node.value == x:
		return node.leftSize
	elif x<node.value:
		return getRank(node.left,x)	
	elif x>node.value:
		if node.right == None:
			return -1
		else:
			return getRank(node.right,x)+1+node.leftSize
			
			
			
			
T = BinarySearchTree()
track(5,T)
track(1,T)
track(4,T)
track(4,T)
track(5,T)
track(9,T)
track(7,T)
track(13,T)
track(3,T)

print getRank(T.root,9)
