from LinkedList import LinkedList
from LinkedList import Node
	
class Result:
	res = False
	node = None
		
def isLLPalindromeRec(list,length):	
	if length<=0: #even number of items in list
		R = Result()
		R.node = list 
		R.res = True
		return R
	elif length ==1: #odd number of items in list
		R = Result()
		R.node = list.next 
		R.res = True
		return R
		
	R = isLLPalindromeRec(list.next,length-2)
	
	if not R.res or R.node==None:
		return R
		
	if R.node.data == list.data:
		R.node = R.node.next
		R.res = True
	else:
		R.res = False
			
	return R
	
	
lst1 = LinkedList(1)
lst1.add(2)
lst1.add(3)
lst1.add(2)
lst1.add(1)
lst1.display()
print isLLPalindromeRec(lst1.head,lst1.size()).res

lst2 = LinkedList(1)
lst2.add(2)
lst2.add(2)
lst2.add(1)
lst2.display()
print isLLPalindromeRec(lst2.head,lst2.size()).res

lst3 = LinkedList(1)
lst3.add(2)
lst3.add(3)
lst3.add(4)
lst3.display()
print isLLPalindromeRec(lst3.head,lst3.size()).res

lst4 = LinkedList(1)
lst4.add(2)
lst4.add(3)
lst4.add(1)
lst4.display()
print isLLPalindromeRec(lst4.head,lst4.size()).res