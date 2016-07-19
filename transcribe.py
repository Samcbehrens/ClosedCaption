import transcribeCore as core
import movieOps as mOps
import sys 
import yaml
import parseResponse as p
from pprint import pprint
from parseResponse import parse
import createSubtitles as sub
import compareCaptions as cc

def setupForTrans(audioFileName,r):
	audioFile = core.setAudioFile(audioFileName)
	audioSource = core.setAudioSource(audioFile,r) 
	return audioSource


if __name__ == "__main__":
	videoFile= sys.argv[1]
	newAudioName = sys.argv[2]

	audioFromVideo = mOps.extractAudio(videoFile, newAudioName)
	data = core.readJson("config.json")

	r = core.setRecognizer()
	audioSource = setupForTrans(newAudioName,r)


	witKey = yaml.safe_load(data["service"]["Wit"]["key"])
	witResults = core.witAi(witKey,r, audioSource, True)

	bingKey = yaml.safe_load(data["service"]["Bing"]["key1"])
	bingResults = core.bingVoice(bingKey,r,audioSource,True)

	aiKey = yaml.safe_load(data["service"]["Ai"]["key"])
	aiResults = core.AI(aiKey, r, audioSource, True)

	IBMUsername = yaml.safe_load(data["service"]["IBM"]["username"])
	IBMPassword = yaml.safe_load(data["service"]["IBM"]["password"])
	ibmResults = core.IBM(IBMUsername, IBMPassword, r, audioSource, True)
	print "IBM results"
	print ibmResults

	results = cc.compareResults(witResults, bingResults, aiResults, ibmResults);
	split = results.split(" ");

	print "compiled sentence "
	print results

	parsed = parse(ibmResults, split)

	print "parsed IBM stuff"
	print parsed



	captionFile = "test.srt"
	finalTranscript = sub.createTranscript(parsed, captionFile)

	mOps.addCaptionToVideo(videoFile, captionFile, "newFile.mp4")


