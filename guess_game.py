from random import randint

replay = "y"
while replay != "n":
	random_number = randint(1,100)
	guess = int(input("Geuss the number between 1 and 100 "))
	while guess != random_number:
		if guess > random_number:
			guess = int(input("Too high! Try again "))
		else:
			guess = int(input("Too low! Try again "))
	print(f"Yes, the number is {guess} ")
	replay = input("Play again? (y/n) ")
print("game over!")