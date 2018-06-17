import os
import signal
import random
import time
import sys
import cgi

addTo = False
listedOptions = False
storeStr = ""

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
		readInputFile = open("./static/Inputs/" + file, "r").readlines()
		newStr = inputTxt.split(" ")
		for word in newStr:
			if (len(word) > 4) and word in readInputFile:
				print("BOOL")
				if file != "farewell":
					readOutputFile = open("./static/Outputs/" + os.path.basename(file), "r").read().split("\n")
					return(random.choice(readOutputFile))
				else:
					readOutputFile = open("./static/Outputs/" + os.path.basename(file), "r").read().split("\n")
					return random.choice(readOutputFile)
				sys.exit()
	addTo = True;
	return defProtocol(inputTxt)

def defProtocol(inputTxt):
	global addTo
	global listedOptions
	global storeStr
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
			inputFile = open("./static/Inputs/" + inputTxt , "a+")
			inputFile.write("\n" + storeStr)
			inputFile.close()
	 		retStr += "Thanks for improving me!"
			listedOptions = False
			addTo = False
		return retStr

#printSys()
