import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class RealTimeGraph:
    def __init__(self):
        # Create a figure and axis
        self.fig, self.ax = plt.subplots()

        # Initial limits
        self.ax.set_xlim(0, 2*np.pi)
        self.ax.set_ylim(-1, 1)

        # Line object to update
        self.line, = self.ax.plot([], [], lw=2)

    def init_graph(self):
        self.line.set_data([], [])
        return self.line,

    def update_graph(self, frame):
        x = np.linspace(0, 2*np.pi, 1000)
        y = np.sin(x + 0.1 * frame)

        # Update line data
        self.line.set_data(x, y)

        # Dynamic Y limits
        ymin = np.min(y) - 0.1  # Adding a small buffer
        ymax = np.max(y) + 0.1
        self.ax.set_ylim(ymin, ymax)

        return self.line,

    def start_animation(self):
        self.ani = animation.FuncAnimation(
            self.fig, 
            self.update_graph, 
            init_func=self.init_graph, 
            blit=True, 
            interval=50
        )
        return self.fig
    




