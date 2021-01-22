# https://leetcode.com/problems/single-number/
# my solution 
# (Runtime: 1172 ms
# Memory Usage: 17 MB)
from collections import Counter as counter
def singleNumber(nums):
    myList = []
    for i in nums:
        # print(i)
        if(i not in myList):
            # add the number in the list
            myList.append(i)
        else:
            # remove the number from the list
            myList.remove(i)
    return myList[0]

# my second attempt at the code (Runtime : 116ms, memory : 16.5MB)
def singleNumber2(nums):
    mycounter = counter(nums)
    print(mycounter)
    for key,value in mycounter.items():
        if(value == 1):
            return key

#solution with 104ms
def singleNumber3(nums):
    current = 0
    for n in nums:
        oldCurrent = current
        current = current ^ n
        print(str(oldCurrent) + ' ^ ' +str(n) + ' = ' + str(current))

    print('returning current')
    return current
'''

    here's a thing,
    ^ is XOR operator
    a ^ b = 1, only if either a or b is non-zero
     & 
    a ^ a = 0
    
    so , in the loop, we xor with all numbers in the num with variable "current", which has zero as default value
    ,here's a demo with input nums = [4,1,2,1,2]
    0 ^ 4 = 4
    4 ^ 1 = 5
    5 ^ 2 = 7
    7 ^ 1 = 6
    6 ^ 2 = 4


'''

print(singleNumber3( [4,1,2,1,2]))