from ReadInput import read_input
from Visualizer import Visualizer


class Simulation:
    def __init__(self):
        animals = read_input()
        self.cats = animals[0:3]
        self.mice = animals[3]

        self.average_cats_positions = None
        self.lazy_cats_positions = None
        self.small_cats_positions = None
        self.mice_positions = None

        self.steps = None

    def init_parameters(self):
        print('how many iterations: ')
        self.steps = int(input())

    def simulate(self):
        self.init_parameters()

        for i in range(self.steps):
            for mouse in self.mice:
                mouse.move()
                for cat_type in self.cats:
                    for cat in cat_type:
                        cat.move()
                        cat.interact(mouse)

    def animate(self):
        visualizer = Visualizer()

        colors = {'AverageCat': 'red', 'LazyCat': 'blue', 'SmallCat': 'green', 'Mouse': 'deeppink'}

        for cat_type in self.cats:
            for cat in cat_type:
                visualizer.append_new_animal(cat.spawn, cat.path, colors[cat.__class__.__name__], cat.__class__.__name__)

        for mouse in self.mice:
            visualizer.append_new_animal(mouse.spawn, mouse.path, colors[mouse.__class__.__name__], mouse.__class__.__name__)

        visualizer.animate()
