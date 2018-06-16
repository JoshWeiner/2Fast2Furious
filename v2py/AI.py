import os
import signal
import random
import time
import sys

def printSys():
	userIn = raw_input()
	while userIn != "--q--":
		print compTxt(userIn)
		userIn = raw_input()
	print("Program quit ... all processes completed and saved")

def compTxt(inputTxt):
	inputs = os.listdir("./Inputs")
	for file in inputs:
		readInputFile = open("./Inputs/" + file, "r").read().split("\n")
		if inputTxt in readInputFile:
			if file != "farewell":
				readOutputFile = open("./Outputs/" + os.path.basename(file), "r").read().split("\n")
				return random.choice(readOutputFile)
			else:
				readOutputFile = open("./Outputs/" + os.path.basename(file), "r").read().split("\n")
				print random.choice(readOutputFile)
				sys.exit()
	defProtocol(inputTxt)

def defProtocol(inputTxt):
	print "I don't quite understand yet. How should I respond to this?\n"
	response = raw_input()

	print "\nWhat category does this belong in?"
	categs = os.listdir("./Inputs")
	categNames = list()
	for file in categs:
		print os.path.basename(file) + "\n"
		categNames.append(os.path.basename(file))
	category = raw_input()

	inputFile = open("./Inputs/" + category, "a+")
	inputFile.append(inputTxt)
	inputFile.close()

	outputFile = open("./Outputs/" + category, "a+")
	inputFile.append(response)
	outputFile.close()

	print "Thanks for improving me!"

printSys()