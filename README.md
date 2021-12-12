# Secret-Santa
Script to create secret santa pairings and email participants who they are purchasing gives for. This script assumes that the sender email is a gmail account (the participant emails are not required to be gmail accounts).

`Argument1`: Email account that will send email to participants. Note that this email address must have [Less secure app access](https://support.google.com/accounts/answer/6010255?hl=en) turned on in their google account. For this reason it is advisable to use a burner email.

`Argument2`: Path to json file defining the participants and their email accounts. A sample `participantsToEmail.json` with the proper name, email pair format is provided in this repo. This file can be easily configured to contain custom participant information.

Simply run the script like:
```
python3 santa.py sender@gmail.com participantToEmail.json
```