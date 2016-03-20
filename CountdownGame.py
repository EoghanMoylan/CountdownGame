words = open("wordlist.txt", "r")
original = "pool"
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
		if len(word) <= len(original):
			if compare(other, list(word)) == True:
				annagrams.append(word)
		
mainOne()

for annagram in annagrams:
	print(annagram)		 
			 
if __name__ == '__main__':
	import timeit
	numLoops = 100
	time = timeit.timeit("mainOne", setup="from __main__ import mainOne", number = numLoops)
	print(time)
	print(numLoops, "Loops, Average of",  time/100, "seconds per loop")