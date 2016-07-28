def RotateMatrix(M,n):
	T = 0
	R = n-1
	L = n-1
	B = 0
	layer = 0
	
	while T<=L and B<=R:
		
		temp = list()
		for i in range(B,R+1): 
			temp.append(M[B][i]) #top = temp
			M[T][i] = M[L-i+layer][B] #top = left
			
		for j in range(T,L+1):
			M[j][T] = M[L][j] #left = bottom
			
		for k in range(B,R+1):
			M[L][k] = M[L-k+layer][R] #bottom = right
			
		for l in range(T,L+1):
			M[l][R] = temp[l-layer] #right = temp
			
		T = T+1
		L = L-1
		B = B+1
		R = R-1
		layer = layer +1
	return M

M = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]

print M

print RotateMatrix(M,5)

