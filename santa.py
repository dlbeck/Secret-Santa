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

			""".format(participant, gifterToGiftee[participant])

			server.login(senderEmail, senderEmailpass)
			server.sendmail(senderEmail, participantToEmail[participant], message)
			print("email sent from " + senderEmail + " to " + participantToEmail[participant])

def main():
	senderEmail = "lotnsecretsanta@gmail.com"
	participantToEmail = {
		"Alice": "lotnsecretsanta" + "alice" + "@gmail.com",
		"Bob": "lotnsecretsanta" + "bob" + "@gmail.com",
		"Charlie": "lotnsecretsanta" + "charlie" + "@gmail.com",
		"Dan": "lotnsecretsanta" + "dan" + "@gmail.com",
    }
	gifterToGiftee = createPairings(list(participantToEmail.keys()))
	print(gifterToGiftee)
	# createAndSendEmail(senderEmail, participantToEmail, gifterToGiftee)

if __name__ == "__main__":
    main()


