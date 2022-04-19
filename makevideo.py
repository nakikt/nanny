from time import sleep
from picamera import PiCamera
from subprocess import call
import requests
import datetime

BASE = "http://192.168.0.122:5000/sendvideo"

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(2)

ctime=datetime.datetime.now()
time=ctime.strftime('%d-%m-%Y-%H.%M.%S')
time=str(time)

file_name = 'images/video_'+time +'.h264'
file_name_mp4 = 'images/video_'+time +'.mp4'
print("Start recording...")
camera.start_recording(file_name)
camera.wait_recording(5)
camera.stop_recording()
print("Done.")

# Convert the h264 format to the mp4 format.
command = "MP4Box -add " + file_name + " " + file_name_mp4
call([command], shell=True)
print("\r\nRasp_Pi => Video Converted! \r\n")

with open('images/video_'+time +'.mp4', 'rb') as file:
	print('Rozpoczecie przesylania')
	dict = {'file': file}
	r = requests.post(BASE, files=dict)
	print("Wyslano video")
	exit()
