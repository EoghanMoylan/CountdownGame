import time
from random import randint
start_time = time.time()
words = open("wordlist.txt", "r")
#original = "eductaion"
annagrams = []
cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vowels = ['a','i','o','u','e','y']

		 	
def compare(l1, l2):
	isValid = True
	for letter in l1:
		if letter in l2:
			l2.remove(letter)
		elif len(l2)<=0:
			isValid = True
		else:
			isValid = False
	return isValid

def checkValid(string):
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
		return 

def generateWord():
	finished = False
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
	other = generateWord()
	mainOne.bestWord = ""
	for word in words:
		word = word.rstrip()
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