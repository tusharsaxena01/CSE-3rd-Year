'''
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...
Until the user guesses the number.
'''
import random

def quitmsg():
	print("\nThank You For Playing!")
	print("\n<-------------------------- Created By Abhi Saxena -------------------------->")

def game(num):
	cowbull = [0,0]
	guess = input("Enter Your Guess: ")
	if guess in "exitEXIT":
		return "exit"
	
	for i in range(len(guess)):
		if guess[i]==num[i]:
			cowbull[1]+=1
		elif guess[i] == num[0] or guess[i] == num[1] or guess[i] == num[2] or guess[i] == num[3]:
			cowbull[0]+=1
	#Cheat_code
	if guess=="01":
		print(num)
	return cowbull

if __name__ == '__main__':
	print("<========= Explaination =========>")
	print("\nLet's play a game of Cowbull!")
	print("\nI will generate a number")
	print("\nand you have to guess the numbers one digit at a time.")
	print("\nFor every number in the wrong place, you get a cow.")
	print("\nFor every one in the right place, you get a bull.")
	print("\nThe game ends when you get 4 bulls!")
	print("\nType exit at any prompt to exit.")
	print("\n<-------------------------- Cow and Bull Game -------------------------->")
	op = input("Play The Game? (Y/N)\n> ")
	times=0
	num = str(random.randint(1000,9999))
	if op == "y" or op == "Y":
		playing=True
	elif op=="N" or op == "n":
		quitmsg()
		playing=False
	else:
		print("Invalid Choice! Exiting The Game...")
		quitmsg()
	while playing:
		times+=1
		cb_count = game(num)
		if cb_count==[0,4]:
			print("Correct!\nYou have Cows=",cb_count[0],"and Bulls=",cb_count[1],"In",times,"Times.")
			quitmsg()
			break
		elif cb_count == "exit":
			quitmsg()
			break
		else:
			print("\nYou have",cb_count[0],"Cows and ",cb_count[1],"Bulls\nKeep Going...\n")
