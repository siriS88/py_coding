from LinkedList import LinkedList
from LinkedList import Node

def LoopDetection(list):

	p1 = list
	p2 = list
	isThereALoop = False
	
	while p1!=None and p2 !=None:
		p1=p1.next.next
		p2=p2.next
		if p1 is p2:
			isThereALoop = True
			break
	
	if isThereALoop:
		p1 = list
		while p1 is not p2:
			p1 = p1.next
			p2 = p2.next
		
		return p1
	
	else:
		return None
		

			
N1 = Node(5)
N2 = Node(56)
N3 = Node(45)
N4 = Node(90)
N5 = N3

N1.setNext(N2)
N2.setNext(N3)
N3.setNext(N4)
N4.setNext(N5)

print N1.data,"->",N2.data,"->",N3.data,"->",N4.data,"->",N5.data

print LoopDetection(N1).data
		
			
			
			