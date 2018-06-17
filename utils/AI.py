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
storeStr = ""
storeFilepath = ""

def printSys(inputTxt):
	if improvingAI == False:
		if inputTxt != "--q--":
			return compTxt(inputTxt)
		else:
			return("Program quit ... all processes completed and saved")
	else:
		return defProtocol(inputTxt)

def compTxt(inputTxt):
	global addTo
	inputs = os.listdir("./static/Inputs")
	for file in inputs:
		filepath = "./static/Inputs/" + file
		readInputFile = open(filepath, "r")
		r = readInputFile.readlines()
		for line in r:
				if inputTxt in line:
					print filepath
					categs = os.listdir("./static/Outputs")
					if file in categs:
						if file != "farewell":
							readOutputFile = open("./static/Outputs/" + file, "r").read().split("\n")
							return(random.choice(readOutputFile))
						else:
							readOutputFile = open("./static/Outputs/" + file, "r").read().split("\n")
							return random.choice(readOutputFile)
					else:
						addTo = True
						addResp = False
						listedOptions = True
						improvingAI = True
						return defProtocol(file)
	addTo = True;
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
			print("BOOOLL")
			outputFile = open("./static/Outputs/" + storeFilepath , "a+")
			if len(storeStr > 1):
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
