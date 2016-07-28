from Tree import BinarySearchTree

def validateBST(node,min,max):
	if node == None:
		return True
		
	if(min!=None and node.value<min) or (max!=None and node.value>max):
		return False
	
	if (not validateBST(node.left,None,node.value) and not validateBST(node.right,node.value,None)):
		return False
		
	return True
	
T = BinarySearchTree()
T.put(10)
T.put(5)
T.put(3)
T.put(7)
T.put(20)
T.put(15)
T.put(25)
T.display()

print validateBST(T.root,None,None)

