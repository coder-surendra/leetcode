def removeElement(num,value):
	val = num[value]
	# print(val)
	count = 0
	for i in range(len(num)):

		# print(i)
		if(i != val):
			count += 1
			# num.remove(val)
			num[count] = num[i]
	print('num len = '+str(len(num)))
	print(num)
	return  count




print(removeElement([3,2,2,3],3))
print(removeElement([0,1,2,2,3,0,4,2],2))