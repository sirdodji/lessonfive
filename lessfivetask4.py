import random
nlist = [random.randint(1, 100) for i in range(20)]
print(nlist)
for i in range(len(nlist)):
    if nlist[i] % 2 != 0:
        nlist[i] = 0
print(nlist)
