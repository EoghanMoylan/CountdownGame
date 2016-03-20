words = open("wordlist.txt", "r")
original = "education"
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

for word in words:
	word = word.rstrip()
	if len(word) <= len(original):
		if compare(other, list(word)) == True:
			annagrams.append(word)
		
for annagram in annagrams:
	print(annagram)