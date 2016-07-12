FFMEG_BIN = "ffmpeg"
import subprocess as sp 
import sys
import numpy

def extractAudio(videoPath, newFileName):
	
	extract = "ffmpeg -i " + videoPath + " " + newFileName
	# extract = "ffmpeg -i audioPath ab 160k -ac 2 -ar 44100 -vn newFileName.wav"
	sp.call(extract, shell = True)

def addCaptionToVideo(originalMovie,captionFile,outFileName):
	addCommand = "ffmpeg -i " + originalMovie + " -f srt -i " + captionFile + " -c:v copy -c:a copy -c:s mov_text "+ outFileName
	sp.call(addCommand, shell = True)
