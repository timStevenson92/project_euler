#Find the greatest product of five consecutive digits in the 1000-digit number.

maxProd = 0
i = 0
numList = []
numFile = open('number.txt', 'r')
for char in numFile:
	numList = char
numFile.close()

for i in range(1000-5):
	prod = int(numList[i]) * int(numList[i+1]) * int(numList[i+2]) * int(numList[i+3]) * int(numList[i+4])
	if prod >= maxProd:
		maxProd = prod
print(maxProd)