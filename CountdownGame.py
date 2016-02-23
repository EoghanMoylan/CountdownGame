words = open("wordlist.txt", "r")
other = "polo"
annagrams = ["",""]
             
for word in words:
	i = 0
	if len(word) - 1 == len(other):
		for letter in other:
			if letter in word:
				i += 1
			else:
				break
	if i == len(other):
		annagrams.append(word)

for annagram in annagrams:
	print(annagram)