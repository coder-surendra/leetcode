def findMaxConsecutiveOnes(nums):
    i = 1
    count = 0

    if(len(nums)<=1): 
        print('arr too short')
        return nums[0]

    maxCount = 0
    count = nums[0]
    while(i<len(nums)):

        # tracking the max count

        if(maxCount <= count) :
            maxCount = count


        if(nums[i] == 1):
            #  current element = 1, 
            if(nums[i-1] == 1) :
                # last element = 0
                # we increment the counter
                count += 1
            else:
                # last element = 0
                # we need to restart the counter
                count = 1

            if(maxCount <= count) :
                maxCount = count

        else:
            #  current element = 0, 
            if(nums[i-1] == 0) :
                # last element = 0
                # we start the counting again
                count = 0 
            else:
                # last element = 1, 
                # we start the counter again
                count = 0


        i += 1

    # print('yolo = ',count)
    return maxCount


print(findMaxConsecutiveOnes([1,1,1,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1,1,0,1]))
print(findMaxConsecutiveOnes([0,1]))
# print(findMaxConsecutiveOnes([0]))
# print(findMaxConsecutiveOnes([1]))

'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        
        nums.append(0)
        for n in nums:
            if n == 1:
                count+=1
            else:
                max_count = max(max_count, count)
                count = 0
        return max_count

'''