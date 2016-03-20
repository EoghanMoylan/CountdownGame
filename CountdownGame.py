words = open("wordlist.txt", "r")
original = "education"
annagrams = []
     
other = set(original.rstrip())
print(other)
	
for word in words:
	word = word.rstrip()
	if len(word) == len(original):
		if other == set(word):
			annagrams.append(word)
		
for annagram in annagrams:
	print(annagram)