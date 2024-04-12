import serial #import pyserial
import time #import time library

arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1)

def TurnLedOn():
    arduino.write(b"1")

def TurnLedOff():
    arduino.write(b"0")

while(True):
    TurnLedOn()
    time.sleep(1)
    TurnLedOff()
    time.sleep(1)