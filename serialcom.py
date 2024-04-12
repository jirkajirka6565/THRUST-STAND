import pyserial

arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1)