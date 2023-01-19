import random
import time
from game_map import map_board


def random_brain(obj):
    if time.time() - obj.start_time < 0.5:
        return
    obj.start_time = time.time()
    x = random.randint(0, 3)
    if x == 0:
        obj.past_move = x
        obj.move(0, -1, obj.number_cell())

    if x == 1:
        obj.past_move = x
        obj.move(0, 1, obj.number_cell())

    if x == 2:
        obj.past_move = x
        obj.move(1, 0, obj.number_cell())

    if x == 3:
        obj.past_move = x
        obj.move(-1, 0, obj.number_cell())

    y = random.randint(0, 1)
    if y == 0:
        obj.shot()


def lumbago_x(pos, player):
    x, y = pos
    x1, y1 = player.number_cell()
    if y == y1:
        if x < x1:
            for i in range(x + 1, x1):
                if map_board[y][i] != 0:
                    return False
            return player.number_cell()
        if x > x1:
            for i in range(x - 1, x1, -1):
                if map_board[y][i] != 0:
                    return False
            return player.number_cell()
    return False


def lumbago_y(pos, player):
    x, y = pos
    x1, y1 = player.number_cell()
    if x == x1:
        if y < y1:
            for i in range(y + 1, y1):
                if map_board[i][x] != 0:
                    return False
            return player.number_cell()
        if y > y1:
            for i in range(y - 1, y1, -1):

                if map_board[x][i] != 0:
                    return False
            return player.number_cell()
    return False


def logic(obj, player):
    if time.time() - obj.start_time < 0.5:
        return
    obj.start_time = time.time()
    if not(lumbago_x(obj.number_cell(), player) is False):
        pos = lumbago_x(obj.number_cell(), player)
        x, y = obj.number_cell()
        if x < pos[0]:
            if obj.past_click[0] == 1:
                obj.shot()
            else:
                obj.move(1, 0, obj.number_cell())
        if x > pos[0]:
            if obj.past_click[0] == -1:
                obj.shot()
            else:
                obj.move(-1, 0, obj.number_cell())
    if not(lumbago_y(obj.number_cell(), player) is False):
        pos = lumbago_y(obj.number_cell(), player)
        x, y = obj.number_cell()
        if y < pos[1]:
            if obj.past_click[1] == 1:
                obj.shot()
            else:
                obj.move(0, 1, obj.number_cell())
        if y > pos[1]:
            if obj.past_click[1] == -1:
                obj.shot()
            else:
                obj.move(0, -1, obj.number_cell())
    if lumbago_y(obj.number_cell(), player) is False and lumbago_x(obj.number_cell(), player) is False:
        #двигаемся по x и ищем прострел для y
        x, y = obj.number_cell()
        for i in range(x - 1, -1, -1):
            if map_board[y][i] != 0:
                break
            if not(lumbago_y((i, y), player) is False):
                obj.move(-1, 0, obj.number_cell())
        for i in range(x + 1, 10):

            if map_board[y][i] != 0:
                break
            if not(lumbago_y((i, y), player) is False):
                obj.move(1, 0, obj.number_cell())
        #двигаемся по y и ещем прострел для x
        for i in range(y - 1, -1, -1):
            if map_board[i][x] != 0:
                break
            if not(lumbago_x((x, i), player) is False):
                obj.move(0, -1, obj.number_cell())
        for i in range(y + 1, 10):
            if map_board[i][x] != 0:
                break
            if not(lumbago_x((x, i), player) is False):
                obj.move(0, 1, obj.number_cell())




