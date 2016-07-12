import transcribeCore as core
import seperateAudio as seperate
import sys 
import yaml
import parseResponse as p
from pprint import pprint
from parseResponse import parse

def setupForTrans(audioFileName,r):
	audioFile = core.setAudioFile(audioFileName)
	audioSource = core.setAudioSource(audioFile,r) 
	return audioSource


if __name__ == "__main__":
	videoFile= sys.argv[1]
	newAudioName = sys.argv[2]

	audioFromVideo = seperate.extractAudio(videoFile, newAudioName)
	data = core.readJson("config.json")

	r = core.setRecognizer()
	audioSource = setupForTrans(newAudioName,r)


	# witKey = yaml.safe_load(data["service"]["Wit"]["key"])
	# core.witAi(witKey,r, audioSource, False)

	# bingKey = yaml.safe_load(data["service"]["Bing"]["key1"])
	# core.bingVoice(bingKey,r,audioSource,False)

	# aiKey = yaml.safe_load(data["service"]["Ai"]["key"])
	# core.AI(aiKey, r, audioSource, False)

	IBMUsername = yaml.safe_load(data["service"]["IBM"]["username"])
	IBMPassword = yaml.safe_load(data["service"]["IBM"]["password"])
	results = core.IBM(IBMUsername, IBMPassword, r, audioSource, True)
	parsed = parse(results)

	


