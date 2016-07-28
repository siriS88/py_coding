import sys
import math

def Merge(A,p,q,r):
	n1 = q-p+1
	n2 = r-q
	L=[]
	R=[]

	for i in range(0,n1):
		L.append(A[p+i])
	for j in range(0,n2):
		R.append(A[j+q+1])
	L.append(sys.maxint)
	R.append(sys.maxint)
	i=j=0
	for k in range(p,r+1):
		if L[i]<R[j]:
			A[k]=L[i]
			i=i+1
		elif R[j]<L[i]:
			A[k] = R[j]
			j=j+1

def mergeSort(A,p,r):

	if p<r:
		q = int(math.floor((p+r)/2))
		mergeSort(A,p,q)
		mergeSort(A,q+1,r)
		Merge(A,p,q,r)	
	
A = [9,6,5,0,8,2]
print A
mergeSort(A,0,len(A)-1)
print A