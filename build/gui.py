import serial #import pyserial
import time #import time library
import matplotlib.pyplot as plt #import matplotlib

#tkinter designer imports
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\polis\Documents\Coding\Tkinter-Designer-1.0.7\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1) #select arduino port

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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    379.0,
    360.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
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
    file=relative_to_assets("button_2.png"))
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
window.resizable(False, False)
window.mainloop()
