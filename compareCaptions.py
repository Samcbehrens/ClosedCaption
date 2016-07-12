def getIBMObjects(bingResults):
	result = {"transcript" : bingResults['results'][0]["alternatives"][0]['transcript'], "confidence": bingResults['results'][0]["alternatives"][0]['transcript']}

def getWitObjects(witResults):
	result = {"transcript": witResults["_text"]}
	return result

def getBingObjects(bingResults):
	result ={"transcript":text['results'][0]["lexical"] , "confidence":text['results'][0]['confidence']}
	return result

def getAiObjects(aiResults):
	result = {"transcript": text["asr"]}

def compare(witResults, bingResults, aiResults, ibmResults):
	print "boo"