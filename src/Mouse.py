from Animal import Animal


class Mouse(Animal):
    def __init__(self, spawn):
        super().__init__(spawn, 1)
