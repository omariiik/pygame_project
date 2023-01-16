import random
import time


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

