words = open("wordlist.txt", "r")
original = "fantastic"
annagrams = []
     
other = set(original.rstrip())
print(other)
	
for word in words:
	word = word.rstrip()
	if (len(word)) < len(original):
		if len(other.intersection(set(word))) > 0:
			annagrams.append(word)
		
for annagram in annagrams:
	print(annagram)