from Tree import Tree

def commonAncestor(root,p,q):
	if not covers(root,p) or not covers(root,q): #if either of the nodes are not found in the tree
		return None
	elif covers(p,q):
		return p
	elif covers(q,p):
		return q

	parent = p.parent
	sibling = getSibling(parent,p)
	while not covers(sibling,q):
		currSib = parent
		parent=parent.parent
		sibling = getSibling(parent,currSib)
	return parent	
	
def covers(root,p):
	if root==None: return False
	elif root==p:return True
	else: return covers(root.left,p) or covers(root.right,p)
	
def getSibling(parent,currChild):
	return parent.left==currentChild ? parent.right:parent.left	