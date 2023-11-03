
#High order functions concepts

'''
# passing functions as arg in other functions
def sum(n, func):
	total = 0
	for num in range(1, n+1):
		total += func(num)
	return total

def square(x):
	return x*x

def cube(x):
	return x*x*x

print(sum(3,square))
print(sum(3,cube))


# nesting funcions in other functions
from random import choice

def obi(person):
	def get_quote():
		msg = choice(("Hello there ", "I have a high ground ", "I loved you "))
		return msg
	result = get_quote() + person
	return result

print(obi("Anakin"))	


# returning function from another function
#from random import choice

def make_laugh_func():
	def get_laugh():
		l = choice(("HAHAHAHAH","lol","tehehe"))
		return l 
	return get_laugh

laugh = make_laugh_func() # laugh becomes a function
print(laugh())


# function accessing outer function scope
#from random import choice

def make_laugh_at_func(person):
	def get_laugh():
		laugh = choice(("HAHAHAHAH","lol","tehehe"))
		return f"{laugh} {person}" 
	return get_laugh

laugh_at = make_laugh_at_func("Joe")
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
'''



# Decorators 
'''
# Decorator as function
def be_polite(fn):
	def wrapper():
		print("What a pleasure to meet you!")
		fn()
		print("Have a nice day!")
	return wrapper

def greet():
	print("My name is Paweł.")

greet()
greet = be_polite(greet) # decorating function
greet()

# There is no need to set:
# greet = be_polite(greet)
@be_polite
def greet():
	print("My name is Paweł.")

greet()
'''


'''
# Functions with different signatures
def shout(fn):
	# def wrapper(name): # will work only with 1 argument
	def wrapper(*args, **kwargs):
		return fn(*args, **kwargs).upper()
	return wrapper

@shout
def greet(name):
	return f"Hi, I'm {name}."

@shout
def order(main,side):
	return f"Hi, I'd like the {main} with a side of {side}, please."

@shout
def lol():
	return "lol"

print(greet("todd"))
print(order("meat","salad"))
print(lol())


# saving metadata using wraps
from functools import wraps
def log_function_data(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		"""Wrapper function"""
		print(f"you are about to call {fn.__name__}")
		print(f"Here's the documentation: {fn.__doc__}")
		return fn(*args, **kwargs)
	return wrapper

@log_function_data
def add(x,y):
	"""Ads two numbers togheter."""
	return x + y

print(add.__doc__)
print(add.__name__)
help(add)
'''

'''
# Speed test decorator
from time import time

def speed_test(fn):
	def wrapper(*args, **kwargs):
		start_time = time()
		result = fn(*args, **kwargs)
		end_time = time()
		print(f"Executing {fn.__name__}")
		print(f"Time Elapsed: {end_time - start_time}")
		return result
	return wrapper

@speed_test
def sum_nums_gen():
	return sum(x for x in range(100000000))

@speed_test
def sum_nums_list():
	return sum([x for x in range(100000000)])

print(sum_nums_gen())
print(sum_nums_list())
'''


'''
# another example of decorator
from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Here are the args:",args)
        print(f"Here are the kwargs:",kwargs)
    return wrapper
	    
@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3,a="hi",b="bye")
'''



# preventing using some args decorator
from functools import wraps

def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
        	raise ValueError("No kwargs allowed!")
        return fn(*args,**kwargs)
    return wrapper
	    
@ensure_no_kwargs
def greet(name):
    print(f"hi there's {name}")

greet("Tony")
greet(name="Tony")


# Examples
'''
from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return [fn(*args,**kwargs),fn(*args,**kwargs)]
    return wrapper
    
@double_return 
def add(x, y):
    return x + y
    
print(add(1, 2)) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

print(greet("Colt")) # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''

'''
rom functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) >= 3:
        	return "Too many arguments!" 
        return fn(*args,**kwargs)
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

print(add_all()) # 0
print(add_all(1)) # 1
print(add_all(1,2)) # 3
print(add_all(1,2,3)) # "Too many arguments!"
print(add_all(1,2,3,4,5,6)) # "Too many arguments!"
'''


'''
from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if any([type(arg) is not int for arg in args]):
        	return "Please only invoke with integers." 
        return fn(*args,**kwargs)
    return wrapper
    
@only_ints 
def add(x, y):
    return x + y
    
print(add(1, 2)) # 3
print(add("1", "2")) # "Please only invoke with integers."
'''


'''
from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
        	return "Shh! Don't tell anybody!" 
        return "Unauthorized"
    return wrapper
    
@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

print(show_secrets(role="admin")) # "Shh! Don't tell anybody!"
print(show_secrets(role="nobody")) # "Unauthorized"
print(show_secrets(a="b")) # "Unauthorized"
'''


# decorator with argument
from functools import wraps

def ensure_first_arg_is(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] != val:
				return f"First arg needs to be {val}"
			return fn(*args, **kwargs)
		return wrapper
	return inner


@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)

print(fav_foods("burrito", "ice cream")) # ('burrito', 'ice cream')
print(fav_foods("ice cream", "burrito")) # 'Invalid! First argument must be burrito'

@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2

print(add_to_ten(10, 12)) # 12
print(add_to_ten(1, 2)) # 'Invalid! First argument must be 10'



'''
def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #convert args into something mutable   
            newargs = []        
            for (a, t) in zip(args, types):
               newargs.append( t(a)) #feel free to have more elaborated convertion
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

@enforce(float, float)
def divide(a,b):
	print(a/b)
# repeat_msg("hello", '5')
divide('1', '4')
'''