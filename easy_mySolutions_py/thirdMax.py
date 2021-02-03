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