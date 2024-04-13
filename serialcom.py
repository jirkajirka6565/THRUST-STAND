import serial #import pyserial
import time #import time library
import tkinter as tk #import tkinter library

root = tk.Tk() #initialize tkinter
arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1) #select arduino port

#define function for led on
def TurnLedOn():
    arduino.write(b"1")
    print(arduino.readline().decode("utf-8"))

#define function for led off
def TurnLedOff():
    arduino.write(b"0")
    print(arduino.readline().decode("utf-8"))

#buttons for Led on/off
LedOnButton = tk.Button(root, text="Led On", command=TurnLedOn)
LedOnButton.pack()
LedOffButton = tk.Button(root, text="Led Off", command=TurnLedOff)
LedOffButton.pack()


root.mainloop()