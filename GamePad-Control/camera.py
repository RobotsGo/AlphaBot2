#!/usr/bin/env python
#coding: utf-8
import subprocess

def cameraOff():
    try:
        subprocess.call("sudo systemctl stop mjpgstreamer.service", shell=True)
    except Exception as e:
        print(e.message)
    
    
