#The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers 
#and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first 
#one hundred natural numbers and the square of the sum.

def sum_square (num):
	for i in range(1, 101):
		num = num + i**2
	return num

def square_sum (num):
	for i in range(1, 101):
		num = num + i
	return num**2

num1 = 0
num2 = 0
final = square_sum(num1) - sum_square(num2)
print(final)