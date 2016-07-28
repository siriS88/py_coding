def insertionSort(A):
	for j in range(1,len(A)):
		key = A[j]
		#insert A[j] into sorted sequence A[1...j-1]
		i=j-1
		while(i>=0 and A[i]>key):
			A[i+1]=A[i]
			i=i-1
		A[i+1] = key
		
A = [9,6,5,0,8,2]
print A
insertionSort(A)
print A