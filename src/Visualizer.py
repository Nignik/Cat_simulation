from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


class Visualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 10))

        self.positions = []
        self.lines = []

    def append_new_animal(self, spawn, positions, color, label):
        self.positions.append(positions)
        line, = self.ax.plot([], [], color=color, label=label)
        self.lines.append(line)

        plt.scatter(spawn[0], spawn[1], color=color, s=50)

    def init_animation(self):
        plt.style.use('dark_background')
        self.ax.set_xlim(0, 100)
        self.ax.set_ylim(0, 100)
        self.ax.grid(True)

        return self.lines

    def update(self, frame):
        for line, pos in zip(self.lines, self.positions):
            if frame < len(pos):
                line.set_data(*zip(*pos[:frame + 1]))
        return self.lines

    def animate(self):
        self.init_animation()
        num_frames = max(len(pos) for pos in self.positions)

        handles, labels = self.ax.get_legend_handles_labels()
        self.ax.legend(handles, labels)

        anim = FuncAnimation(self.fig, self.update, frames=num_frames, init_func=self.init_animation, blit=True)
        plt.show()
