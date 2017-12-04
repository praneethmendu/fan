from time import sleep
import serial
from subprocess import check_output
import subprocess
while(True):
    k=check_output(['bash', '-c', "nvidia-smi dmon -c 1 | sed -n '3,5p' - | cut -b 16-18"])
    print(str(k)[2:4])
    sleep(15)

