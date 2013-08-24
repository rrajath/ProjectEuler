sum = 0
lst = [a for a in range(1000) if a%3 == 0 or a%5 == 0]
for i in lst:
	sum = sum + i
print sum
