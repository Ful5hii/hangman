import replit
import sys
import random
def checkOne(words):
	if len(words) == 1:
		answer = input("Is your word '" + words[0] + "'?")
		if answer == 'y':
			print("Yay!!")
			sys.exit()
		else:
			print("Okay")
	elif len(words) == 0:
		print("Your word doesn't exist!!")
		sys.exit()

def checkRandom(x):
	
	while True:
		answer = input("Is your word '" + random.choice(x) + "' [y/n]")
		if answer == 'y':
			print("Yay!!")
			sys.exit()
		else:
			print("Okay")

word_file = open('words.txt','r')
words = word_file.read().split('\n')
words = set(list(map(lambda x:x.lower(), words)))
words_test = words

print("I will guess any English word with less than 10 tries.\n\n\n\n")
print(len(words))
length = int(input("What is the length of your word (includes dashes, periods, etc.) >>> "))
words = list(filter(lambda x:(len(x) == length),words))
replit.clear()
checkOne(words)

letters = []
lettersUsed = []

print(len(words))
while len(letters) < length:
	word = random.choice(words)
	letter = random.choice(word)
	if letter not in letters:
		ans = input("Does your word contain letter " + letter.upper() + "[y/n] >>> ")
		if ans == "y":
			words = list(filter(lambda x:(letter in x),words))
			letters.append(letter)
		elif ans == "n":
			words = list(filter(lambda x:(letter not in x),words))
		lettersUsed.append(letter)
		print(len(words))
		if len(words) < 10:
			break
checkOne(words)


guess = []
com = []
for y in range(len(words)):
	com.append(words[y][0])
com = set(com)
for x in com:
	ans = input("Is the first letter of your word " + x.upper() + "? [y/n] >>> ")
	if ans == 'y':
		words = list(filter(lambda y:(x == y[0]),words))
		checkOne(words)
		checkRandom(words)
		break

#supercalifragilisticexpialidocius
