from queue import Queue

class Node:
	def __init__(self,data):
		self.value =data
		self.children = []
		self.visited = False
		self.marked = False
		self._preorder = 0
		self._postorder =0
		self._prev = None
		self.distance=0
		self.weightsOfChildren=[]
		self.index =0
		self.name = " "
	
class Graph:
	def __init__(self):
		self.nodes = []
		self.adjList = []
		self._clock=0
	
	def addToGraph(self,node):
		if node!=None:
			self.nodes.append(node)
			l = node.children
			self.adjList.append(l)
			
	def DFS(self):
		for node in self.nodes:
			if not node.visited:
				self.search(node)
			
	def search(self,node):
		if node == None:
			return None
		else:
			node.visited = True
			print node.value,"->",
			self._clock+=1
			self._preorder = self._clock
			for n in node.children:
				if n.visited == False:
					self.search(n)
			self._clock+=1
			self._postorder = self._clock
					
	def BFS(self):
		self.BFS_Search(self.nodes[0])
	
	def BFS_Search(self,node):
		q=Queue()
		node.distance =0
		node.prev=None
		#print node.value,"->",
		q.add(node)
		while not q.isEmpty():
			u = q.remove()
			if not u.marked:
				print u.value,"->",
			u.marked = True
			for n in u.children:
				if not n.marked:
					n.distance = u.distance+1
					n.prev = u
					q.add(n)
					
#g = Graph()
#a = Node(0)
#b = Node(1)
#c = Node(5)
#d = Node(4)
#e = Node(3)
#f = Node(2)
#a.children = [b,d,c]
#b.children = [d,e]
#c.children = []
#d.children = []
#e.children = [f,d]
#f.children = [b]

#g.addToGraph(a)
#g.addToGraph(b)
#g.addToGraph(c)
#g.addToGraph(d)
#g.addToGraph(e)
#g.addToGraph(f)

#g.DFS()
#print "/n"
#g.BFS()
#print "/n"