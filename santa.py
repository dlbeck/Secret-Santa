import sys
import json
import smtplib, ssl
import random
from getpass import getpass

def createPairings(participantsDict):
	participantsList = list(participantsDict.keys())
	random.shuffle(participantsList) # unnecessary shuffle added for extra fun
	for gifter in participantsList:
		participantsDict[gifter]["disallowedGiftees"].append(gifter)

	while True:
		gifteesLeft = participantsList.copy()
		pairMappings = {}
		for gifter in participantsList:
			potentialGifteeExists = False
			for potentialGiftee in gifteesLeft:
				if not potentialGiftee in participantsDict[gifter]["disallowedGiftees"]:
					potentialGifteeExists = True
					break
			if not potentialGifteeExists:
				break # initiate global pairing redraw

			while True:
				giftee = random.choice(gifteesLeft)
				if not giftee in participantsDict[gifter]["disallowedGiftees"]:
					pairMappings[gifter] = giftee
					gifteesLeft.remove(giftee)
					break # move on to assigning the next gifter

		if len(gifteesLeft) == 0:
			print("gifter to giftee pairings created")
			return pairMappings


def createAndSendEmail(senderEmail, participantsDict, gifterToGiftee):
	port = 465  # For SSL
	smtpServer = "smtp.gmail.com"
	senderEmailpass = getpass("Type the password for {} and press enter: ".format(senderEmail))
	
	for gifter in list(participantsDict.keys()):
		giftee = gifterToGiftee[gifter]

		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtpServer, port, context=context) as server:
			message = "Subject: Secret Santa\n" \
			"Hello {},\n\nYou will be purchasing a gift for {} at the address: {}\n\n" \
			"The code used to generate this email and the secret santa assignments can be found here: https://github.com/dlbeck/Secret-Santa" \
			.format(gifter, giftee, participantsDict[giftee]["address"])

			server.login(senderEmail, senderEmailpass)
			sendeeEmail = participantsDict[gifter]["email"]
			server.sendmail(senderEmail, sendeeEmail, message)
			print("email sent from " + senderEmail + " to " + senderEmail)

def main():
	if len(sys.argv) != 3:
		print("Invalid arguments. Run like 'python3 santa.py sender@gmail.com participantToEmail.json'")
		sys.exit()
	
	senderEmail = sys.argv[1]
	with open(sys.argv[2]) as f:
		data = f.read()
	participantsDict = json.loads(data)
	  
	gifterToGiftee = createPairings(participantsDict)
	createAndSendEmail(senderEmail, participantsDict, gifterToGiftee)

if __name__ == "__main__":
    main()


