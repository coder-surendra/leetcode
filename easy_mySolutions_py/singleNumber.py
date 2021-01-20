# https://leetcode.com/problems/single-number/
# my solution
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

# my second attempt at the code
def singleNumber2(nums):
    mycounter = counter(nums)
    print(mycounter)
    for key,value in mycounter.items():
        if(value == 1):
            return key

print(singleNumber2( [4,1,2,1,2]))