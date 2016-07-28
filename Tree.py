class Node1:
	def __init__(self):
		self.name = ''
		self.children = []

class Tree:
	def __init__(self):
		self.root = Node1()
		
class Node2:
	def __init__(self,data):
		self.value = data
		self.left = None
		self.right = None
		self.parent = None
		
	def hasLeftChild(self):
		val = False
		if self.left !=None:
			val = True 
		return val
		
	def hasRightChild(self):
		val = False
		if self.right !=None:
			val = True 
		return val
		
	def hasBothChildren(self):
		return (self.left!=None and self.right!=None) 
	
	def isLeafNode(self):
		return (not self.hasLeftChild()) and (not self.hasRightChild())
	
	def isRightChild(self):
		return self.parent.right==self
		
	def isLeftChild(self):
		return self.parent.left==self
			
		
class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size =0
			
	def isTreeEmpty(self):
		return self.root==None
	
	def treeSize(self):
		return self.size()
	
	def put(self,data):
		if self.isTreeEmpty():
			self.root = Node2(data)
		else:
			self._put(self.root,data)
		self.size+=1
		
	def _put(self,node,data):
		if data < node.value: #browse the left subtree
			if node.hasLeftChild():
				self._put(node.left,data)
			else:
				node.left = Node2(data)
				node.left.parent = node
		elif data > node.value: #browse the right subtree
			if node.hasRightChild():
				self._put(node.right,data)
			else:
				node.right = Node2(data)
				node.right.parent = node
				
	def __contains__(self,data):
		if self.get(data):
			return True
		else:
			return False

	def get(self,data):
		res=None
		if self.isTreeEmpty():
			raise NameError("Cannot get from an empty tree")
		else:
			res = self._get(self.root,data) 
		if res !=None:
			return False
		else:
			return True
			
	def _get(self,currentNode,data):
		if currentNode==None:
			return None 
		elif currentNode.value==data:
			return currentNode
		elif data<currentNode.value:
			self._get(currentNode.left,data)
		elif data>currentNode.value:
			self._get(currentNode.right,data)	
			
	def delete(self,data):
		self._delete(data,self.root)
	
	def _delete(self,data,node):
		n = self._get(node,data)
		print n
		if n == None:
			raise NameError("Cannot delete a non existent node")
		if n.isLeafNode: #case I: no children
			if n.isRightChild():
				n.parent.right = None
				n.parent = None
			else:
				n.parent.left = None
				n.parent = None
		elif not n.hasBothChildren(): #case II: only one child
			if n.isRightChild():
				if n.hasRightChild():
					n.parent.right = n.right
					n.right.parent = n.parent 
				else:
					n.parent.right = n.left
					n.left.parent = n.parent 
			else:
				if n.hasRightChild():
					n.parent.left = n.right
					n.right.parent = n.parent
				else:
					n.parent.left = n.left
					n.left.parent = n.parent
		else:# case III: has both children
			minInRightST = self.findMin(n.right)
			n.value = minInRightST.value
			self.delete(minInRightST.value,n.right) #delete the duplicate min value in the right subtree of node
				
		
	def findMin(self,node):
		current = node
		while current!=None and current.left!=None:
				current = current.left
		return current
					
	def inOrderTraversal(self,node):
		if node !=None:
			self.inOrderTraversal(node.left)
			self.visit(node)
			self.inOrderTraversal(node.right)

	def preOrderTraversal(self,node):
		if node!=None:
			self.visit(node)
			self.preOrderTraversal(node.left)
			self.preOrderTraversal(node.right)
	
	def postOrderTraversal(self,node):
		if node!=None:
			self.postOrderTraversal(node.left)
			self.postOrderTraversal(node.right)
			self.visit(node)
			
	def visit(self,node):
		print node.value,"->",
		
	def display(self):
		self.inOrderTraversal(self.root)
		print("/n")
		self.preOrderTraversal(self.root)
		print("/n")
		self.postOrderTraversal(self.root)
		print("/n")
		
		
#T = BinarySearchTree()
#T.put(10)
#T.put(5)
#T.put(3)
#T.put(7)
#T.put(20)
#T.put(15)
#T.put(25)
#T.display()

#print T.get(7)
#print 7 in T

#T.delete(7)
#T.display()
#T.delete(5)
#T.display()
#T.delete(20)
