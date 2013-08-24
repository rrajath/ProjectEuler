def evenly_divisible(n):
    flag = True
    for i in range(1,20):
        if n%i != 0:
            flag = False
            break
    return flag

i = 1
while True:
    i = i+1
    if evenly_divisible(i):
        print i
        break
