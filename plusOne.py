# problem link : https://leetcode.com/problems/plus-one/
# this was exteremly tricky, because they didn't problem proper test case
def plusOne(digits):
	print(digits)
	string =  (''.join(str(d) for d in digits))
	# print(number)
	number = int(string)
	number += 1

	n = len(digits)

	# convert to string
	plusOneString = str(number)
	print('plusOneString = '+ plusOneString)
	if(n != len(plusOneString)):
		# padd the zeros
		plusOneString = plusOneString.zfill(n)
		print('length not equal to '+str(n))
	else:
		print('same length')
	print(plusOneString)

	print([int(i) for i in str(plusOneString)])

# plusOne([1,2,3])
plusOne([0,0])