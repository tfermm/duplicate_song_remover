import unicodedata
import mutagen
from mutagen.mp4 import MP4
import os

import glob

directory = "."

f = []
f = glob.glob(directory + "/*.m4a")

for i in f:
 	split = i.split(".")
	split = split[2]

	if split == ("m4a"):
		audio = MP4(i) 

		x = audio.pprint()
		audio = x.encode('ascii', 'ignore').split('\n')
		for j in audio:
#			print j
			temp = j.split("=")
			tag = temp[0]
			if tag == "nam":
				temp[0] = "";
				name = " ".join(temp).lstrip()
			elif tag == "ART":
				temp[0] = "";
				artist = " ".join(temp).lstrip()
				print artist
