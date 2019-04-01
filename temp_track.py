import os
import time

temp=""
measure=True

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

def start_measure():
	while measure:
        	print(measure_temp())
        	time.sleep(5)

def end_measure():
	global measure
	measure=false
