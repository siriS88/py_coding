from Tree import Node2

def createMinimalBST(arr,start,end):
	if end<start
		return None
		
	mid = int(math.floor(start+end)/2)
	n = Node2(arr[mid])
	n.left = createMinimalBST(arr[start:mid-1],start,mid-1)
	n.right = createMinimalBST(arr[mid+1:end],mid+1,end)
	return n
	

