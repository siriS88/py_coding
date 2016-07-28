#A is big enough to hold B also
def merge2Arrays(A,B,indexA,indexB):
	indexMerged = indexA+indexB-1
	indexA=indexA-1
	indexB=indexB-1

	while indexB >=0:
		if indexA>=0 and A[indexA]>B[indexB]:
			A[indexMerged] = A[indexA]
			indexA-=1
		elif B[indexB]>A[indexA]:
			A[indexMerged] = B[indexB]
			indexB-=1
		indexMerged-=1
	return A
	
	
A = [2,5,7,8,0,0,0,0]
B = [1,3,4]
print merge2Arrays(A,B,4,3)