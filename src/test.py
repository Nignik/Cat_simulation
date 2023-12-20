from matplotlib import pyplot as plt
import matplotlib.animation as animation


class Visualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 10))

        self.spawn_points = []
        self.animal_id = 0

    def append_new_animal(self, positions):
        self.positions = positions

    def append_spawn_points(self, positions):
        self.spawn_points.append(positions)

    def init_animation(self):
        plt.style.use('dark_background')
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        self.ax.grid(True)

    def animate(self, frame):
        if frame < len(self.animations.positions):
            x, y = self.animations.positions[frame]
            self.animations.lines.set_data([x], [y])

        return self.animations.lines

    def run_animation(self):
        self.init_animation()
        self.ani = animation.FuncAnimation(self.fig, self.animate, frames=100, interval=400, blit=True)

        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        self.ax.legend(by_label.values(), by_label.keys())

        plt.show()

    def plot_static(self):
        self.init_animation()
        for my_animation in self.animations:
            plt.plot(*zip(*my_animation.positions), color='blue', label='xd')
        plt.show()
