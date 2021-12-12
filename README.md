# Secret-Santa
Script to create secret santa pairings and email participants who they are purchasing gives for. This script assumes that all emails (sender and receivers) are gmail accounts.

Hardcoded values for user to update:

`senderEmail`: email account that will send email to participants. Note that this email address must have [Less secure app access](https://realpython.com/python-send-email/#:~:text=Allow%20less%20secure%20apps%20to%20ON) turned on in their google account. For this reason it is advisable to use a burner email.
`participantToEmail`: dictionary defining the participants and their email accounts.

Simply run the script like:
```
python santa.py
```