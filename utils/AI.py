import os
import signal
import random
import time
import sys
import cgi

addTo = False
listedOptions = False
addResp = False
improvingAI = False
inCrisis = False
whatMatter = False
sendLocation = False
storeStr = ""
storeFilepath = ""

def printSys(inputTxt):
	global inCrisis
	global sendLocation
	global whatMatter
	global improvingAI
	print inCrisis
	if inCrisis:
		return crisis(inputTxt)
	elif improvingAI == False:
		if inputTxt != "--q--":
			return compTxt(inputTxt)
		else:
			return("Program quit ... all processes completed and saved")
	else:
		return defProtocol(inputTxt)

def compTxt(inputTxt):
	global addTo
	global addResp
	global listedOptions
	global improvingAI
	global inCrisis
	newTxt = inputTxt.lower()
	if ("i'm in trouble.".find(newTxt) != -1) or ("please help me.".find(newTxt) != -1) or ("i need help.".find(newTxt) != -1):
		inCrisis = True
		return crisis(inputTxt)
	elif whatMatter == True:
		return crisis(inputTxt)
	else:
		inputs = os.listdir("./static/Inputs")
		for file in inputs:
			filepath = "./static/Inputs/" + file
			readInputFile = open(filepath, "r")
			r = readInputFile.readlines()
			for line in r:
				newLine = line.lower()
				if newTxt in newLine:
						categs = os.listdir("./static/Outputs")
						if file in categs:
							if file != "farewell":
								readOutputFile = open("./static/Outputs/" + file, "r").read().split("\n")
								retStr = random.choice(readOutputFile)
								if retStr != "ignoreOutput":
									return retStr
							else:
								readOutputFile = open("./static/Outputs/" + file, "r").read().split("\n")
								retStr = random.choice(readOutputFile)
								if retStr != "ignoreOutput":
									return retStr
						else:
							addTo = True
							addResp = False
							listedOptions = True
							improvingAI = True
							return defProtocol(file)
		addTo = True;
		improvingAI = True;
		return defProtocol(inputTxt)

def defProtocol(inputTxt):
	global addTo
	global listedOptions
	global addResp
	global storeStr
	global storeFilepath
	retStr = ""
	if addTo == True:
		improvingAI = True
		if listedOptions == False:
			storeStr = inputTxt
			retStr += "I don't quite understand yet. How should I respond to this? <br> \n"
			retStr += "\nTell me what category this belongs in! <br> \n"
			categs = os.listdir("./static/Inputs")
			categNames = list()
			for file in categs:
				retStr += os.path.basename(file) + "<br>\n"
				categNames.append(os.path.basename(file))
			listedOptions = True
			addResp = False
		elif addResp == True:
			outputFile = open("./static/Outputs/" + storeFilepath , "a+")
			if len(inputTxt) > 1:
				outputFile.write(inputTxt + "\n")
			outputFile.close()
			retStr += "Thank you for the input!"
			listedOptions = False
			addTo = False
			addResp = False
			improvingAI = False
		else:
			storeFilepath = inputTxt
			inputFile = open("./static/Inputs/" + storeFilepath , "a+")
			inputFile.write(storeStr + "\n")
			inputFile.close()
		 	retStr += "Please let me know how I should respond to that."
			addResp = True
			listedOptions = True
		return retStr

#printSys()

def crisis(inputTxt):
	global inCrisis
	global whatMatter
	newTxt = inputTxt.lower()
	if whatMatter == False:
		whatMatter = True
		return "Please tell me what is the issue"
	elif whatMatter == True:
		inCrisis = False
		whatMatter = False
		if "assault" in newTxt:
			return "Here are some locations near you that can help with assault:"
		elif "fire" in newTxt:
			return "Here are the locations of the nearest fire departments:"
		elif "sick" in newTxt:
			return "Here are the locations of the nearest medical care facilities:"
