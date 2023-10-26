'''
import module as mo
mo.method()
or
from module import method
method()
'''


import keyword as kw
def contains_keyword(*args):
    return any([kw.iskeyword(arg) for arg in args])
    
print(contains_keyword("hello", "goodbye")) #False
print(contains_keyword("def", "haha", "lol", "chicken", "alaska")) #True
print(contains_keyword("four", "for", "if")) #True
print(contains_keyword("blah", "doggo", "crab", "anchor")) #False
print(contains_keyword("grizzly", "ignore", "return", "False")) #True


#py -m pip install package #to install external package


#Example
from pyfiglet import figlet_format
from colorama import init 
from termcolor import colored
 
# use colorama to make termcolor work on Windows too
init()
print(colored('Hello, World!', 'green', 'on_red'))


def print_acii_art(msg, color):
    if color not in ("red", "green", "yellow", "blue", "magenta", "cyan", "white"):
        color = input("Sorry, you have to choose one of these: \n red/green/yellow/blue/magenta/cyan/white ")
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)

msg = input("What do you like to print? ")
color = input("What color? ")
print_acii_art(msg, color)


#autopep8 --in-place ugly_code.py #to clean up the code