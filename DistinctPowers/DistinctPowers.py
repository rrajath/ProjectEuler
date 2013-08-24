a = [x for x in range(2,101)]
lst = []
for i in a:
	for j in a:
		if i**j not in lst:
			lst.append(i**j)

print len(lst)
