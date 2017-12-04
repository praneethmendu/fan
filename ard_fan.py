from time import sleep
import serial
from subprocess import check_output
import subprocess

ser = serial.Serial('/dev/ttyACM0', 9600)
tick = 0

while(True):
    k=check_output(['bash', '-c', "nvidia-smi dmon -c 1 | sed -n '3,5p' - | cut -b 16-18"])
    if(int(str(k)[2:4])>58):
        ser.write('h'.encode())
        if tick == 0 :
            tick = 1
            subprocess.run(["/home/mendu/fan/high.sh"])

    else:
        if tick == 1 :
            tick = 0
            subprocess.run(["/home/mendu/fan/low.sh"])
    sleep(4.99)



