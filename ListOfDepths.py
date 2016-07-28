from Tree import BinarySearchTree

def listOfDepths_REC(node,resultList,level):
	if node==None:
		return resultList
	if level == len(resultList): #list is not in this level
		list = []
		list.append(node)
		resultList.append(list)
	else:
		resultList[level].append(node)
	
	resultList = listOfDepths_REC(node.left,resultList,level+1)
	resultList = listOfDepths_REC(node.right,resultList,level+1)
	return resultList

def listOfDepths(root):
	root.marked = True
	result =[]
	parents = []
	parents.append(root)
	
	while not len(parents)==0:
		result.append(parents)
		currentList =[]
		for p in parents:
			if p.left!=None: 
				currentList.append(p.left)
			if p.right !=None:
				currentList.append(p.right)
		parents = currentList
	return result

T = BinarySearchTree()
T.put(10)
T.put(5)
T.put(3)
T.put(7)
T.put(20)
T.put(15)
T.put(25)
#T.display()
result= listOfDepths(T.root)
for level in result:
	for nodes in level: 
		print nodes.value,"->",
	print " "

resultList = []
listOfDepths_REC(T.root,resultList,0)
for level in resultList:
	for nodes in level: 
		print nodes.value,"->",
	print " "


