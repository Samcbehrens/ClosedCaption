
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

	print "postResponse Length"
	print len(postResponse) 

	print "finalSentence length"
	print len(finalSentence)

	for i in range(len(finalSentence)):
		print "current index"
		print i

		if i % 5 == 0:
			
			sentence = sentence+ " " + finalSentence[i]
			print "current word"
			print finalSentence[i]
			print "startTime"
			print startTime
			print "endTime"
			print postResponse[i][2]
			subtitleObject = createSubObject(sentence, startTime,postResponse[i][2] )
			subtitleArray.append(subtitleObject)

			sentence = ""

		elif i == len(finalSentence)-1:
			print "in elif"
			sentence = sentence+ " " + finalSentence[i]
			addToSentence(subtitleArray, sentence)

		elif i%5 ==1: 
			startTime = postResponse[i][1]
			sentence = sentence+ " " + finalSentence[i]
		else:
			print "in else"
			print i 
			print finalSentence[i]
			sentence = sentence+ " " + finalSentence[i]
			
	print "subtitleArray"
	print subtitleArray
	return subtitleArray
	
	