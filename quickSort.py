def partition(A,p,r):
	key=A[r]
	i=p-1
	for j in range(p,r):
		if A[j]<key:
			i=i+1
			swap(A,i,j)
	swap(A,i+1,r)
	return i+1
	
def swap(A,index1,index2):
	temp = A[index1]
	A[index1]=A[index2]
	A[index2]=temp
	
def quickSort(A,p,r):
	if p<r:
		q = partition(A,p,r)
		quickSort(A,p,q-1)
		quickSort(A,q+1,r)
		
A = [9,6,5,0,8,2]
print A
quickSort(A,0,len(A)-1)
print A
		
		