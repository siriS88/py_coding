from LinkedList import LinkedList
from LinkedList import Node

def LinkedListIntersection(list1,list2):
	#see if the two lists intersect by comparing their tails
	curr1 = list1.head
	curr2 = list2.head
	
	while curr1.next!=None:
		curr1 = curr1.next
			
	while curr2.next!=None:
		curr2 = curr2.next
			
	if curr1==curr2:
		isThereIntersection = True
		print "Lists Intersect!!"
	else:
		isThereIntersection = False
		print "Lists Don't Intersect"
		
	if isThereIntersection:
		length1 = list1.size()
		length2 = list2.size()
		#increment the longer list head pointer by diff in lengths
		p1 = list1.head
		p2 = list2.head
		if length1>length2:
			for i in range(0,length1-length2):
		 		p1 = p1.next
		else:
			for i in range(0,length2-length1):
				p2 = p2.next
		
		while p1!=p2:
			p1=p1.next
			p2= p2.next
		return p1
			

lst1 = LinkedList(56)
lst1.add(3)
lst1.add(600)
lst1.add(6)
lst1.add(34)
lst1.display()

lst2 = LinkedList(56)
lst2.add(3)
lst2.add(600)
lst2.add(5)
lst2.add(7)
lst2.add(89)
lst2.display()

outNode = LinkedListIntersection(lst1,lst2)
if outNode!=None:
	print outNode.data
else:
	print None
