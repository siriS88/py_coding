from LinkedList import LinkedList
from LinkedList import Node

class Index:
	def __init__(self):
		self.val=0

def KthToLast(llst,k):
	p1 = llst.head
	p2 = llst.head
	count =1
	while p1!=None and count <k:
		p1 = p1.next
		count = count +1
	
	while p1.next!=None:
		
		p1=p1.next
		p2 = p2.next
		print "Howdy",p2.data
		
	return p2.data
	
def KthToLastRecursive(head,k):
	if head == None:
		return 0
	index = KthToLastRecursive(head.next,k) +1
	if index == k:
		print "Kth To last element is:",head.data
	return index
	
def KthToLastRecursive2(head,k,i):
	if head ==None:
		return None
	node = Node(KthToLastRecursive2(head.next,k,i))
	i.val=i.val+1
	if i.val==k:
		print "KthToLast element is:",head.data
		return head
	return node
			
llst = LinkedList(10)
llst.add(3)
llst.add(4)
llst.add(100)
llst.add(5)
llst.add(6)
llst.add(600)
llst.add(7)

llst.display()
print KthToLast(llst,2)
i = Index
print KthToLastRecursive(llst.head,2)
print KthToLastRecursive2(llst.head,2,i)