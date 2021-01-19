def removeDuplicates(nums):
	'''
		removes duplicate entries from a sorted array &
		returns the length of modified array
		NOTE: Memory constriants : O(1)
	
	'''

	i = 0
	while(i<len(nums)):

		# print('at the start')
		# print(nums)
		# print(str(i) + ' ' + str(len(nums)) )
		if((i+1) < len(nums)):
			if(nums[i] == nums[i + 1]):
			# we found duplicate
			# remove the entry and reduce
				nums.pop(i+1)
				# print('at the end')
				# print(nums)
				continue
			else:
				i += 1
		else:
			i += 1

	# print(nums)
	return nums


# removeDuplicates([0,0,1,1,1,2,2,3,3,4])
removeDuplicates([1,1,2])