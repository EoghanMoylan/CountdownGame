words = open("wordlist1.txt", "r")
morewords = open("wordlist2.txt", "r")
new = open("wordlist.txt", "w")
	
for word in words:
	if not word in morewords and len(word) < 10:
		new.write(word)
		
for word in morewords:
	if not word in words and len(word) < 10:
		new.write(word)