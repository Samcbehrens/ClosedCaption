FFMEG_BIN = "ffmpeg"
import subprocess as sp 
import sys
import numpy

def extractAudio(audioPath, newFileName):
	
	extract = "ffmpeg -i audioPath ab 160k -ac 2 -ar 44100 -vn newFileName.wav"
	subprocess.call(extract, shell = True)

if __name__ == "__main__":
	extractAudio(sys.argv[1], sys.argv[2])