#!/usr/bin/env python
#coding: utf-8

# Written by spoonie (Rick Spooner) for RobotsGo 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
