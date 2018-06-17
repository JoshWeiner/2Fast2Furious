import os
import signal
import random
import time
import sys
import cgi

addTo = False
listedOptions = False
addResp = False
storeStr = ""
storeFilepath = ""

def printSys(inputTxt):
	if listedOptions == False:
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
		newStr = inputTxt.split(" ")
		for line in r:
			for word in newStr:
				if word in line and len(word) > 3:
					categs = os.listdir("./static/Outputs")
					if file in categs:
						if file != "farewell":
							readOutputFile = open("./static/Outputs/" + file, "r").read().split("\n")
							return(random.choice(readOutputFile))
						else:
							readOutputFile = open("./static/Outputs/" + file, "r").read().split("\n")
							return random.choice(readOutputFile)
						sys.exit()
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
		else:
			if addResp == True:
				outputFile = open("./static/Outputs/" + storeFilepath , "a+")
				outputFile.write("\n" + inputTxt)
				outputFile.close()
				retStr += "Thank you for the input!"
				listedOptions = False
				addTo = False
				addResp = False
			else:
				storeFilepath = inputTxt
				inputFile = open("./static/Inputs/" + storeFilepath , "a+")
				inputFile.write("\n" + storeStr)
				inputFile.close()
		 		retStr += "Please let me know how I should respond to that."
				addResp = True
		return retStr

#printSys()
