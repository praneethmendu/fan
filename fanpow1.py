from time import sleep
import serial
from subprocess import check_output
import subprocess

ser = serial.Serial('/dev/ttyACM2', 9600)
tick = 0

while(True):
    k=check_output(['bash', '-c', "nvidia-smi dmon -c 1 | sed -n '3,5p' - | cut -b 16-18"])
    print(str(k)[2:4],str(k)[7:9])
    if(int(str(k)[2:4])>58 or int(str(k)[7:9])>58):
        ser.write('h'.encode())

    sleep(15)



