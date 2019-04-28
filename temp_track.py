import os
import time
import threading

temp = 0
measure=True

def poll_temp():
        global temp
	temp = os.popen("vcgencmd measure_temp").readline()
	ts = time.time()
        return temp.replace("temp=","") + " id: " + str(threading.current_thread())
