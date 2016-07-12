def parse(postResponse):
	postResponse = postResponse['results'][0]['alternatives'][0]['timestamps']
	print postResponse


	sentence  = ""
	subtitleObject = []
	subtitleArray = []
	startTime = 0

	for i in range(len(postResponse)):
		

		if i % 5 == 0:

			subtitleArray.append(subtitleObject)

			subtitleObject = []

			sentence = sentence+ " " + postResponse[i][0]

			subtitleObject.append(sentence)
			subtitleObject.append(startTime)
			subtitleObject.append(postResponse[i][2])

			sentence = ""

		elif i == len(postResponse)-1:
			
			sentence = sentence+ " " + postResponse[i][0]
			subtitleObject.append(sentence)
			subtitleObject.append(startTime)
			subtitleObject.append(postResponse[i][2])
			subtitleArray.append(subtitleObject)

		else:
		
			startTime = postResponse[i][1]
			sentence = sentence+ " " + postResponse[i][0]
			

	subtitleArray.remove([])	
	return subtitleArray
	
	