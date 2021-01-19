# https://leetcode.com/problems/add-binary/
def addBinary(a,b):
	totalLen = len(a) + len(b)
	a = a.zfill(totalLen)
	b = b.zfill(totalLen)
	listA = list(a)
	listB = list(b)
	#  we need to reverse 
	carry = 0
	i = totalLen - 1
	addList = [0] * (totalLen+1)

	while(i >= 0):
		addition = 0
		addition = int(listA[i]) + int(listB[i]) + carry

		if(addition == 0):
			# we cant do a thing
			carry = 0

		elif(addition == 1):
			carry = 0

		elif(addition == 2):
			carry = 1
			addition = 0

		else:
			# its addition = 3
			carry = 1
			addition = 1

		# insert the value to the array
		addList[i+1] = addition

		i -= 1



	# print(list(a))
	# print(' + ')
	# print(list(b))
	# print(' = ')
	# print(addList)

	s = int(''.join(str(e) for e in addList))
	return (str(s))


print(addBinary("1010","1011"))
