#no links to parent, if p and q are on same side keep looking on that side
#if p and q are on different sides of root, return root as it is the CA

def commonAncestor(root,p,q):
	if not covers(root,p) or not covers(root,q):
		return None
	elif covers(p,q):
		return p
	elif covers(q,p):
		return q
	else:
		return commonAncestorHelper(root,p,q)
	
def commonAncestorHelper(root,p,q):
	if root == None or p ==None or q==None:
		return root
		
	pIsOnLeft = covers(root.left,p)
	qIsOnLeft = covers(root.left,q)
	
	if pIsOnLeft!=qIsOnLeft:
		return root
		
	return pIsOnLeft==False ? commonAncestorHelper(root.right,p,q):commonAncestorHelper(root.left,p,q)
	



def covers(root,p):
	if root==None: return False
	elif root==p:return True
	else: return covers(root.left,p) or covers(root.right,p)