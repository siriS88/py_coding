from LinkedList import LinkedList
import math

def sumLists1(lst1,lst2):
	
	current1 = lst1.head
	i = 0
	val1 =0
	while current1 !=None:
		val1 = val1+(10**i)*current1.data
		i=i+1 
		current1 = current1.next
	
	print val1
	
	current2 = lst2.head
	j = 0
	val2 =0
	while current2 !=None:
		val2 = val2+(10**j)*current2.data
		j=j+1 
		current2 = current2.next
	print val2
	
	S = str(val1+val2)
	
	numDigits = math.floor(math.log10(val1+val2))
	
	lst3 = LinkedList(int(S[numDigits-1]))
	for k in range(numdigits,1,-1):
		lst3.append(int(S[k]))
		
	return lst3





lst1 = LinkedList(6)
lst1.add(1)
lst1.add(7)

lst2 = LinkedList(2)
lst2.add(9)
lst2.add(5)

print sumLists1(lst1,lst2)