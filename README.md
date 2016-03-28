### Eoghan Moylan
#### G00298939

# Countdown Letters Game Solver
This gist was created for my Theory Of Algorithms project. This README is just a copy of the Gist that can be found [here](https://gist.github.com/EoghanMoylan/0575315938261d73b1e7). The purpose of the project is to create a Python script that will solve the Countdown Letters Game. 

## Background
The idea of this algorithm is to convert a dictionary into a list, then convert each string in that list into a list of characters. It then generates a list of letters that will act as the letters on the board, and then compare both lists. Originally sets were used, however sets do not allow for duplicate values. 
````Python
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
```
##Letters on The Board
The list created for the *letters on the board* adhere to rules of the countdown letters game. Namely that there must be at least three vowels and at least four consonants. The script randomly generates a number, either one or zero. This will determine whether the next letter is a vowel or consonant. Then, depending on the outcome of the first number generated, the script will generate another random number to determine the letter itself. If the outcome does not meet the requirements, the code will run again until it does. The following code snippet shows the programming behind this. 
````python
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
```
The ```def checkValid()```looks like this:
```python
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
```
## Words list
In order to make my list of words as extensive as possible, I created a script that would compile a number of smaller word lists into one large dictionary. The script also excludes words that are over nine characters long. The current word list stands at over 75,000 (was 120,000 prior to the removal of words greater than nine letters in length) words. It is too large to list here and can be found [here] (https://github.com/EoghanMoylan/CountdownGame) as well as the scripts created for this project.

## Main Def
The ```python def mainOne()``` calls the other functions in the script. This function also keeps track of the longest valid word that has occured. From here, the list of words is converted into a list of letters in order to be compared to the list of letters in the board. The words here are also stripped of their newline characters in order to ensure that the length is calculated correctly. 
```python
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
```

## Preprocessing
The script begins by parsing a deictionary file named "wordlist.txt" into a list. It begins the time.time module and then populates two lists of letters, one full of consonants, the other, vowels. 

## Efficiency
Using the Time.time to test the running time of the script, the average execution time is roughly 0.8 - 1.0 seconds. This is well within the bounds of Countdown's 30 second time limit. This time is skewed as a result of processes running simultaneously to the script, as well as the machine, itself and is not entirely representative of the algorithms runtime. When tested with the Timeit module the results were significantly lower, averaging around 0.04 - 0.5 seconds.  

## Results
The algorithm results in the best solution to the countdown letters game being found, and runs at an acceptable rate. The dictionarycons.py script compiles multiple wordlist files into one meaning the list of words used is always extensive and can be easily updated.


## References
These are references for both scripts and word lists used: 

[Time](http://stackoverflow.com/questions/1557571/how-to-get-time-of-a-python-program-execution)

[New Line](http://stackoverflow.com/questions/275018/how-can-i-remove-chomp-a-newline-in-python)

[Random Numbers](http://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9)

[File Reading](https://docs.python.org/2/tutorial/inputoutput.html)

[Dictionary](https://raw.githubusercontent.com/ConfuddledPenguin/Countdown/master/dictionary.txt)
