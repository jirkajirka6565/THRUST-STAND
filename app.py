import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import arduinoSerialConnect
import graphs

def arduinoConnect():
    arduinoSerialConnect.Connect()

class RealTimeGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Graph with Dynamic Limits")

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)

        # Create a button above the graph
        self.button = tk.Button(self.frame, text="Click me!", command=arduinoConnect)
        self.button.pack(side=tk.TOP)

        # Create graph instance
        self.graph1 = graphs.RealTimeGraph()
        self.graph2 = graphs.RealTimeGraph()
        self.graph3 = graphs.RealTimeGraph()

        # Embed the plot into Tkinter
        self.canvas1 = FigureCanvasTkAgg(self.graph1.start_animation(), master=self.root)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=1, ipady=10)

        self.canvas2 = FigureCanvasTkAgg(self.graph2.start_animation(), master=self.root)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=1)

        self.canvas3 = FigureCanvasTkAgg(self.graph3.start_animation(), master=self.root)
        self.canvas3.draw()
        self.canvas3.get_tk_widget().pack(fill=tk.BOTH, expand=1)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = RealTimeGraphApp(root)
    app.run()