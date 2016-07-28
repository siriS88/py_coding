class Node:
	def __init__(self,data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right		

def verticalOrder(root):
	map = {}
	_verticalOrder(root,map,0)
	for key in sorted(map):
		for ns in map[key]:
			print ns.data, " ",
		print " "

def _verticalOrder(node,map,hd):
	if node == None: return
	if hd not in map:
		map[hd] = [node]
	else:
		map[hd].append(node)
		
	_verticalOrder(node.left,map,hd-1)	
	_verticalOrder(node.right,map,hd+1)
		
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
verticalOrder(root)
