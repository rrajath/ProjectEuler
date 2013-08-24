res = 0
sum = 0
sum_of_sq = lambda n:n**2
sq_of_sum = 0

for i in range(1,101):
    res += sum_of_sq(i)
    sq_of_sum += i

sq_of_sum = sq_of_sum ** 2

print sq_of_sum - res
