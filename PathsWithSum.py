from Tree import Tree

def computePaths(root,targetSum):
	map = {}
	return computePathsWithSum(root,0,targetSum,map)
	
def computePathsWithSum(node,runningSum,targetSum,map):
	if node == None:
		return 0
	runningSum+=node.data
	sum = runningSum-targetSum
	totalPaths = map.get(sum,0)
	
	if runningSum==targetSum:
		totalPaths+=1
	
	map[runningSum]+=1
	totalPaths+=computePathsWithSum(node.left,runningSum,targetSum,map)
	totalPaths+=computePathsWithSum(node.right,runningSum,targetSum,map)
	map[runningSum]-=1
	return totalPaths