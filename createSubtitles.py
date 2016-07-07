import pysubs2

global subs 

def loadTemplate(templateName):
	subs = pysubs2.load("template.srt");

def createEvent(start, end, content):
	ev = pysubs2.SSAEvent(start=pysubs2.make_time(s=start), end=pysubs2.make_time(s=end), text=content)
	return ev 

def addEvent(event):
	subs.append(event)