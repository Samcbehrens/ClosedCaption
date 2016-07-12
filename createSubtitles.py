import pysubs2

subs =[]

def loadTemplate():
	global subs
	subs = pysubs2.load("template.srt");
	del subs[0:2]

def createEvent(content,start, end, ):
	ev = pysubs2.SSAEvent(start=pysubs2.make_time(s=start), end=pysubs2.make_time(s=end), text=content)
	return ev 

def addEvent(i, event):
	global subs  
	print "in add event"
	print event
	subs.insert(i, event)

def createTranscript(subtitleArray, captionFinalTitle):
	loadTemplate()

	for x in range(len(subtitleArray)):
		event = createEvent(subtitleArray[x][0], subtitleArray[x][1], subtitleArray[x][2])
		print event 
		addEvent(x, event)
	
	saveTranscript(captionFinalTitle)


def saveTranscript(finalName):
	global subs 
	subs.save(finalName);
