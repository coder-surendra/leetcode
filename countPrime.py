
def countPrime(n):
	i = 2
	if n<=1 :
		return 0

	primeCount = 0
	primeList = []
	while( i < n):

		isPrime = True

		# checking current number is divisible by previous numbers
		for prime in primeList:
			if( i % prime == 0):
				# i is not a prime number
				isPrime = False
				break




		if(isPrime):
			primeCount += 1
			primeList.append(i)
			print('this number is prime '+str(i))

		i += 1
	print(primeList)
	print(primeCount)


countPrime(30)

