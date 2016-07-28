from  Tree import BinarySearchTree

#Finding a successor has 3 cases
#Case I: if node has right child (or has both children): 
#successor is min on right subtree

#Case II: if node has no right child (but has one or no left child)
#If node is the left child of its parent, sucessor is the parent, other wise
#If node is the right child of its parent, 
# either the successor is None if Node is the rightmost in the tree, or it is the next untraversed parent
def successor(T,data):
	n = T._get(T.root,data)
	print n
	res = findSuccessor(n)
	return res.value


def findSuccessor(node):
	if node == None:
		return None
	if node.right!=None: #Case I
		succ = findMin(node.right)
	else: #Case II
		if node.parent.left == node:
			succ = node.parent
		elif node.parent.right == node:
			q = node
			x = q.parent
			while (x.left!=q):
				q=x
				x=x.parent
			succ = x
	return succ
		
		
def findMin(node):
	if node == None:
		return None
	while (node.left!=None):
		node = node.left
	return node
	
	
T = BinarySearchTree()
T.put(10)
T.put(5)
T.put(3)
T.put(7)
T.put(20)
T.put(15)
T.put(12)
T.put(17)
T.put(16)
T.put(25)
T.display()

print successor(T,17)