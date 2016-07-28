from Tree import BinarySearchTree

def containsTree(T1,T2):
	if T2.root==None:
		return True
	else:
		return isSubtree(T1.root,T2.root)
		
def isSubtree(r1,r2):
	if r1 == None:
		return False
	elif ((r1.value == r2.value) and matched(r1,r2)):
		return True
	else:
		return isSubtree(r1.left,r2) or isSubtree(r1.right,r2)
		
def matched(r1,r2):
	if r1==None and r2==None:
		return True
	elif r1==None or r2==None:
		return False
	elif r1.value!=r2.value:
		return False
	else:
		return matched(r1.left,r2.left) and matched(r1.right,r2.right)
		
#############################################################		

def containsTree2(T1,T2):
	str1 = ''
	str2 = ''
	getOrderString(T1.root,str1)
	getOrderString(T2.root,str2)
	
	if str2 in str1:
		return True
	else:
		return False
	

def getOrderString(r,string):
	if r == None:
		string =  string + "X"
	else:
		string = string + str(r.value)
		getOrderString(r.left,string)
		getOrderString(r.right,string)
	

T1 = BinarySearchTree()
T1.put(10)
T1.put(5)
T1.put(3)
T1.put(7)
T1.put(20)
T1.put(15)
T1.put(25)

T2 = BinarySearchTree()
T2.put(5)
T2.put(3)
T2.put(7)

T3 = BinarySearchTree()
T3.put(5)
T3.put(6)
T3.put(7)

print containsTree(T1,T2)
print containsTree2(T1,T2)

print containsTree2(T1,T3)
print containsTree2(T1,T3)
		