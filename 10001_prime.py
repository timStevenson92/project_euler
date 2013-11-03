#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we 
#can see that the 6th prime is 13.
#What is the 10,001st prime number?

def isPrime(n):
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for i in range(3, int(n**.5)+1, 2):
		if n % i == 0:
			return False
	return True

count = 0
primeCount = 1
while (True):
	count += 1
	x = isPrime(count)
	if x == True:
		primeCount += 1
	if primeCount == 10002:
		break
print(count)