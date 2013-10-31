#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
#without any remainder.
#What is the smallest positive number that is evenly divisible by all of the 
#numbers from 1 to 20?

num = 2521
flag = False
while(not flag):
	if num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 5 == 0 and num % 6 == 0 and num % 7 == 0 and num % 8 == 0 and num % 9 == 0 and num % 10 == 0 and num % 11 == 0 and num % 12 == 0 and num % 13 == 0 and num % 14 == 0 and num % 15 == 0 and num % 16 == 0 and num % 17 == 0 and num % 18 == 0 and num % 19 == 0 and num % 20 == 0:
		flag = True
		break
	num = num + 1

print ("The smallest multiple using a loop is ", num)

#Alternatively, The smallest multiple can also be found by multiplying 
#the highest primes in this range

print("Multiplying the highest primes, the smallest multiple is ", 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)