def addOne(nums):
    
    stringNumber = ''.join(str(nums))
    intNumber = int(stringNumber)

    intNumber += 1

    stringNumber = str(stringNumber)

    nums = list(stringNumber)

    print(nums)

nums = [1,2,3]
addOne(nums)
