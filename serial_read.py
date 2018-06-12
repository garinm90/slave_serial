#!/usr/bin/env python

import time
import serial
import subprocess
import threading
import os

lines = []
playlist_path = "/home/fpp/media/playlists/"
play = ["/opt/fpp/bin.pi/fpp", "-P",]
stop = ["/opt/fpp/bin.pi/fpp", "-d"]
flag = 0
try:
	ser = serial.Serial(port='/dev/ttyUSB0',baudrate = 115200, timeout=1)
except:
	pass
time.sleep(117)


def get_playlist():
    files = os.listdir(playlist_path)
    sequence = ""
    os.path.isfile
    if os.path.isfile(playlist_path + "".join(files)):
        play.append(files[0])
        with open(playlist_path + "".join(files)) as file:
            for line in file:
                lines.append(line.strip())
        sequence = "".join(lines[1].lstrip('s').split(','))
        play.append(sequence)        

def check_play():
	while True:
		time.sleep(3)
		playStatus = subprocess.check_output(["/opt/fpp/bin.pi/fpp", "-s"])
        playStatus = playStatus.split(',')
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
			#print serData
		if serData == 'p':
			subprocess.call(stop)
			subprocess.call(play)
			#print("Play")
		#elif serData == 't':
		#	play.append(playlist[1])
        	#	subprocess.call(stop)
        	#	subprocess.call(play)
	
if __name__ == "__main__":
	get_playlist()
	t1 = threading.Thread(target = check_play)
	t2 = threading.Thread(target = serCheck)
	t1.setDaemon(True)
	t2.setDaemon(True)
	t1.start()
	t2.start()
	while True:
		time.sleep(.5)
		pass
