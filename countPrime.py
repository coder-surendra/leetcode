# https://leetcode.com/problems/count-primes

def countPrime(n):

	if n<=2 :
		return 0

	primeCount = 0
	primeList = [2]
	for i in range(3,n,2):

		for prime in primeList:
			# this is other way of writing prime> sqrt(i))
			if(prime*prime > i):
				primeList.append(i)
				break
			if (i % prime == 0):
				break




	print(primeList)
	print(len(primeList))


countPrime(30)
# todo : learn about sieve method, which deals with finding prime between 1 and n 
