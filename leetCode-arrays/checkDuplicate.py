# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
from collections import Counter
def checkDuplicate(nums):
    i = 0
    n = len(nums)
    num1 = sorted(nums)
    while(i < n):
        print(num1[i+1:n])
        if(num1[i] in num1[i+1:n]):
            print(str(num1[i])+' found')
            return True
        
        i += 1

    print('no match found')
    return False

def fun2(nums):
    c = Counter(nums)
    print(c)
    for key,value in c.items():
        print(key, '->', value)
        if(value>0):
            print()
nums = [1,1,1,3,3,4,3,2,4,2]   
nums = [1,2,3,4]     
fun2(nums)


# runtime sample 120ms :
def containsDuplicate120( nums):
    if len(nums)>len(set(nums)):
        return True
    else:
        return False

# runtime sample 96ms :
def containsDuplicate96ms( nums):
    return (len(set(nums)) != len(nums))



# memoryDistrubution
def containsDuplicate_19100KB(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False

