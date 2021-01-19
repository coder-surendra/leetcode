def reverse( x: int) -> int:
    greaterThanZero = 0

    abs_num = abs(x)
    num_string = str(abs_num)
    reverse_string = num_string[::-1]
    reverse_num = int(reverse_string)
    
    if(not((-2**31)<=reverse_num and (reverse_num<=(2**31 - 1)))):
        reverse_num=0;

    if(x>=0):
        return reverse_num
    else:
        return -1 * reverse_num

print(reverse(1534236469))
# 2147483648
# 1534236469