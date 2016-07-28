from Tree import Tree
import math

def commonAncestor(p,q):
	l1 = depth(p)
	l2 = depth(q)

	delta = l1-l2

	shallow = delta>0 ? q:p
	deep = delta>0 ? p:q 
	
	diff = math.abs(delta) #move deeper node up by the difference in depths
	while (diff>0):
		deep = deep.parent
		diff=-1
	
	while (deep!=shallow and deep!=None and shallow!=None):
		deep= deep.parent
		shallow.parent
		
	return deep==None or shallow==None ? None:deep
		
		

def depth(node):
	count =0
	while node!=None:
		node = node.parent
		count+=1
	return count
	
	
#Time Complexity is O(d) where d is the depth of the deepest node