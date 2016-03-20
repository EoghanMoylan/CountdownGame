import time
start_time = time.time()

words = open("wordlist.txt", "r")
original = "eductaion"
annagrams = []
     
other = list(original.rstrip())			 
	
def compare(l1, l2):
	isValid = True
	for letter in l1:
		if letter in l2:
			l2.remove(letter)
			#pass
		elif len(l2)<=0:
			isValid = True
		else:
			isValid = False
	return isValid

def mainOne():
	for word in words:
		word = word.rstrip()
		if len(word) <= len(original) and len(word) >= 4:
			if compare(other, list(word)) == True:
				annagrams.append(word)
		
mainOne()

for annagram in annagrams:
	print(annagram)		 
	
print("--- %s seconds ---" % (time.time() - start_time))