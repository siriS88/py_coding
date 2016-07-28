import math
class coord:
	def __init__(self):
		self.row = 0
		self.col = 0
		
	def returnMidRowAndCol(self,dest_coord):
		mid_coord = coord()
		mid_coord.row = int(math.floor((self.row+dest_coord.row)/2))
		mid_coord.col = int(math.floor((self.col+dest_coord.col)/2))
		return mid_coord
	
	def isBefore(self,dest_coord):
		return self.row>dest_coord.row and self.col>dest_coord.col
		
	def isIndexOutOfBounds(self,numRows,numCols):
		return self.row>numRows or self.col>numCols
		
def matrixSearch(M,origin_coord,dest_coord,val):
	if origin_coord.isIndexOutOfBounds(len(M)-1,len(M[0])-1) or dest_coord.isIndexOutOfBounds(len(M)-1,len(M[0])-1):
		return -1
	if origin_coord.isBefore(dest_coord):
		return -1
	
	start = coord()
	end = coord()
	start = origin_coord
	diagDist = min([dest_coord.row-origin_coord.row,dest_coord.col-origin_coord.col])
	end.row = start.row+diagDist
	end.col = start.col+diagDist
	
	while start.isBefore(end):
		mid = start.returnMidRowAndCol(end)
		print mid.row,mid.col
		if val>M[mid.row][mid.col]:
			start.row = mid.row+1
			start.col = mid.col+1
		elif val<M[mid.row][mid.col]:
			end.row = mid.row-1
			end.col = mid.col-1
		elif val==M[mid.row][mid.col]:
			return (mid.row,mid.col)
	partitionAndSearch(M,origin_coord,dest_coord,start,val)		
	
def partitionAndSearch(M,origin,dest,pivot,val):
	lowerLeftOrigin = coord()
	lowerLeftDest = coord()
	upperRightOrigin = coord()
	upperRightDest = coord()
	
	lowerLeftOrigin.row = pivot.row
	lowerLeftOrigin.col = origin.col
	lowerLeftDest.row = dest.row
	lowerLeftDest.col = pivot.col-1
	
	upperRightOrigin.row = origin.row
	upperRightOrigin.col = pivot.col
	upperRightDest.row = pivot.col-1
	upperRightDest.col = dest.col
	res = matrixSearch(M,lowerLeftOrigin,lowerLeftDest,val)
	if res == -1:
		matrixSearch(M,upperRightOrigin,upperRightDest,val) 
		
		
M = [[15,20,40,85],[20,35,80,95],[30,55,95,105],[40,80,100,120]]
origin_coord = coord()
origin_coord.row = 0
origin_coord.col =0
dest_coord = coord()
dest_coord.row = len(M[0])-1
dest_coord.col = len(M[0])-1
print matrixSearch(M,origin_coord,dest_coord,55)	
	


	