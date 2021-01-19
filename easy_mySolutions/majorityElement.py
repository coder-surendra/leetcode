# https://leetcode.com/problems/majority-element/
from collections import Counter as counter
def majorityElement(nums):
    n = len(nums)
    # print(n)
    # x = nums.count(nums)
    myCounter = counter(nums)
    # print(myCounter.items())
    halfN = n // 2
    # print(halfN)
    majorElement = 0
    for key,value in myCounter.items():
        # print(key ,'->', value)
        if(value>halfN):
            majorElement = key

    # print('majorElement = ',majorElement)
    return majorElement
majorityElement([2,2,1,1,1,2,2])
