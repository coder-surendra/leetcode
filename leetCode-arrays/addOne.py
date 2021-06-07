def addOne(nums):
    
    stringNumber = ''.join([str(a) for a in nums])
    print(stringNumber)
    intNumber = int(stringNumber)

    intNumber += 1
    stringNumber = str(intNumber)
    print(type(stringNumber))

    nums1 = list(stringNumber)

    print(nums1)

nums = [1,2,3]

addOne(nums)
