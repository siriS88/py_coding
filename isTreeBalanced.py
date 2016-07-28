from Tree import BinarySearchTree

def checkHeight(node):
	if node == None: #base case of recursion
		return -1
	
	L_H = checkHeight(node.left)
	if L_H == -10**8: return -10**8 #early return from recursion backtrack
	
	R_H = checkHeight(node.right)
	if R_H == -10**8: return -10**8 #early return from recursion backtrack
	
	maxH = max(L_H,R_H)+1
	diff = int(abs(L_H-R_H))
	
	if diff>1:
		return -10**8 #pass an error back up
	else:
		return maxH
		
def isTreeBalanced(T): #balanced means diff between left height and right height
# of any subtree is less than or equal to 1
	return checkHeight(T.root)!=-10**8
	
	
	
		
T = BinarySearchTree()
T.put(10)
T.put(5)
T.put(3)
T.put(7)
T.put(20)
T.put(15)
T.put(25)

print isTreeBalanced(T)


		
T = BinarySearchTree()
T.put(10)
T.put(5)
T.put(3)
T.put(16)
T.put(20)
T.put(15)
T.put(25)
T.put(45)
T.put(60)

print isTreeBalanced(T)