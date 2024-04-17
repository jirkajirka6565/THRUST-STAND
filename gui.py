import serial #import pyserial
import serial.tools.list_ports
import time #import time library
import tkinter
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import numpy as np

window = Tk()

fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [], lw=2)

ax.set_xlim(0, 100)
ax.set_ylim(-0.5, 2) 

window.geometry("1280x720")
window.configure(bg = "#463030")

def get_ports():
    ports = serial.tools.list_ports.comports()
    return ports

def FindArduino(portsFound):
    comport = "no port"
    print("\n")
    numOfPorts = len(portsFound)

    for i in range(0, numOfPorts):
        port = portsFound[i]
        strPort = str(port)
        print(strPort)
        print("\n")

        if "Arduino" in strPort:
            splitPort = strPort.split(" ")
            comport = splitPort[0]
            print(comport)
        elif "ACM" in strPort:
            splitPort = strPort.split(" ")
            print(splitPort)
            comport = splitPort[0]

    return comport

def Connect():

    arduino_port = FindArduino(get_ports())
    print(arduino_port)
    try:
        global arduino
        arduino = serial.Serial(port=arduino_port, baudrate=9600, timeout=1) #select arduino port
        messagebox.showinfo("Info", "Arduino connected successfully!")
    except:
        print("Port not found")
        messagebox.showerror("Error", "Arduino not found")



#define function for led on
def TurnLedOn():
    arduino.write(b"1")
    print(arduino.readline().decode("utf-8"))

#define function for led off
def TurnLedOff():
    arduino.write(b"0")
    print(arduino.readline().decode("utf-8"))

def ExitProgram():
    exit()

canvas = Canvas(
    window,
    bg = "#463030",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(file="image_1.png")

canvas.create_image(379.0, 360.0, image=image_image_1)

graph = FigureCanvasTkAgg(fig, master=window)
graph.get_tk_widget().place(x=650,y=100)

button_image_1 = PhotoImage(
    file="button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=TurnLedOn,
    relief="flat"
)
button_1.place(
    x=261.0,
    y=205.0,
    width=236.0,
    height=96.0
)

button_image_2 = PhotoImage(
    file="button_2.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=TurnLedOff,
    relief="flat"
)
button_2.place(
    x=261.0,
    y=384.0,
    width=236.0,
    height=96.0
)

connectButton = Button(
    text="Connect",
    borderwidth=0,
    highlightthickness=0,
    command=Connect,
    relief="flat"
)
connectButton.place(
    x=261,
    y=30,
    width=236.0,
    height=96.0
)

def get_sensor_data():
    
    receivedData = arduino.readline()

    print(receivedData)

    if receivedData == "Led on":
        data = 1
    elif receivedData == "Led off":
        data = 0

    return data

def init():
    line.set_data([], [])
    return line,

def animate(frame):
    x_data.append(frame)
    y_data.append(get_sensor_data())  # Get sensor data
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, animate, frames=np.linspace(0, 100, 100), init_func=init, blit=True)
plt.xlabel('Time')
plt.ylabel('Sensor Data')
plt.title('Real-time Sensor Data')
plt.grid(True)

window.protocol("WM_DELETE_WINDOW", ExitProgram)
window.mainloop()
