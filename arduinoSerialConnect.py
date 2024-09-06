import serial
import serial.tools.list_ports

arduino_connected = False
port_not_found = False

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
    global arduino_port
    arduino_port = FindArduino(get_ports())
    print(arduino_port)
    try:
        global arduino
        arduino = serial.Serial(port=arduino_port, baudrate=9600, timeout=1) #select arduino port
        arduino_connected = True
        print("Arduino connected succesfully!")
    except:
        print("Port not found")
        port_not_found = True

def getSerialData():
    
    try:
        return arduino.readline().decode("utf-8")
    except:
        return 0
    
def decodeSerialData(data):
    pass
    