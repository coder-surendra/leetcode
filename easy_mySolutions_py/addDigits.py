# https://leetcode.com/problems/add-digits/
def addDigits(n):
    # flag = True
    digitSum = 0
    num = n
    while(True):

        # loop thought the digits
        digitSum = 0
        while(num != 0):
            digitSum += num%10
            num  = num//10

        if(0<=digitSum and digitSum<=9):
            # flag = False
            # print('sum = '+str(digitSum))
            return(digitSum)    
            # break
        else:
            num = digitSum
        
        # print('sum = '+str(digitSum))


print(addDigits(0))


'''
best solution

def addDigits(self, num: int) -> int:
        
        while num >= 10:
            dig = num % 10
            dig1 = num // 10
            num = dig + dig1
        return num

this was pretty easy to implement, if I would have thought about compressing the code
nonetheless, it is beautiful code
'''