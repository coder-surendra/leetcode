from math import ceil
def getSum(n):
    sum  = 0
    for digit in str(n):
        sum += int(digit)

    return(sum)

def getFactor(givenSum,n):
    '''
        function to get possible candidates,where
        whose sum(digits) =  givensum && digit>n 
    '''

    # this function would only work, where sum <18, 
    
    # lenNewDigit = givenSum // 9
    print('given sum ='+str(givenSum))
    flag = True
    N = ceil(givenSum / 9)
    while(flag):
        myList = [9]*N

        remainder = givenSum%9
        if(remainder != 0):
            myList[0] = remainder
        # nBy2 = givenSum//2
        print(myList)
        num = (int(''.join(str(e) for e in myList)))
        if(num >n):
            flag = False
            break
        N += 1
    # if(int(''.join(myList)))
    # intNum

n = 10
initialSum = getSum(n)
sumX2 = initialSum * 2
print('sumX2 = '+str(sumX2))
getFactor(sumX2,n)
# getFactor(29,n)