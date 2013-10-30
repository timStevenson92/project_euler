#A palindromic number reads the same both ways. The largest palindrome made from the 
#product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

max_pal = 0		
for x in range(999,100,-1):
	for y in range(999,100,-1):
		flag = True
		xystring = str(x*y)
		for index in range(len(xystring)):
			if xystring[index] != xystring[len(xystring) - index - 1]:
				flag = False
		if flag and max_pal < x*y:
			max_pal = x*y
			flag = True
			
print(str(max_pal))