import sys
import json
import smtplib, ssl
import random
from getpass import getpass

def createPairings(participants):
	random.shuffle(participants)
	while True:
		gifteesLeft = participants.copy()
		pairMappings = {}
		for gifter in participants:
			while True:
				giftee = random.choice(gifteesLeft)
				if giftee != gifter:
					pairMappings[gifter] = giftee
					gifteesLeft.remove(giftee)
					print(gifter + ' to ' + giftee)
					break
				elif len(gifteesLeft) == 1:
					break
		if len(gifteesLeft) == 0:
			return pairMappings


def createAndSendEmail(senderEmail, participantToEmail, gifterToGiftee):
	port = 465  # For SSL
	smtpServer = "smtp.gmail.com"
	senderEmailpass = getpass("Type the password for {} and press enter: ".format(senderEmail))
	
	for participant in list(participantToEmail.keys()):
		context = ssl.create_default_context()
		with smtplib.SMTP_SSL(smtpServer, port, context=context) as server:
			message = """\
			Subject: Secret Santa

			Hello {},

			You will be purchasing a gift for {}

			The code used to generate this email and the secret santa assignments can be found here: https://github.com/dlbeck/Secret-Santa

			""".format(participant, gifterToGiftee[participant])

			server.login(senderEmail, senderEmailpass)
			server.sendmail(senderEmail, participantToEmail[participant], message)
			print("email sent from " + senderEmail + " to " + participantToEmail[participant])

def main():
	if len(sys.argv) != 3:
		print("Invalid arguments. Run like 'python3 santa.py sender@email.com participantToEmail.txt'")
		sys.exit()
	
	senderEmail = sys.argv[1]
	with open(sys.argv[2]) as f:
		data = f.read()
	participantToEmail = json.loads(data)
	  
	gifterToGiftee = createPairings(list(participantToEmail.keys()))
	print(gifterToGiftee)
	createAndSendEmail(senderEmail, participantToEmail, gifterToGiftee)

if __name__ == "__main__":
    main()


