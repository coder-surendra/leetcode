# https://leetcode.com/problems/third-maximum-number/
def thirdMaxfunction(nums):
    nums = list(set(nums))
    n = len(nums)
    if(n == 1):
        return nums[0]
    elif(n == 2):
        return max(nums[1],nums[0])
    else:

        firstMax = secondMax = thirdMax = min(nums)
        for i in nums:
            # print(i)

            # if(i != firstMax or i != secondMax or i != thirdMax):


            if( i > firstMax and i != firstMax):
                print('1st condition')
                thirdMax = secondMax
                secondMax =firstMax
                firstMax = i
            elif(i > secondMax and i != firstMax):
                thirdMax = secondMax
                print('2nd condition')

                secondMax = i
            elif(i > thirdMax and i != secondMax and i != firstMax):
                thirdMax = i
                print('3rd condition')

            else:
                print('4th condition')

                continue

            print('firstMax = ',firstMax,' secondmax = ',secondMax,' thirdMax = ',thirdMax)
            

        # print('after the loop');
        print('firstMax = ',firstMax,' secondmax = ',secondMax,' thirdMax = ',thirdMax)
    return thirdMax
    
print(thirdMaxfunction([1,1,2,3,3]))

'''


    def thirdMax(self, nums: List[int]) -> int:
        max = min(nums) - 1       
        second_max = min(nums) - 1       
        third_max = min(nums) - 1  
        for num in set(nums):
            if num > max:
                third_max, second_max = second_max, third_max
                max, second_max = num, max
            elif num > second_max:
                second_max, third_max = num, second_max
            elif num > third_max:
                third_max = num
        if len(set(nums)) < 3:
            return max
        return third_max

'''


'''
15000 KB submission

import math 

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        f = nums[0]
        s = -math.inf 
        t = -math.inf 
        
        for num in nums[1:]:
            if num > f:
                t = s
                s = f
                f = num
            elif num > s and num < f:
                t = s
                s = num
            elif num > t and num < s:
                t = num
        if t == -math.inf:
            return f
        return t
'''