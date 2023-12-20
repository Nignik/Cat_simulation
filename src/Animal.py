import random
import numpy as np


def clamp(pos, min, max):
    if pos[0] < min:
        pos = (0, pos[1])
    if pos[0] > max:
        pos = (max, pos[1])
    if pos[1] < min:
        pos = (pos[0], min)
    if pos[1] > max:
        pos = (pos[0], max)

    return pos


class Animal:
    def __init__(self, spawn: tuple, speed):
        self.spawn = spawn
        self.speed = speed

        self.position = spawn
        self.path = [spawn]

    def move(self):
        move_x = random.randint(-self.speed, self.speed)
        move_y = random.randint(-self.speed, self.speed)
        self.position = (self.position[0] + move_x, self.position[1] + move_y)
        self.position = clamp(self.position, 0, 100)

        self.path.append(self.position)

    def recall(self):
        self.position = self.spawn
