from pyfiglet import figlet_format
from colorama import init 
from termcolor import colored

import requests
from random import choice

init()
start_phrase = colored(figlet_format("DAD300!!!"), color="red")
print(start_phrase)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(
	url, 
	headers={"Accept":"application/json"},
	params={"term":user_input}
).json()

amount_jokes = response["total_jokes"]

if amount_jokes > 1:
	print(f"There are {amount_jokes} of jokes with {user_input}! ") #check cat
	print("Here is a random one: ")
	print(choice(response["results"])['joke']) 
elif amount_jokes == 1:
	print("There is one joke!") #check "monastery"
	print(response["results"][0]['joke']) 
else:
	print(f"There no jokes with {user_input}, sorry! ") #check rhhfdhdfhdfh


