
def sortPeaksAndValleys(Array):
	i=0
	while i<len(Array):
		LI = findLargestIndex(Array,i-1,i+1)
		if LI != i:
			swap(Array,i,LI)
		i=i+2
			
def findLargestIndex(Array,startI,endI):
	if startI<0:
		startI=0
		endI=endI+1
	elif endI>len(Array)-1:
		endI = len(Array)-1
		startI = startI-1
	
	max = None
	maxI = startI
	for i in range(startI,endI+1):
		if Array[i]>max:
			max = Array[i]
			maxI = i
	return maxI
	
def swap(Array,x,y):
	temp = Array[x]
	Array[x]=Array[y]
	Array[y] = temp
	
	
Arr = [5,3,1,2,3]
sortPeaksAndValleys(Arr)
print Arr			

Arr = [9,1,0,4,8,7]
sortPeaksAndValleys(Arr)
print Arr	