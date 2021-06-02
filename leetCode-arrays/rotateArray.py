def rotateArray(nums,k):
    i = 0
    n = len(nums)
    newList = [None] * n
    while(i < n):
        print('i = ',i)
        if(i + k < n):
            newList[i+k] = nums[i]
        else:
            newList[i-k-1] = nums[i]
        i += 1
        print(newList)


def rotate2(nums,k):
    # arr = []
    n = len(nums)
    arr = [None] * ( n)
    arr[0] = nums[0:k]
    # arr.extend(nums[0:k])
    # print(arr)
    arr[1] = nums[k:n]
    # arr.extend(nums[k:n])
    print(arr[1] + arr[0])


def tempFunction(nums,k):

    n = len(nums)
    k=k%n
    if n>=2 and k>0:
        nums[:] = nums[n-k:] + nums[:n-k]  
    print(nums)
  
# nums = [1,2,3,4,5,6,7]
# rotateArray(nums,k)
k = 2
nums = [-1,-100,3,99]
# rotate2(nums,k)

# tempFunction(nums,k)

nums = [1,2,3,4,5,6,7]
k = 3
print(tempFunction(nums,k))

# rotate2(nums,k)
# print(nums[k:])
