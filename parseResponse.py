
def createSubObject(sentence, startTime, endTime):
	subtitleObject = [sentence, startTime, endTime]
	return subtitleObject

def addToSentence(subArray, appendPhrase):
	subArray[len(subArray)-1][0] = subArray[len(subArray)-1][0]+" "+appendPhrase

def parse(postResponse, finalSentence):
	postResponse = postResponse['results'][0]['alternatives'][0]['timestamps']



	sentence  = ""
	subtitleArray = []
	startTime = 0

	for i in range(len(finalSentence)):
		
		print "what is this"
		print postResponse[i][0]

		if i % 5 == 0:
			
			sentence = sentence+ " " + finalSentence[i]

			subtitleObject = createSubObject(sentence, startTime,postResponse[i][2] )
			subtitleArray.append(subtitleObject)

			sentence = ""

		elif i == len(postResponse)-1:
		
			sentence = sentence+ " " + finalSentence[i]
			addToSentence(subtitleArray, sentence)

		else:
			
			startTime = postResponse[i][1]
			sentence = sentence+ " " + finalSentence[i]
			
	print "subtitleArray"
	print subtitleArray
	return subtitleArray
	
	