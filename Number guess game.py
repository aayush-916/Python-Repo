import random as rn
import time 

def game(l):
	a = rn.randint(1,l)
	for i in range(1,7):
		if i == 6:
			print('  ')
			print('This is your last chance \n do you want Hints ')
			h = int(input('1.Yes / 2.No  :   '))
			if h == 1:
				if a % 2 == 0:
					print('The no. is closes to....',a-1)
				else:
					print('The no. is closes to....',a+1)
		b = int(input("Enter Number :   "))
		if b > a:
			print('Your number is Greater ')
		if b < a:
        
			print('Your number is Lower  ')
		if b == a:
			print("You win .....")
			break
	else:
		print('     ')
		print('You lost the game........')
		print(' ')
		print('The no. is........',a)
#Mr_Aayush
def cho():
	ch = int(input("Choose your level:  \n \n 1.Easy \n 2.Medium \n 3.Hard \n  :     "))
	if ch == 1:
		print('guess a number between 1 to 50 ')
		game(50)
	elif ch == 2:
		print('guess a number between 1 to 100 ')
		game(100)
	elif ch == 3:
		print('guess a number between 1 to 200')
		game(200)
	else:#Mr_Ayush
		print('Invalid input.....')
		cho()
	print('  ')
	print('  ')
	print('Do you want to play again...')
	aa = input('1.Yes \n 2.No :   ')
	if aa == '1':#Aayush
		cho()
	else:
		print('Thank you ')
cho()
