import serial
import serial.tools.list_ports
import time

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
    global arduino_connected
    global arduino_port
    arduino_port = FindArduino(get_ports())
    print(arduino_port)
    try:
        global arduino
        arduino = serial.Serial(port=arduino_port, baudrate=9600, timeout=1) #select arduino port
        arduino_connected = True
        print("Arduino connected succesfully!")
    except:
        print("Port Arduino/ACM not found")
        arduino_connected = False
        port_not_found = True

def getSerialData():
    
    try:
        data = arduino.readline().decode("utf-8")
        return data
    except:
        return 0
    
def decodeSerialData(data):
    
    global LC_1, LC_2, LC_3 ##Load Cells
    try:
        splitData = data.split(" ")
        LC_1 = splitData[0]
        LC_2 = splitData[1]
        LC_3 = splitData[2]
        #print(LC_1," ", LC_2," ", LC_3)
        return LC_1, LC_2, LC_3
    except:
        print("Error decoding serial data")
        return 0
    
def calibrateLoadCellZero(LoadCell):
    try:
        if(LoadCell == "LC_1"):
            arduino.write(b"LC_1")
        elif(LoadCell == "LC_2"):
            arduino.write(b"LC_2")
        elif(LoadCell == "LC_3"):
            arduino.write(b"LC_3")
    except:
        print("Arduino not connected")

def calibrateLoadCellInput(LoadCell, value):
    value = str(value)
    value.strip()
    arduino.reset_input_buffer()
    #try:
    if(LoadCell == "LC_1"):
        Data = "LC1_" + str(value)
        arduino.write(Data.encode('utf-8'))
        time.sleep(1)
    elif(LoadCell == "LC_2"):          
        Data = "LC2_" + str(value)
        arduino.write(Data.encode('utf-8'))
        time.sleep(1)
    elif(LoadCell == "LC_3"):            
        Data = "LC3_" + str(value)
        arduino.write(Data.encode('utf-8'))
        time.sleep(1)

    arduino.reset_output_buffer()
    #except:
        #print("Arduino not connected")
    
