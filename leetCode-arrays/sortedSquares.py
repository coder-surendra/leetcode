def sortedSquares(nums):
    sqNums = []
    for i in nums:
        print(i)
        sqNums.append(i*i)

    print(sqNums)
    sqNums.sort()
    return sqNums


nums = [-4,-1,0,3,10]
print(sortedSquares(nums))


'''

        return sorted(x*x for x in nums)

'''

'''
        length = len(nums)
        for i in range(0, length):
            nums[i] = nums[i]* nums[i]
        nums.sort()

'''