def StringCompression(str):
	counts = dict()
	for l in str:
		counts[l] = counts.get(l,0)+1
	print counts.items()
	
str = "aabccccccaaa"
StringCompression(str)