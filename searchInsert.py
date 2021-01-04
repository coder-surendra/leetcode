def searchInsert(nums,target):
	length = len(nums)
	average = sum(nums)//length
	print(average)

	mid = length// 2
	print(mid)

	if(target>=average):
		i = mid
		while i<length:

			if(nums[i] == target):
				return i
			elif(target < nums[i]):
				return i
			# else:
				
			i += 1
		# we found no match 
		return i 
		# return 0
			# pass
	else:
		i = mid
		while(i>=0):
			print(nums[i])
			if(nums[i] == target):
				print('target found at' +str(i))
				return i
			elif(target > nums[i]):
				print('target > '+str(nums[i]) + '  ' +str(i))
				return i+1
			# else:
				
			i -= 1
		# we found no match 
		return 0 
		# return 0




print('position = '+str( searchInsert([1,4,6,7,8,9],6) ))
