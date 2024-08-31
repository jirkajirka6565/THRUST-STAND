import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")

# Create a label
label = tk.Label(root, text="Graphs", font=("Helvetica", 24))
label.pack(pady=10)

# Create a container frame for the two subframes
container = tk.Frame(root)
container.pack(fill=tk.BOTH, expand=True)

# Create the left frame for the matplotlib plot
left_frame = tk.Frame(container)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

graph_frame = tk.Frame(left_frame)
graph_frame.pack(fill=tk.BOTH, expand=True)

middle_frame = tk.Frame(container)
middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

# Create the right frame for the option buttons
right_frame = tk.Frame(container)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Matplotlib figure and axis
fig, ax = plt.subplots()
fig.set_size_inches(8, 3)

fig2, ax2 = plt.subplots()
fig2.set_size_inches(8, 3)

# Initialize variables to store data points
x_data = []
y_data = []

# Function to update the plot in real-time
def animate(i):
    current_time = time.time()
    
    # Add new data point
    x_data.append(current_time - start_time)
    y_data.append(np.sin(x_data[-1]))

    # Clear the axis and plot updated data
    ax.clear()
    ax.plot(x_data, y_data)

    # Set axis labels
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")

    # Set dynamic axis limits
    ax.set_xlim(max(0, x_data[-1] - 10), x_data[-1] + 1)  # Show last 10 seconds
    ax.set_ylim(min(y_data) - 0.1, max(y_data) + 0.1)

    x_data2 = np.linspace(0, 2 * np.pi, 100)
    y_data2 = np.cos(x_data2)
    ax2.clear()
    ax2.plot(x_data2, y_data2)
    ax2.set_xlabel("Angle (radians)")
    ax2.set_ylabel("Cosine")


    data_display.config(text=f"Latest Time: {x_data[-1]:.2f}s\nLatest Amplitude: {y_data[-1]:.2f}")
    data_display_2.config(text=f"Graph 2 - Angle: {x_data2[-1]:.2f} rad\nCosine: {y_data2[-1]:.2f}")

# Store the start time to calculate elapsed time
start_time = time.time()

# Create the canvas for the matplotlib plot
canvas = FigureCanvasTkAgg(fig, master=left_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

canvas2 = FigureCanvasTkAgg(fig2, master=left_frame)
canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)

canvas.get_tk_widget().pack(in_=graph_frame, side=tk.TOP, fill=tk.BOTH, expand=True)
canvas2.get_tk_widget().pack(in_=graph_frame, side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Animation for real-time updates
ani = animation.FuncAnimation(fig, animate, interval=100, save_count=100)

data_display = tk.Label(middle_frame, text="Latest Time: 0.00s\nLatest Amplitude: 0.00", font=("Helvetica", 14))
data_display.pack(pady=10)

data_display_2 = tk.Label(middle_frame, text="Graph 2 - Angle: 0.00 rad\nCosine: 0.00", font=("Helvetica", 14))
data_display_2.pack(pady=10, anchor=tk.W)

# Option buttons in the right frame
button1 = ttk.Button(right_frame, text="Option 1")
button1.pack(pady=10, padx=10)

button2 = ttk.Button(right_frame, text="Option 2")
button2.pack(pady=10, padx=10)

button3 = ttk.Button(right_frame, text="Option 3")
button3.pack(pady=10, padx=10)

# Start the Tkinter event loop
root.mainloop()
