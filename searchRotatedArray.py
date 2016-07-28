def searchInARoatatedArray(Arr,low,high,x):
	if low<high:
		return -1
	
	mid = math.floor((low+high)/2)
	if Arr[mid]==x:
		return mid
		
	if Arr[low]<Arr[mid]: #try to search on left if possible
		if x>=Arr[low]and x<Arr[mid]:
			return searchInRotatedArray(Arr,low,mid-1)
		else:
			return searchInRotatedArray(Arr,mid+1,high)
	elif Arr[mid]>Arr[high]: #try to search on right if possible
		if x<=Arr[high] and x>Arr[mid]:
			return searchInRotatedArray(Arr,mid+1,high)
		else:
			return searchInRotatedArray(Arr,low,mid-1)
	
	else: #search on both sides
		res = searchInRotatedArray(Arr,low,mid-1)
		if res==-1:
			return searchInRotatedArray(Arr,mid+1,high)
		else:
			return res
			
Arr1 = [10,15,20,0,5]
searchInARoatatedArray(Arr1,0,4,0)
print Arr1
Arr2 = [50,5,20,30,40]
searchInARoatatedArray(Arr2,0,4,40)
print Arr2
Arr3 = [2,2,2,3,4,2]
searchInARoatatedArray(Arr3,0,5,4)
print Arr3
	