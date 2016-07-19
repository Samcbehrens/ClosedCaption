from itertools import groupby
import collections
import spellChecker as sp

def getIBMObjects(ibmResults):
	result = {"transcript" : ibmResults['results'][0]['alternatives'][0]['transcript'], "confidence": ibmResults['results'][0]['alternatives'][0]['confidence'], "wordConfidence" : ibmResults['results'][0]['alternatives'][0]['word_confidence'] }
	return result
def getWitObjects(witResults):
	result = {"transcript": witResults["_text"], "confidence": witResults["outcomes"][0]["confidence"]}
	return result

def getBingObjects(bingResults):
	result ={"transcript":bingResults['results'][0]["lexical"] , "confidence":bingResults['results'][0]['confidence']}
	return result

def getAiObjects(aiResults):
	result = {"transcript": aiResults["asr"]}
	return result

def createDictionary(results, confidence):
	newResults = []
	diction = {"word": None , "confidence": None}
	for n in results:
		diction["word"] = n
		if confidence != None:
			diction["confidence"] = confidence
		else: 
			diction["confidence"] = "0"
		newResults.append(diction)
		diction = {"word": None , "confidence": None}
	return newResults  

def compareResults(witResults, bingResults, aiResults, ibmResults):
	ibmObjects = getIBMObjects(ibmResults)
	bingObjects = getBingObjects(bingResults)
	aiObjects = getAiObjects(aiResults)
	witObjects = getWitObjects(witResults)

	ibmArray = ibmObjects['wordConfidence']
	newDict = {"word" : None, "confidence": None}
	ibmDict = []

	for x in range(len(ibmArray)):
		newDict["word"]=ibmArray[x][0]
		newDict["confidence"]= ibmArray[x][1]
		ibmDict.append(newDict);
		newDict = {"word" : None, "confidence": None}


	bingArray = bingObjects['transcript'].split()
	bingDict = createDictionary(bingArray, bingObjects['confidence'])

	witArray = witObjects['transcript'].split()
	witDict = createDictionary(witArray, witObjects['confidence'])

	aiArray1, aiConf1 = aiObjects['transcript'].popitem()
	aiArray1 = aiArray1.split()
	aiDict1 = createDictionary(aiArray1, aiConf1)

	aiArray2, aiConf2 = aiObjects['transcript'].popitem()
	aiArray2 = aiArray2.split()
	aiDict2 = createDictionary(aiArray2, aiConf2)

	aiArray3, aiConf3 = aiObjects['transcript'].popitem()
	aiArray3 = aiArray3.split()
	aiDict3 = createDictionary(aiArray3, aiConf3)

	apiWordArray = [ibmDict, bingDict, aiDict1, aiDict2, aiDict3, witDict]

	#find longest one
	longestArray = len(max(apiWordArray, key=len))

	foo = None
	## create array 
	words=[[foo for i in range(len(apiWordArray))] for j in range(longestArray)]

	for bigIndex, array in enumerate(apiWordArray):
		for littleIndex, item in enumerate(array):
			words[littleIndex][bigIndex] = item 

	words = [[{'word':' ',  'confidence': 1.0} if x is None else x for x in c] for c in words]	
	
	finalWords = [];
	for wordGroup in words:
		chosenWord = chooseCorrectWord(wordGroup)
		chosenWord = chosenWord['word']
		finalWords.append(chosenWord)

	finalWords = " ".join(finalWords).rstrip()
	print "finalArray"
	print finalWords
	finalWords = sp.checkGrammar(finalWords)
	return finalWords

def chooseCorrectWord(ArrayDictionaries):
	singleWords = [d['word'] for d in ArrayDictionaries]

	if(all(x==singleWords[0] for x in singleWords)):
		return singleWords[0]
	else: 
		grouped = createGroups(ArrayDictionaries);
		findWords = createSum(grouped)
		chosen = sorted(findWords, key = lambda k:k['sum'], reverse = True ) 
		chosen = chosen[0]
		return chosen

def createGroups(ArrayDictionaries): 
	itemsByWord = collections.defaultdict(list)
	for item  in ArrayDictionaries:
		itemsByWord[item['word']].append(item)
	return itemsByWord

def createSum(groupedItems): 
	wieghtedAvg = []
	counter = -1; 

	for k,v in groupedItems.iteritems():
		counter = counter+1;
		l = {"word": k, "sum": 0}
		wieghtedAvg.append(l)

		for item in v: 
			if item['confidence'] == None:
				item['confidence'] = 0
			wieghtedAvg[counter]['sum'] = wieghtedAvg[counter]['sum'] + float(item['confidence'])
		counter = 0;
	return wieghtedAvg
