class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		
def printpathsFromRootToLeaf(node,path,pathLen):
	if node == None:
		return
	path.append(node.data)
	pathLen+=1
	if node.left == None and node.right == None:
		for n in path:
			print n," ",
		print " "
	else:
		printpathsFromRootToLeaf(node.left,path,pathLen)
		printpathsFromRootToLeaf(node.right,path,pathLen)
		
def printpathsFromRootToLeaf2(node,string):
	if node == None:
		return

	if node.left == None and node.right == None:
		nodeVal = node.data
		print string+" "+str(nodeVal)
	else:
		val = node.data
		printpathsFromRootToLeaf2(node.left,string+" "+str(val))
		printpathsFromRootToLeaf2(node.right,string+" "+str(val))
		
		
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

printpathsFromRootToLeaf(n1,[],0)
printpathsFromRootToLeaf2(n1,"")
			