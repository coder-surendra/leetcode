# problem link : https://leetcode.com/problems/two-sum/
def twoSum(arr,target):
    result = []
    numIndex = {}
    i = 0
    while(i<len(arr)):
        num = arr[i]
        compliment = target - num
        if(compliment in numIndex):
            # we found the result
            result.append(numIndex[compliment])
            result.append(i)

            # print(result)
            break
        numIndex[num] = i
        i += 1
    
    return result

print( twoSum([2,7,11,15], 18) )

