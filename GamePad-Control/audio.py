#!/usr/bin/env python
#coding: utf-8

import subprocess

def soundOne():
	print("Playing burp-sound-effect.mp3")
	subprocess.Popen(['mpg123', 'burp-sound-effect.mp3'])
	
def soundTwo():
	print("Playing Cow-moo-sound.mp3")
	subprocess.Popen(['mpg123', 'Cow-moo-sound.mp3'])
	
def soundThree():
	print("Playing Dj-air-horn-sound-effect.mp3")
	subprocess.Popen(['mpg123', 'Dj-air-horn-sound-effect.mp3'])
	
def soundFour():
	print("Playing Duck-quack.mp3")
	subprocess.Popen(['mpg123', 'Duck-quack.mp3'])
