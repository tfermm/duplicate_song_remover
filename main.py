import unicodedata
import mutagen
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3
from mutagen.id3 import ID3 as ID3
import os
 
import glob
  
directory = "./"
badSongs = []  
f = []
f = glob.glob(directory + "*.m4a")
f = f + glob.glob(directory + "*.mp3")
music = {}
hadIssues = False
for i in f:
	try:
		dir_len = directory.__len__()
		file_name = i[dir_len:]
		split = i.split(".")
		split2 = split[2]
# section for m4a files
# m4a in this case is iTunes
		if split2 == ("m4a"):
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
					name = " ".join(temp).lstrip().lower()
					temp2 = music.get(artist)
					if temp2.has_key(name):
						print '"' + temp2.get(name)["location"] + '"' + " and " + '"' + i + '"' + " are duplicates"
						if bitrate < temp2.get(name)["bitrate"]:
							print "\tRemoving " + '"' + i + '"'
							os.remove(i)
						else:
							print "\tRemoving " + '"' + temp2.get(name)["location"] + '"'
							os.remove(temp2.get(name)["location"])
						#print "duplicate"
				elif tag == "ART":
					temp[0] = "";
					artist = " ".join(temp).lstrip().lower()
				if not music.has_key(artist):
					music[artist] = {}
				music[artist][name] = {}
				music[artist][name]["name"] = name;
				music[artist][name]["file_name"] = file_name;
				music[artist][name]["location"] = i;
				music[artist][name]["bitrate"] = bitrate;
		elif split2 == "mp3":
			audio = MP3(i)

			bitrate = audio.info.bitrate
			x = audio.pprint().split('\n')
			name=""
			artist=""
			for j in x:
				temp = j.split("=")
				tag = temp[0]
				if tag == "TIT2":
					temp[0] = "";
					name = " ".join(temp).lstrip().lower()
					name = name.encode('ascii', 'ignore')
				elif tag == "TPE1":
					temp[0] = "";
					artist = " ".join(temp).lstrip().lower()
					artist = artist.encode('ascii', 'ignore')
					if not music.has_key(artist):
						music[artist] = {}
					temp2 = music.get(artist)
					if temp2.has_key(name):
						print temp2.get(name)["name"] + " and " + i + " are duplicates"
						if bitrate < temp2.get(name)["bitrate"]:
							print "\tRemoving " + '"' + i + '"'
							os.remove(i)
						else:
							print "\tRemoving " + '"' + temp2.get(name)["location"] + '"'
							os.remove(temp2.get(name)["location"])
						#print "duplicate"
				if not music.has_key(artist):
						music[artist] = {}

				music[artist][name] = {}
				music[artist][name]["name"] = name;
				music[artist][name]["file_name"] = file_name;
				music[artist][name]["location"] = i;
				music[artist][name]["bitrate"] = bitrate;
	except:
		badSongs.append(i)
print "valid Songs\n"
for i in range(1, len(music)):
 	artist = music.keys()[i]
 	print music.keys()[i] + "\n"
	songs = music.get(artist)
 	for j in range(0, len(songs)):
 		song = songs.keys()[j]
 		print "\t" + song
 	print "\n"



for song in badSongs:
	if not hadIssues:
		print "invalid songs path"
		file = open('errors.txt','w')
		file.close()

	hadIssues = True
	file = open('errors.txt','a')
	file.write(song)
	print "\t" + song
	file.close()
if hadIssues:
	print "All songs that had issues are in errors.txt"
