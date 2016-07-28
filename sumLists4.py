from LinkedList import LinkedList
from LinkedList import Node
	
class partialSum:
	n = Node(None)
	carry = 0
	
def sumLists4(list1,list2):
	
	def insertBefore(listNode,data):
		newNode = Node(data)
		if listNode !=None:
			newNode.next = listNode
		return newNode
	
	def padZeros(list,num):
		newHead = list.head
		for n in range(0,num):
			newHead = insertBefore(newHead,0)
		return newHead
	
	def sumListsHelper(n1,n2):
		if n1==None and n2==None:
			p_sum = partialSum() #create an partial sum node that is None and has 0 carry at the end of both lists
			return p_sum
		
		res = sumListsHelper(n1.next,n2.next) #recurse to the end of both lists 
		val = n1.data+n2.data+res.carry
		full_result = partialSum()
		full_result.n = insertBefore(res.n,val%10)
		full_result.carry = val/10
		return full_result
	
	
	length1 = list1.size()
	length2 = list2.size()
	
	if length1 < length2:
		list1 = padZeros(list1,length1-length2)
	elif length1>length2:
		list2 = padZeros(list2,length2-length1)

	fsum = sumListsHelper(list1.head,list2.head)
	
	if fsum.carry == 0:
		return fsum.n 
	elif fsum.carry==1:
		newNode = Node(0)
		newNode = insertBefore(fsum.n,1)
		return newNode
	

lst1 = LinkedList(7)
lst1.add(1)
lst1.add(6)

lst2 = LinkedList(5)
lst2.add(9)
lst2.add(2)

b = sumLists4(lst1,lst2)

while b!=None:
	print b.data,"->",
	b = b.next

