import time
from random import randint
#starts count for timing
start_time = time.time()
#opens open readable dictionary
words = open("wordlist.txt", "r")
#original = "eductaion"
annagrams = []
#lists of letters
cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a','i','o','u','e','y']

		 	
def compare(l1, l2):
	isValid = True
	#compares all the letters in each word
	#removes one letter from the list to ensure the
	#same letter isn't counted twice
	for letter in l1:
		if letter in l2:
			l2.remove(letter)
		#allows words with less letters than original to be counted
		elif len(l2)<=0:
			isValid = True
		else:
			isValid = False
	return isValid

def checkValid(string):
	#ensures that the letters generated 
	#have a valid amount of vowels and consonants
	vCount = 0
	cCount =0
	for letter in string:
		if letter in vowels:
			vCount += 1
		else:
			cCount += 1
	if vCount >= 3 and cCount >= 4:
		return True
	else:
		return False

def generateWord():
	#generates the letters used for the countdown game
	finished = False
	#will allow def to keep running until a valid 
	#list is generated
	while finished == False:
		newWord = []
		for i in range(0,9):
			num = randint(0,1)
			if num == 1:
				newWord.append(cons[randint(0,20)])
			else: 
				newWord.append(vowels[randint(0,5)])
		if checkValid(newWord):
			print ("Letters are : ", newWord)
			finished = True
			return newWord
	
def mainOne():
	#actual main def of script
	#calls method to generate list of letters
	other = generateWord()
	#allows variable to be accessed outside of def
	mainOne.bestWord = ""
	for word in words:
		word = word.rstrip()
		#will not accept words less than four letters
		#calls the the compare def to ensure it's a valid word
		if len(word) <= len(other) and len(word) >= 4:
			if compare(other, list(word)) == True:
				annagrams.append(word)
				if len(mainOne.bestWord) < len(word):
					mainOne.bestWord = word
mainOne()
						
for annagram in annagrams:
	print(annagram)	
	
print("The Best Word is : ", mainOne.bestWord)
	

print("--- %s seconds ---" % (time.time() - start_time))