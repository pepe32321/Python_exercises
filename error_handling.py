'''
Common Errors:

SyntaxError - incorrect syntax
NameError - variable is not defined, hasn't be assigned
TypeError - mismatch of data type
IndexError - trying to use element with invalid index
ValueError - right type but incorret value
KeyError - trying to use invalid key
AttributeError - trying to use invalid attribute
'''

#Raising own exceptions
#raise ValueError('invalid value')

def colorize(text, color):
	colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
	if type(text) is not str:
		raise TypeError("text must be instance of str")
	if type(color) is not str:
		raise TypeError("color must be instance of str")
	if type(text) not in colors:
		raise ValueError("color is invalid")
	print(f"Printed {text} in {color}")

#colorize('hello', 'red')
#colorize(22, 'red')

#Handling Errors

#try - code is continued after error
try:
	fhdfhdhfd
except:
	print('Problem!')
print('after the try')


def get(d,key):
	try:
		d[key]
	except KeyError:
		return None

d = {"name":"Ricky"}
d["name"]
print(get(d,"city"))


#try, except, else, finally
while True:
	try:
		num = int(input("Please enter a number: "))
	except ValueError:
		print("That is not a number!") #Except runs if error in try
	else:
		print("Nice!") #Else runs if no error in try
		break
	finally:
		print("End of try") #Finally runs anyway
print("After the loop")


def divide(a,b):
	try:
		result = a/b 
	except ZeroDivisionError as err:
		print("Please, don't divide by 0")
		print(err)
	except TypeError as err:
		print("Please, input only ints or floats")
		print(err)
	else:
		print(result)

print(divide('a',2))
print(divide(5,0))
print(divide(5,2))

'''
#debugging with pdb
import pdb 
pdb.set_trace() #put this right before error
#import pdb; pdb.set_trace() - optional in one line

#pdb commands:
l #(list) - shows where am I in code
n #(next line)
p #(print) - to print variable which inflict with pdb syntax
c #(continue - finishes debugging)
'''















