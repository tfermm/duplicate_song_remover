import unicodedata
import mutagen
from mutagen.mp4 import MP4
import os
 
import glob
 
directory = "."
 
f = []
f = glob.glob(directory + "/*.m4a")
music = {}
for i in f:
 	split = i.split(".")
 	split = split[2]
   
 	if split == ("m4a"):
 		audio = MP4(i) 
 
 		x = audio.pprint()
 		bitrate = audio.info.bitrate
 		audioDecoded = x.encode('ascii', 'ignore').split('\n')

		artist=""
		name=""
 		for j in audioDecoded:
 			temp = j.split("=")
 			tag = temp[0]
 			if tag == "nam":
 				temp[0] = "";
 				name = " ".join(temp).lstrip()
 			elif tag == "ART":
 				temp[0] = "";
 				artist = " ".join(temp).lstrip()
			if not music.has_key(artist):
				music[artist] = {}
			music[artist][name] = {}
			music[artist][name]["name"] = name;
			music[artist][name]["bitrate"] = bitrate;
			music[artist][artist] = artist
for i in range(1, len(music)):
	artist = music.keys()[i]
	print music.keys()[i] + "\n"
	songs = music.get(artist)
	for i in range(2, len(songs)):
		song = songs.keys()[i]
		print "\t" + song
	print "\n"
