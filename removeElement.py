def removeElement(num,value):
	val = num[value]
	# print(val)
	count = 0
	for i in range(len(num)):

		if num[i] != val :
			print(i)
			# num.remove(val)
			num[count] = num[i]
			count += 1
			print(num)
	print('num len = '+str(len(num)))
	print(num)
	return  count




print(removeElement([3,2,2,3],3))
print(removeElement([0,1,2,2,3,0,4,2],2))