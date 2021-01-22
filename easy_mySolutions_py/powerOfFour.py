from math import log
'''
Runtime: 32 ms
Memory Usage: 14.3 MB
'''
def isPowOfFour(n):
    # negative = 1;
    if(n <=0):
        return False;
        # n  = abs(n)

    return(log(n,4).is_integer())



# print(isPowOfFour(-2147483648))
print(isPowOfFour(-64))
# print(log(-2147483648,4).is_integer())
# print((log(64,4)))

# code with 14000KB space
def isPowerOfFour1( n):
    while n>1:
        if n%4:
            return False
        n>>=2
    return n==1


'''
code with 16ms runtime

'''
def isPowerOfFour2(self, n: int) -> bool:
    if n <= 0:
        return False
    ans = 0
    while n > 1 and ans == 0:
        ans = n % 4
        n = n / 4
        if (n < 1 or ans != 0):
            return False
        
    return True