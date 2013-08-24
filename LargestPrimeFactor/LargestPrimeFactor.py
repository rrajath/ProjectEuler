lst = []
num = 600851475143
div = 2
while num > 1:
    if num % div == 0:
        num = num/div
        div = div -1
    div = div + 1

print div
