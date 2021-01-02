def isPalindrome( x: int) -> bool:
	rev_num = 0
	if(x<0 or (x % 10 == 0 and x != 0)):
		print('returning false')
		return False
	while(x > rev_num):
		rev_num = rev_num * 10 + x % 10
		x = int(x/10)

	print('after long calculations')
	print(rev_num)
	return x ==  rev_num or x == rev_num/10   

print(isPalindrome(121))