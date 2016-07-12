import pysubs2

subs =[]

def loadTemplate():
	global subs
	subs = pysubs2.load("template.srt");

def createEvent(content,start, end, ):
	
	ev = pysubs2.SSAEvent(start=pysubs2.make_time(s=start), end=pysubs2.make_time(s=end), text=content)
	return ev 

def addEvent(event):
	global subs  
	print "in add event"
	print event
	subs.append(event)

def createTranscript(subtitleArray, captionFinalTitle):
	loadTemplate()

	for tgroup in subtitleArray:
		event = createEvent(tgroup[0], tgroup[1], tgroup[2])
		print event 
		addEvent(event)
	
	saveTranscript(captionFinalTitle)

def saveTranscript(finalName):
	global subs 
	subs.save(finalName);
