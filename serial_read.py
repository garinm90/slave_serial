#!/usr/bin/env python

import time
import serial
import subprocess
import threading
import os

previous_seconds = 0
interval = 5
lines = []
playlist_path = "/home/fpp/media/playlists/"
play = ["/opt/fpp/bin.pi/fpp", "-P", ]
stop = ["/opt/fpp/bin.pi/fpp", "-d"]
flag = 0
time.sleep(117)
try:
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=1)
    except:
        pass


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
        time.sleep(3)
        playStatus = subprocess.check_output(["/opt/fpp/bin.pi/fpp", "-s"])
        playStatus = playStatus.split(',')
        if int(playStatus[1]) == 0:
            subprocess.call(play)


def serCheck():
        # read data from serial port
        serData = ser.readline()
        serData = serData.strip('\n')
        serData = serData.strip('\r')
        serData = serData.strip('\x00')
        if len(serData) >= 1 and serData == 'p':
            subprocess.call(stop)
            subprocess.call(play)

def play_timer(seconds):
    global previous_seconds
    if (time.time() - previous_seconds > interval):
        previous_seconds = time.time()
#        print(previous_seconds)
        check_play()

if __name__ == "__main__":
    while True:
        get_playlist()
        serCheck()
        play_timer(interval)
