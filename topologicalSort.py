class Project:
	def __init__(self,name):
		self.children=[]
		self.map = {}
		self.name = name
		self.dependencies = 0
	
	def addChild(self,P):
		if P.getName() in self.map:
			self.map[P.getName()] = P
			self.incrementDependencies()
			self.addChildren(P)
			
	def incrementDependencies(self):
		self.dependencies+=1
	def decrementDependencies(self):
		self.dependencies-=1
	def getName(self):
		return self.name
	def getChildren(self):
		return self.children
	def addChildren(self,node):
		self.children.append(node)
	def numDependencies(self):
		return self.dependencies
		
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
	buildOrder = []
	toBeProcessed = 0
	EOL = addIndependentNodes(nodes,buildOrder,0)
	
	if len(buildOrder==0):
		return None
		
	while toBeProcessed < len(buildOrder):
		for c in buildOrder[toBeProcessed].children:
			c.decrementDependencies()
				
		EOL = addIndependentNodes(buildOrder[toBeProcessed].children,buildOrder,EOL)
		toBeProcessed+=1
	return buildOrder

def addIndependentNodes(nodes,buildOrder,offset):
	for n in nodes:
		if n.numDependencies() ==0:
			buildOrder[offset] = n
	
		
	
		
		
		