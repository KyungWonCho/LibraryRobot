import serial

ser=serial.Serial('/dev/ttyACM0', 9600)

while True:
    a=input("")
    ser.write(b'1')
