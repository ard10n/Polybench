import serial
import struct
from serial.tools.list_ports import comports
import math
import csv

def zoekPoort():
    ser = None
    for port in comports():
        #print(port.serial_number)
        if port.serial_number == 'E3DB147B50575230372E3120FF191E23':
            print("barometer gevonden")
            ser = serial.Serial(port=port.device, baudrate=9600,  parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)  # ,timeout=2)
            return ser


ser = zoekPoort()
if ser != None:

    with open(r'C:\Users\vp-pi\documents\actueleluchtdruk\barodruk.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')

        for i in range(5):
            s = ser.read(4)
            f = math.trunc(struct.unpack('<f', s)[0])
            print(f)
            spamwriter.writerow([i+1,f])


    ser.close()


