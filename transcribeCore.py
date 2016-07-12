import json 
from pprint import pprint
import sys 
import speech_recognition as sr
from os import path



def printByResponseType(response, showMore):
	if showMore:
		pprint(response)
	else:
		print response

def readJson(jsonFile):
	with open(jsonFile) as data_file:    
		data = json.load(data_file)
	return data

def setAudioFile(audioFileName):
	audioFile = path.join(path.dirname(path.realpath(__file__)), audioFileName)
	return audioFile

def setRecognizer():
	r = sr.Recognizer()
	return r 

def setAudioSource(audioFile,r):
	with sr.AudioFile(audioFile) as source:
		audio = r.record(source) # read the entire audio file
	return audio

def googleSpeech(googleKey, r, audio,showMore):
	try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`
		print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

def witAi(witKey,r, audio,showMore):
	try:
		print "witAi"
		response = r.recognize_wit(audio, key=witKey, show_all=showMore)
		printByResponseType(response,showMore)

	except sr.UnknownValueError:
		print("Wit.ai could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Wit.ai service; {0}".format(e))

def bingVoice(bingKey,r, audio,showMore):
	try:
		print "bing"
		response = r.recognize_bing(audio, key=bingKey,show_all=showMore)
		printByResponseType(response,showMore)

	except sr.UnknownValueError:
		print("Microsoft Bing Voice Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

def AI(aiKey,r, audio,showMore):
	try:
		print "AI"
		response = r.recognize_api(audio, client_access_token=aiKey,show_all=showMore)
		printByResponseType(response,showMore)
	except sr.UnknownValueError:
		print("api.ai could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from api.ai service; {0}".format(e))

def IBM(username, password,r, audio,showMore):
	try:
		print "IBM"
		response = r.recognize_ibm(audio, username=username, password=password,show_all=showMore)
		printByResponseType(response,showMore)
		return(response)
	except sr.UnknownValueError:
		print("IBM Speech to Text could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from IBM Speech to Text service; {0}".format(e))

