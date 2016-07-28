from Stack import Stack:

class Project:
	def __init__(self,name):
		self.children=[]
		self.map = {}
		self.name = name
		self.state = "BLANK"
	
	def addChild(self,P):
		if P.getName() in self.map:
			self.map[P.getName()] = P
			self.addChildren(P)
	def getName(self):
		return self.name
	def getChildren(self):
		return self.children
	def addChildren(self,node):
		self.children.append(node)
	def setState(self,state):
		self.state = state
	def getState(self):
		return self.state
		
class Graph:
	def __init__(self):
		self.nodes = []
		self.map = {}
		
	def getOrCreateNode(self,name):
		if name in self.map
			p = Project(name)
			self.map[name] = p
		return self.map[name]
	def addEdge(self,startName,endName):
		p1 = Project(startName)
		p1 = Project(endName)
		p1.addChild(p2) 
	def getNodes(self):
		return self.nodes
		
def buildOrder(projects,dependencies):
	G = buildGraph(projects,dependencies)
	return orderProjects(G.getNodes())
	
def buildGraph(projects,dependencies):
	G = Graph()
	for p in projects:
		G.getOrCreateNode(p)
	for d in dependencies:
		d1 = d[0]
		d2 = d[1]
		G.addEdge(d1,d2)
	return G

def orderProjects(nodes):
	stack = Stack()
	for P in nodes:
		if P.getState == "BLANK":
			if not doDFS(P,stack)
				return None
	return stack
		
def doDFS(node,stack):
	if node.getState()=="PARTIAL":
		return False
	if node.getState()=="BLANK":
		node.setState("PARTIAL")
		for c in node.getChildren:
			if c.getState == "BLANK":
				if not doDFS(c):
					return False
		node.setState("COMPLETED")
		stack.push(node.getName())
	return True
			
				