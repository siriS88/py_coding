from LinkedList import LinkedList
from LinkedList import Node

def sumLists2(list1,list2,carry):

	if list1 == None and list2 == None and carry ==0:
		return None
		
	value = carry
	if list!=None:
		value = value + list1.data
		
	if list2!=None:
		value = value+list2.data
		
	res = Node(value%10)
	
	if list1!=None or list2!=None: #go till the end of both lists
		next_res = 	sumLists2(None if list1==None else list1.next, None if list2==None else list2.next,1 if value>=10 else 0)
		
	res.next = next_res
	
	return res
	
lst1 = LinkedList(6)
lst1.add(1)
lst1.add(7)

lst2 = LinkedList(2)
lst2.add(9)
lst2.add(5)

b = sumLists2(lst1.head,lst2.head,0)

while b!=None:
	print b.data,"->",
	b = b.next