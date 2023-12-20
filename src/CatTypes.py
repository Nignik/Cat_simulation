import math
import random
from Animal import Animal
from Mouse import Mouse


class AverageCat(Animal):
    def __init__(self, spawn: tuple):
        super().__init__(spawn, 10)

    def interact(self, mouse: Mouse):
        in_range = math.dist(self.position, mouse.position) <= 10

        if in_range:
            mouse.recall()


class LazyCat(Animal):
    def __init__(self, spawn: tuple):
        super().__init__(spawn, 10)
        self.mouse_pats = 0

    def calculate_interest(self):
        return 1 / (1 + math.exp(-0.1 * self.mouse_pats))

    def interact(self, mouse: Mouse):
        in_range = math.dist(self.position, mouse.position) <= 10

        if self.calculate_interest() >= random.randrange(0, 1) and in_range:
            self.mouse_pats += 1
            mouse.recall()


class SmallCat(Animal):
    def __init__(self, spawn: tuple):
        super().__init__(spawn, 5)

    def interact(self, mouse: Mouse):
        in_range = math.dist(self.position, mouse.position) <= 10
        distance_to_bed = math.dist(self.position, mouse.position)

        if distance_to_bed <= 50 and in_range:
            mouse.recall()

        self.recall()
