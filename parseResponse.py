
def createSubObject(sentence, startTime, endTime):
	subtitleObject = [sentence, startTime, endTime]
	return subtitleObject

def addToSentence(subArray, appendPhrase):
	subArray[len(subArray)-1][0] = subArray[len(subArray)-1][0]+" "+appendPhrase

def parse(postResponse):
	postResponse = postResponse['results'][0]['alternatives'][0]['timestamps']
	print postResponse


	sentence  = ""
	subtitleArray = []
	startTime = 0

	for i in range(len(postResponse)):
		

		if i % 5 == 0:
			print "in if "
			print sentence
			print subtitleArray

			sentence = sentence+ " " + postResponse[i][0]

			subtitleObject = createSubObject(sentence, startTime,postResponse[i][2] )
			subtitleArray.append(subtitleObject)

			sentence = ""

		elif i == len(postResponse)-1:
			print "in else if "
			print sentence
			print subtitleArray

			sentence = sentence+ " " + postResponse[i][0]
			addToSentence(subtitleArray, sentence)

		else:
			print("in else")
			print sentence
			print subtitleArray

			startTime = postResponse[i][1]
			sentence = sentence+ " " + postResponse[i][0]
			

	return subtitleArray
	
	