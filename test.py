from santa import createPairings
import sys

def test():
	participantsDict = {
		"Alice": {
			"email": "alice@email.com",
			"address": "aliceAddr",
			"disallowedGiftees": [
				"Bob"
			]
		},
		"Bob": {
			"email": "bob@email.com",
			"address": "bobAddr",
			"disallowedGiftees": [
				"Alice",
				"Charlie"
			]
		},
		"Charlie": {
			"email": "charlie@email.com",
			"address": "charlieAddr",
			"disallowedGiftees": [
				"Bob"
			]
		},
		"Dan": {
			"email": "dan@email.com",
			"address": "danAddr",
			"disallowedGiftees": []
		},
		"Elliot": {
			"email": "elliot@email.com",
			"address": "elliotAddr",
			"disallowedGiftees": []
		},
		"Francis": {
			"email": "francis@email.com",
			"address": "francisAddr",
			"disallowedGiftees": []
		}
	}
	gifterToGiftee = createPairings(participantsDict)
	if gifterToGiftee["Alice"] == "Alice" or gifterToGiftee["Alice"] == "Bob":
		print(gifterToGiftee)
		return 1
	if gifterToGiftee["Bob"] == "Alice" or gifterToGiftee["Bob"] == "Bob" or gifterToGiftee["Bob"] == "Charlie]":
		print(gifterToGiftee)
		return 1
	if gifterToGiftee["Charlie"] == "Bob" or gifterToGiftee["Charlie"] == "Charlie":
		print(gifterToGiftee)
		return 1
	if gifterToGiftee["Dan"] == "Dan":
		print(gifterToGiftee)
		return 1
	if gifterToGiftee["Elliot"] == "Elliot":
		print(gifterToGiftee)
		return 1
	if gifterToGiftee["Francis"] == "Francis":
		print(gifterToGiftee)
		return 1
	return 0

def main():
	if(len(sys.argv) != 2):
		print("Invalid arguments. Run like 'python3 test.py <numRuns>'")
		sys.exit()

	numRuns = int(sys.argv[1])
	for i in range(numRuns):
		if test() == 1:
			print("Failed. Ran {} times".format(i))
	print("Passed. Ran {} times".format(numRuns))
		

if __name__ == "__main__":
	main()
