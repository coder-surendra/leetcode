def isPowerOfTwo(n):
    if n <= 0:
        return False
    ans = 0
    while n > 1 and ans == 0:
        ans = n % 2
        n = n / 2
        if (n < 1 or ans != 0):
            return False
        
    return True