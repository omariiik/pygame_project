import random

x = random.randint(1, 3)
f = open(f'data\level{x}.txt', encoding='utf-8')
maap = []
for i in range(10):
    a = []
    s = f.readline()
    s = s.rstrip()
    for j in s:
        j = int(j)
        a.append(j)
    maap.append(a)
f.close()
map_board = maap[:]
