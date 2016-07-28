from LinkedList import LinkedList

def partition(llst,pivot):
	H = llst.head
	T = llst.head
	current = llst.head
	while current!=None:
		temp = current.next
		if current.data < pivot:
			#attach to head
			current.next = H
			H = current
			llst.head = H
		elif current.data >= pivot:
			#attach to tail
			T.next = current
			T = current
		current = temp
	T.next = None
	return llst
	
llst = LinkedList(1)
llst.add(2)
llst.add(10)
llst.add(5)
llst.add(8)
llst.add(5)
llst.add(3)

llst.display()
partition(llst,5)
llst.display()