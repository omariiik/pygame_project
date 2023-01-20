from game_map import map_board


def create_map(level):
    create(level)


def create(level):
    f = open(f'data\{level}.txt', encoding='utf-8')
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
