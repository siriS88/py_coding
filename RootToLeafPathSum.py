class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		
def RootToLeafSum(node,currSum, targetSum):
	if node == None:
		return False
	currSum = currSum + node.data
	if node.left == None and node.right == None: #leafNode
		return currSum == targetSum
	
	LS = RootToLeafSum(node.left,currSum,targetSum)
	RS = RootToLeafSum(node.right,currSum,targetSum)
	return LS or RS
	

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

print RootToLeafSum(n1,0,4)