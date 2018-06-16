import os
import signal
import random
import time

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
			readOutputFile = open("./Outputs/" + os.path.basename(file), "r").read().split("\n")
			return random.choice(readOutputFile)
	defProtocol(inputTxt)

def defProtocol(inputTxt):
	print "I don't quite understand yet. How should I respond to this?\n"
	response = raw_input()

	print "\nWhat category does this belong in?"
	categs = os.listdir("./Inputs")
	categNames = list()
	for file in categs:
		print os.path.basename(file.name) + "\n"
		categNames.append(os.path.basename(file.name))
	category = raw_input()

	inputFile = open("./Inputs/" + category, "a+")
	write(inputTxt)
	inputFile.close()

	outputFile = open("./Outputs/" + category, "a+")
	write(response)
	outputFile.close()

	print "Thanks for improving me!"

printSys()