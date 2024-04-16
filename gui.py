import serial #import pyserial
import serial.tools.list_ports
import time #import time library
import tkinter
from tkinter import *



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
        elif "ACM0" in strPort:
            splitPort = strPort.split(" ")
            print(splitPort)
            comport = splitPort[0]

    return comport

arduino_port = FindArduino(get_ports())
print(arduino_port)


try:
    arduino = serial.Serial(port=arduino_port, baudrate=9600, timeout=1) #select arduino port
except:
    print("Port not found")

#define function for led on
def TurnLedOn():
    arduino.write(b"1")
    print(arduino.readline().decode("utf-8"))

#define function for led off
def TurnLedOff():
    arduino.write(b"0")
    print(arduino.readline().decode("utf-8"))

window = Tk()

window.geometry("1280x720")
window.configure(bg = "#463030")


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

window.mainloop()
