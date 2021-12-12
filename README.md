# Secret-Santa
Script to create secret santa pairings and email participants who they are purchasing gives for

`Argument1`: Email account that will send email to participants. The sender email is assumed to be a gmail account (the participant emails are not required to be gmail accounts). Note that this email address must have [Less secure app access](https://support.google.com/accounts/answer/6010255?hl=en) turned on in their google account. For this reason it is advisable to use a burner email.

`Argument2`: Path to json file defining the participants with the fields "email", "address", and "disallowedGiftees". disallowedGiftees is a list of participants that the participant is not allowed to buy for. The script assumes that participants are not allowed to buy for themselves so it is unnecessary to list a participant in their disallowedGiftees. A sample participantsToEmail.json with the proper format is provided in this repo. This file can be easily configured to contain custom participant information.

Simply run the script like:
```
python3 santa.py sender@gmail.com participantToEmail.json
```

A test script was created to ensure createPairings follows the rules of the "disallowedGiftees" lists. This can be run like:
```
python3 test.py <numRuns>
```
where numRuns is an integer specifying the number of times to run the test (because createPairings is non-deterministic)