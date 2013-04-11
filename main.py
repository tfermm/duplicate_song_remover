import unicodedata
import mutagen
from mutagen.mp4 import MP4
from mutagen.id3 import ID3,TIT2
from mutagen.easyid3 import EasyID3
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
			temp = j.split("=")
			if temp[0] == "nam":
				temp[0] = "";
				temp = " ".join(temp).lstrip()
				print temp
