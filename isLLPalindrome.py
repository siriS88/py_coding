from LinkedList import LinkedList
from LinkedList import Node
	
def reverseALinkedList(list):
	curr = list.head
	revList = None
	while curr!=None:
		revList = insertBefore(revList,curr.data)
		curr = curr.next
	return revList

def insertBefore(node,data):
	newN = Node(data)
	newN.next = node
	return newN
		
def isLLPalindrome1(list):
	revL = reverseALinkedList(list)
	isPalindrome = True
	fList = list.head
	while revL!=None:
		print revL.data,"->",
		if fList.data != revL.data:
			isPalindrome = False
		revL = revL.next
		fList = fList.next
	return isPalindrome
	
lst1 = LinkedList(1)
lst1.add(2)
lst1.add(3)
lst1.add(2)
lst1.add(1)
lst1.display()
print isLLPalindrome1(lst1)