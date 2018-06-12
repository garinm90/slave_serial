#!/usr/bin/env python

import time
import serial
import subprocess
import threading
import os.path


playlist_path = "/home/fpp/media/playlists"
play = ["/opt/fpp/bin.pi/fpp", "-P", "1", "comp2fAfixt2ff.fseq"]
stop = ["/opt/fpp/bin.pi/fpp", "-d"]
flag = 0
ser = serial.Serial(port='/dev/ttyUSB0',baudrate = 115200, timeout=1)
#time.sleep(117)


def get_playlist():
    for playlist_path, subdir, files  in os.walk(playlist_path):
        for name in subdir:
            print os.path.join(playlist_path,name)
        for name in files:
            print os.path.join(playlist_path,name)

def check_play():
	while True:
		time.sleep(3)
		playStatus = subprocess.check_output(["/opt/fpp/bin.pi/fpp", "-s"])
        	playStatus = playStatus.split(',')
        	print playStatus
		print playStatus[1]
		if int(playStatus[1]) == 0:
			subprocess.call(play)
		else:
			pass

def serCheck():
	while True:
	#read data from serial port
		time.sleep(1)
		serData = ser.readline()
		serData = serData.strip('\n')
		serData = serData.strip('\r')
		serData = serData.strip('\x00')
	#serData = serData.decode("ascii")  #.replace('\x00', '').replace("\r\n", "")
	#if there is smth do smth
		if len(serData) >= 1:
			print serData
		if serData == 'p':
			subprocess.call(stop)
			subprocess.call(play)
			print("Play")
		#elif serData == 't':
		#	play.append(playlist[1])
        	#	subprocess.call(stop)
        	#	subprocess.call(play)
	
if __name__ == "__main__":
	t1 = threading.Thread(target = check_play)
	t2 = threading.Thread(target = serCheck)
	t1.setDaemon(True)
	t2.setDaemon(True)
	t1.start()
	t2.start()
	while True:
		time.sleep(.5)
		pass