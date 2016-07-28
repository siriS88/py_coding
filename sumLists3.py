from LinkedList import LinkedList
from LinkedList import Node
	
class partialSum:
	n = Node(0)
	carry = 0
	
	
def sumLists3(list1,list2,pSum):

	if list1 == None and list2 == None and pSum.carry ==0:
		return None
		
	value = pSum.carry
	if list!=None:
		value = value + list1.data
		
	if list2!=None:
		value = value+list2.data
	
	newPSum = partialSum()
	newPSum.n = Node(value%10)
	newPSum.carry = value/10
		
	if list1!=None or list2!=None: #go till the end of both lists
		next_res = 	sumLists3(None if list1==None else list1.next, None if list2==None else list2.next,newPSum)
	res = Node(newPSum.n.data)
	res.next = next_res
	
	return res
	
lst1 = LinkedList(6)
lst1.add(1)
lst1.add(7)

lst2 = LinkedList(2)
lst2.add(9)
lst2.add(5)

i_p = partialSum()

b = sumLists3(lst1.head,lst2.head,i_p)

while b!=None:
	print b.data,"->",
	b = b.next