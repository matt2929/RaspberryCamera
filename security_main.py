import camera_runner
import temp_track
import upload_bucket
import threading
import time
import sys

if __name__ == '__main__':
	print("starting security!...")
	camera_runner.start_camera()
	task = camera_runner.start_camera
	t = threading.Thread(target=task, args=(data, ))
	t.start()
	sys.stdout.flush()
	print("temp start")
	task = temp_track.start_measure
	t = threading.Thread(target=task, args=(data, ))
	t.start()
	sys.stdout.flush()
	print("begin temp sensing")
	while True:
		print("temp: " + temp_track.measure_temp())
		sleep(5)
