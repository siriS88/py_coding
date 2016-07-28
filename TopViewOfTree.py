import Queue
class Node:
	def __init__(self,data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right	
		
class QItem:
	def __init__(self,node,hd):
		self.node = node
		self.hd =hd
		
def topViewOfTree(root):
	q = Queue.Queue()
	q.put(QItem(root,0))
	map = {}
	map[0] = [root]
	print root.data," ",
	while not q.empty():
		n = q.get()
		node = n.node
		hd = n.hd
		if hd not in map:
			print node.data," ",
			map[hd] = [node]
		else:
			map[hd].append(node)
			
		if node.left:
			q.put(QItem(node.left,hd+1))
		if node.right:
			q.put(QItem(node.right,hd-1))
			

			
#Create following Binary Tree
#            1
#          /  \
#         2    3
#          \
#           4
#            \
#             5
#              \
#               6
root = Node(1);
root.left = Node(2);
root.right = Node(3);
root.left.right = Node(4);
root.left.right.right = Node(5);
root.left.right.right.right = Node(6);

topViewOfTree(root)