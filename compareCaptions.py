from itertools import groupby


def getIBMObjects(ibmResults):
	result = {"transcript" : ibmResults['results'][0]['alternatives'][0]['transcript'], "confidence": ibmResults['results'][0]['alternatives'][0]['confidence'], "wordConfidence" : ibmResults['results'][0]['alternatives'][0]['word_confidence'] }
	return result
def getWitObjects(witResults):
	result = {"transcript": witResults["_text"]}
	return result

def getBingObjects(bingResults):
	result ={"transcript":bingResults['results'][0]["lexical"] , "confidence":bingResults['results'][0]['confidence']}
	return result

def getAiObjects(aiResults):
	result = {"transcript": aiResults["asr"]}
	return result

def compareResults(witResults, bingResults, aiResults, ibmResults):
	ibmObjects = getIBMObjects(ibmResults)
	bingObjects = getBingObjects(bingResults)
	aiObjects = getAiObjects(aiResults)
	witObjects = getWitObjects(witResults)

	ibmArray = ibmObjects['transcript'].split()
	bingArray = bingObjects['transcript'].split()
	witArray = witObjects['transcript'].split()
	aiArray1, aiConf1 = aiObjects['transcript'].popitem().split()
	aiArray2, aiConf2 = aiObjects['transcript'].popitem().split()
	aiArray3, aiConf3 = aiObjects['transcript'].popitem().split()



	apiWordArray = [ibmArray, bingArray, aiArray1, aiArray2, aiArray3, witArray]

	##group by length in case they are not the same
	groups = groupby(sorted(apiWordArray, key=len), key=len)

	#find longest one
	longestArray = len(max(apiWordArray, key=len))

	## create array 
	words = [None]*longestArray

	for arraysByLenth in groups:
		for array 

