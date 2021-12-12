# Secret-Santa
Script to create secret santa pairings and email participants who they are purchasing gives for. This script assumes that all emails (sender and receivers) are gmail accounts.

`Argument1`: email account that will send email to participants. Note that this email address must have [Less secure app access](https://realpython.com/python-send-email/#:~:text=Allow%20less%20secure%20apps%20to%20ON) turned on in their google account. For this reason it is advisable to use a burner email.

`Argument2`: path to json file defining the participants and their email accounts. This file will look something like:
```
{
	"Alice": "alice@email.com",
	"Bob": "bob@email.com",
	"Charlie": "charlie@email.com",
}
```

Simply run the script like:
```
python3 santa.py sender@email.com participantToEmail.json
```