def romanLetters( x: str) -> int:
	romanDict = {
	'I' : 1,
	'V' : 5,
	'X' : 10,
	'L' : 50,
	'C' : 100,
	'D' : 500,
	'M' : 1000

	}
	num = 0
	i = 0
	n = len(x)
	while(i<n):
		# print(x[i])
		if( i+1 <n):
			# print('i + 1 < n');
			if(romanDict[x[i+1]] > romanDict[x[i]]): 
				# we have something like #IV
				# print('x[i+1] > x[i]');

				num += romanDict[x[i+1]] - romanDict[x[i]]
				i += 2
			else:
				# print('x[i+1] < x[i]');

				num += romanDict[x[i]]
				i += 1

		else:
			num += romanDict[x[i]]
			i += 1
		# print(num)

	# print(num)
	return num

romanLetters('LVIII')
romanLetters('MCMXCIV')
