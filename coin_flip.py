from random import random

def flip_coin():
	if random()>0.5:
		return "Orzeł"
	else:
		return "Reszka"
print (flip_coin())