from time import sleep
import serial
from subprocess import check_output
import subprocess

try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
except:
    try:
        sleep(2)
        ser = serial.Serial('/dev/ttyACM1', 9600)
    except:
            try:
                sleep(2)
                ser = serial.Serial('/dev/ttyACM2', 9600)
            except:
                sleep(2)
                ser = serial.Serial('/dev/ttyACM2', 9600)            

while(True):
    k=check_output(['bash', '-c', "nvidia-smi dmon -c 1 | sed -n '3,5p' - | cut -b 16-18"])
    print(str(k)[2:4])
    if(int(str(k)[2:4])>58):
        try:
            ser.write('h'.encode())
        except:
            sleep(7)  
            try:
                ser = serial.Serial('/dev/ttyACM0', 9600)
            except:
                sleep(2)
                try:
                    ser = serial.Serial('/dev/ttyACM1', 9600)
                except:
                    sleep(2)
                    try:
                        ser = serial.Serial('/dev/ttyACM2', 9600)
                    except:
                        sleep(2)
                        ser = serial.Serial('/dev/ttyACM3', 9600)            

 
    sleep(15)

