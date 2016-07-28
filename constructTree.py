def constructTree(Inorder,Preorder):
	root = Preorder[0]
	[L_In,R_In] = getLRIn(Inorder,root)
	if L_In:
		L_Pre = Preorder[1:len(L_In)+1]
		root.left = constructTree(L_In,L_Pre)

	if R_In:
		R_Pre = Preorder[-len(R_In):]
		root.right = constructTree(R_In,R_Pre)
	return root
	
	
def getLRIn(Inorder,root):
	L_In = []
	R_In = []
	seenRoot = False
	for i in Inorder:
		if i!=root and not seenRoot:
			L_In.append(i)
		elif i!=root and seenRoot:
			R_In.append(i)
		elif i==root:
			seenRoot = True
	return L_In,R_In
	
Inorder = ["E", "A", "C", "K", "F", "H", "D", "B", "G"]
Preorder = ["F", "A", "E", "K", "C", "D", "H", "G", "B"]

constructTree(Inorder,Preorder)
	