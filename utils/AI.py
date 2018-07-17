import os
import signal
import random
import time
import sys
import cgi
import io

addTo = False
listedOptions = False
addResp = False
improvingAI = False
inCrisis = False
whatMatter = False
sendLocation = False
storeStr = ""
storeFilepath = ""
userName = ""
namePrime = False
knowName = False

def printSys(inputTxt):
	global inCrisis
	global sendLocation
	global whatMatter
	global improvingAI
	if inCrisis:
		return crisis(inputTxt)
	elif improvingAI:
		return defProtocol(inputTxt)
	elif improvingAI == False:
		if inputTxt != "--q--":
			return compTxt(inputTxt)
		else:
			return("Program quit ... all processes completed and saved")

def compTxt(inputTxt):
	global addTo
	global addResp
	global listedOptions
	global improvingAI
	global whatMatter
	global inCrisis
	global namePrime
	global userName
	global knowName
	newTxt = inputTxt.lower()
	if "my name" in newTxt and len(userName) < 1:
		namePrime = True
	if ("i'm in trouble.".find(newTxt) != -1) or ("please help me.".find(newTxt) != -1) or ("i need help.".find(newTxt) != -1):
		inCrisis = True
		return crisis(inputTxt)
	elif whatMatter == True:
		return crisis(inputTxt)
	else:
		inputs = os.listdir("./static/Inputs")
		for file in inputs:
			filepath = "./static/Inputs/" + file
			readInputFile = io.open(filepath, "r", encoding='cp1252')
			r = readInputFile.readlines()
			for line in r:
				newLine = line.lower()
				if namePrime:
					userTxt = inputTxt.split(" ")
					for word in userTxt:
						if "what" in inputTxt.lower() and knowName == False:
							namePrime = True
							return "I don't know yet! What is your name?"
						if word.lower() != "my" and word.lower() != "name" and word.lower() != "is" and knowName == False:
							userName += word + " "
							knowName = True
						namePrime = False
					if len(userName) > 1:
						return "Nice to meet you, " + userName
				elif newTxt in unicode(newLine) or unicode(newLine) in newTxt:
					categs = os.listdir("./static/Outputs")
					if file == "userNameQuery":
						return "Your name is " + userName
					elif file in categs:
						if file != "farewell":
							readOutputFile = open("./static/Outputs/" + file, "r").read().split("\n")
							retStr = random.choice(readOutputFile)
							if "your name" in retStr.lower():
								namePrime = True
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
			if inputTxt != ">":
				outputFile.write("\n" + inputTxt)
			outputFile.close()
			retStr += "Thank you for the input!"
			listedOptions = False
			addTo = False
			addResp = False
			improvingAI = False
		else:
			storeFilepath = inputTxt
			inputFile = open("./static/Inputs/" + storeFilepath , "a+")
			inputFile.write("\n"+ storeStr)
			inputFile.close()
			retStr += "Please let me know how I should respond to that."
			addTo = True
			addResp = True
			listedOptions = True
			improvingAI = True
		return retStr

					#printSys()

def crisis(inputTxt):
	global inCrisis
	global whatMatter
	newTxt = inputTxt.lower()
	#This is used to get the user location
	#ipaddress = getIPaddress()
	#setPlace  = ipaddress
	if whatMatter == False:
		whatMatter = True
		return "Please tell me what is the issue"
	elif whatMatter == True:
		inCrisis = False
		whatMatter = False
		if "no issue" in newTxt or "nothing" in newTxt:
			return "Gotcha, let me know if you need me for something else"
		elif "assault" in newTxt:
			return 'Here are some locations near you that can help with assault:<br>\
			<a href="http://www1.nyc.gov/site/nypd/bureaus/patrol/precincts/5th-precinct.page">5th Precinct - 19 Elizabeth St</a><br>\
			<a href="http://www1.nyc.gov/site/nypd/bureaus/patrol/precincts/1st-precinct.page">1st Precinct - 16 Ericsson Pl</a><br>\
			<a href="http://www1.nyc.gov/site/nypd/bureaus/patrol/precincts/9th-precinct.page">9th Precinct - 321 E 5th St</a>'
		elif "fire" in newTxt:
			return "Here are the locations of the nearest fire departments:<br>\
			Ladder 8 - 14 N Moore St<br>\
			Battalion 1 - 100 Duane St<br>\
			Battalion 2 - 363 Broome St<br>"
		elif "sick" in newTxt:
			return 'Here are the locations of the nearest medical care facilities:<br>\
			<a href="https://www.nyp.org/lowermanhattan">New York Presbytarian Hospital - 170 William St</a><br>\
			<a href="https://www.nychealthandhospitals.org/health_care/?doctor=&specialty=&filter_location=39346&condition=1">NYC Health and Hospitals - 227 Madison St</a><br>\
			<a href="https://nyulangone.org/locations/nyu-langone-medical-associates-canal-street">NYU Langone - 196 Canal St</a>'

'''def getIPaddress():
#The ip address of Gekko
parameters = "103.201.231.145"
#Use the place API for google to get nearlocation
response = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/output?input=parameters")
parameters = response.getLocation()
return "geoLocation"'''
