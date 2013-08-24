st = ""
rev = ""
lst = []
for i in range(101,1000):
	for j in range(101,1000):
		st = str(i*j)
		rev = st[::-1]
		if st == rev:
			lst.append(int(st))
print max(lst)
