import transcribeCore as core
import seperateAudio as seperate
import sys 
import yaml

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

	witKey = data["service"]["Wit"]["key"]
	witKey=yaml.safe_load(witKey)
	core.witAi(witKey,r, audioSource)