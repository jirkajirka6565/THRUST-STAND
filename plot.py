import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
from drawnow import *

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
    try:
        global arduino
        arduino = serial.Serial(port=arduino_port, baudrate=9600, timeout=1) #select arduino port
    except:
        print("Port not found")

Connect()

# Initialize plot
plt.ion()  # Turn on interactive mode
data = []

def make_plot():
    plt.plot(data, 'ro-')  # Real-time plot

# Read and plot data continuously
while True:
    while arduino.inWaiting() == 0:  # Wait for data
        pass
    val = arduino.readline().decode('utf-8').strip()
    print(val)
    data.append(float(val))  # Convert to float and append to list
    drawnow(make_plot)  # Update the plot
    plt.pause(0.000001)  # Pause to allow the plot to update
