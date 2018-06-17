import os
import signal
import random
import time
import sys
import cgi

def printSys():
	userIn = raw_input()
	while userIn != "--q--":
		print compTxt(userIn)
		userIn = raw_input()
	print("Program quit ... all processes completed and saved")

def compTxt(inputTxt):
	inputs = os.listdir("./static/Inputs")
	for file in inputs:
		readInputFile = open("./static/Inputs/" + file, "r").read().split("\n")
		if inputTxt in readInputFile:
			if file != "farewell":
				readOutputFile = open("./static/Outputs/" + os.path.basename(file), "r").read().split("\n")
				return(random.choice(readOutputFile))
			else:
				readOutputFile = open("./static/Outputs/" + os.path.basename(file), "r").read().split("\n")
				return random.choice(readOutputFile)
				sys.exit()
	defProtocol(inputTxt)

def defProtocol(inputTxt):
	return "I don't quite understand yet. How should I respond to this?\n"
	response = raw_input()

	return "\nWhat category does this belong in?"
	categs = os.listdir("./static/Inputs")
	categNames = list()
	for file in categs:
		return os.path.basename(file) + "\n"
		categNames.append(os.path.basename(file))
	category = raw_input()

	inputFile = open("./static/Inputs/" + category, "a+")
	inputFile.append(inputTxt)
	inputFile.close()

	outputFile = open("./static/Outputs/" + category, "a+")
	inputFile.append(response)
	outputFile.close()

	return "Thanks for improving me!"

#printSys()
