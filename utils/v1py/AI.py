import os
import signal
import random
import time

def printSys():
	userIn = raw_input()
	while userIn != "quit prog":
		print compTxt(userIn)
		userIn = raw_input()
	print("Good bye!")

def compTxt(inputTxt):
	for file in os.listdir(os.getcwd()):
		if not(file.startswith(".")):
			# print file
			if file.endswith("Inputs"):
				compingFileRead = open(file, "r").read()
				listOfWords = compingFileRead.split("\n")
				# print listOfWords
				# print inputTxt
				if inputTxt in listOfWords:
					outputFile = file[:-6] + "Outputs"
					# print outputFile
					respFileRead = open(outputFile, "r").read()
					listOfOutputs = respFileRead.split("\n")
					# print listOfOutputs
					# print respFileRead
					return (random.choice(listOfOutputs))
	print("I don't understand, please enlighten me by following the instructions below:")
	print("What category do you want me to store this in?")
	categ = raw_input()
	fileCheck(categ, inputTxt, "Inputs")
	print("What do you want me to say?")
	resp = raw_input()
	fileCheck(categ, resp, "Outputs")
	return ("Thank you for improving me, I will do my best to answer your questions in the   future.")

def fileCheck(userCateg, inputTxt, typeInOut):
	for file in os.listdir(os.getcwd()):
		if file == userCateg + typeInOut:
			writeToFile = open(file, "a")
			writeToFile.write("\n" + inputTxt)
			writeToFile.close()
			break
		else:
			if typeInOut == "Inputs":
				print("There is no category currently for this.")
				print("Would you like me to create a new category?")
			else:
				print('''Would you like me to create the corresponding category?''')
			userInputCategBool = raw_input()
			if userInputCategBool == "Yes":
				openNew = open(userCateg + typeInOut, "w+")
				openNew.write(inputTxt)
				openNew.close()
				pass
			else:
				os.remove(userCateg + typeInOut)
				print('''Ok, your privacy is of utmost importance, I will not write down any feedback for this.
					However, the next time you ask this question, you will be prompted to follow the instructions again.
					Thank you.''')
				pass
			break

print('''================================================================================Important Notice: If any bugs are noticed with this program, please notify the  owner: Bill Ni, ASAP. Thank You                                                 Please note: During this session, please type with proper grammar, punctuation, and whitespace so that you get the best experience.                             ================================================================================''')

printSys()
