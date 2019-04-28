import upload_bucket
import temp_track
#Camera Library
from picamera import PiCamera, Color
from time import sleep
import time
import datetime
import os
#Picture Library
from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import atexit

DESTINATION = '/home/pi/Desktop/security/'
IMAGE_ONE = DESTINATION+'pic_one.jpeg'
IMAGE_TWO = DESTINATION+'pic_two.jpeg'
IMAGE_GOOD_CAPTURE_LAST = DESTINATION+'pic_last_good.jpeg'
IMAGE_RECENT = DESTINATION+'pic_recent.jpeg'

Camera = PiCamera()
Started = False

DiffThreshold = .7

##Make directory to save pictures
if (os.path.isdir('/home/pi/Desktop/security/')==False):
	os.mkdir('/home/pi/Desktop/security/')

def start_camera():
	global Camera
	setup_camera_lowres(Camera)
	opposite = False
	while True:
		if(takePictureAnalysis(Camera, opposite)):
			trigger_event(Camera)
		sleep(.4)
		print("temp " + temp_track.poll_temp())
		opposite = not opposite

def trigger_event(camera):
	takePictureBurst(camera)
	upload_bucket.upload_newest_pic()
	print("Upload!")

def setup_camera_highres(camera):
	camera.rotation = 180
	camera.start_preview(alpha = 200)
	camera.resolution = (400,400)

def setup_camera_lowres(camera):
	camera.rotation = 180
	camera.start_preview(alpha = 200)
	camera.resolution = (200,200)

def takePictureAnalysis(camera, opposite):
	global Started
	if(opposite):
		camera.capture(IMAGE_ONE)
		camera.capture(IMAGE_RECENT)
	else:
		camera.capture(IMAGE_TWO)
	opposite = not opposite
	if(not Started):
		Started = True
		return False
	diff = compareTwoPics(IMAGE_ONE, IMAGE_TWO)
	if (diff < DiffThreshold):
		return True
	return False

def takePictureBurst(camera):
	setup_camera_highres(camera)
	st = ""
	for i in range(5):
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime(DESTINATION+'%m|%d|%Y_%H:%M:%S:%f')
		print st
		camera.capture(st+'.jpg')
	camera.capture(IMAGE_GOOD_CAPTURE_LAST)
	setup_camera_lowres(camera)

def compareTwoPics(pic1, pic2):
#	print("start ssim")
	img1 = cv2.imread(IMAGE_ONE)
	img2 = cv2.imread(IMAGE_TWO)
	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	s = ssim(img1, img2)
#	print('end ssim: '+str(s))
	return s

def exit_message():
	print("\nEnd of camera!\n")

atexit.register(exit_message)
