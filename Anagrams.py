#anagrams are words in which the letters are the same but just the order is different
# this program puts all anagrams next to each other
def groupByAnagrams(strArray):
	d = {}
	#sort each string in the array and use that as the key to store all anagrams of this string 
	for s in strArray:
		if sortString(s) in d:
			lst = d[sortString(s)]
			lst.append(s)
			d[sortString(s)] = lst
		else:
			
			d[sortString(s)] = [s]
	#now construct the list of strings back by grouping the anagrams together
	offset =0
	for keys in d:
		lst = d[keys]
		for l in lst:
			strArray[offset]=l
			offset+=1
	return strArray


strArray = ["acre","pan","mate","nap","race","team","care"]

def sortString(s):
	s = sorted(s)
	str = ""
	for c in s:
		str = str+c
	return str
	
print groupByAnagrams(strArray)