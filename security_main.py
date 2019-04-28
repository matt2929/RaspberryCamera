import camera_runner
import temp_track
import upload_bucket
import threading
import time
import sys
import batch_write

def time_track():
	task = time_track
	temp_track.poll_data()
	sleep(5)
	t = threading.Thread(target=task, args=(data, ), daemon=True)
	t.start()

def main():
	print("starting security!...")
	camera_runner.start_camera()
	task = camera_runner.start_camera
	t = threading.Thread(target=task, args=(data, ), daemon=True)
	t.start()
	sys.stdout.flush()
	print("temp start")
	task = temp_track.start_measure
	t = threading.Thread(target=task, args=(data, ), daemon=True)
	t.start()
	sys.stdout.flush()
	print("begin temp sensing")
	task = time_track()
	t = threading.Thread(target=task, args=(data, ), daemon=True)

main()
