sum = 0
res = 0
lst = []
for n in range(1000):
	sum = (0.4472135954999579392818347337462552470881236719223051448541*(pow(1.6180339887498948482045868343656381177203091798057628621354,n) - pow(-0.618033988749894848204586834365638117720309179805762862135,n)))
	if int(sum) % 2 == 0:
		if int(sum) < 4000000:
			lst.append(int(sum))

for i in lst:
	res = res + i

print res
