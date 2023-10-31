'''
#iterator or iterable
iterable1 = "word" #iterable
iterator1 = iter(iterable1) # iterator 
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
#print(next(iterator1)) #should return an error

#Custom for loop with iterator
def my_for(iterable,function):
	iterator = iter(iterable)
	while True:
		try:
			i = next(iterator)
		except:	
			break
		else:
			function(i)


def square(x):
	print(x*x)

my_for("hello",print)
my_for([1,2,3,6,8,223],square)
'''



'''
#Custom class with iterator
class Counter:
		def __init__(self,low,high):
			self.current = low
			self.high = high

		def __iter__(self):
			return self

		def __next__(self):
			if self.current < self.high:
				num = self.current
				self.current += 1
				return num
			raise StopIteration


c = Counter(50,70)
for x in c:
	print(x)
'''


#Generators are iterators
#uses yield instead of return

def count_up_to(max):
	count = 1
	while count <= max:
		yield count
		count += 1

def week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        yield day
        
'''
days = week()
print(next(days)) # 'Monday'
print(next(days)) # 'Tuesday'
print(next(days)) # 'Wednesday'
print(next(days)) # 'Thursday'
print(next(days)) # 'Friday'
print(next(days)) # 'Saturday'
print(next(days)) # 'Sunday'
#next(days) # StopIteration

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"


gen = yes_or_no()
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
print(next(gen)) # 'yes'
print(next(gen)) # 'no'


def current_beat():
	nums = (1,2,3,4)
	x = 0
	while True:
		yield nums[x]
		x += 1
		if x >= len(nums): x = 0

beat = current_beat()
print(next(beat)) # 1
print(next(beat)) # 2
print(next(beat)) # 3
print(next(beat)) # 4
print(next(beat)) # 1
print(next(beat)) # 2
print(next(beat)) # 3
print(next(beat)) # 4
'''



'''
def make_song(amount=99,word="soda"):
    nums = [x for x in range(2,amount+1)]
    nums.reverse()
    for num in nums:
    	yield f"{num} bottles of {word} on the wall."
    yield f"Only 1 bottle of {word} left!"
    yield f"No more {word}!"


default_song = make_song(5, "kombucha")
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song))
print(next(default_song)) 

default_song = make_song()
print(next(default_song)) # '99 bottles of soda on the wall.'
'''


'''
def get_multiples(num=1,count=10):
    x = 1 
    while x <= count:
        yield num*x
        x += 1

evens = get_multiples(2, 3)
print(next(evens)) # 2
print(next(evens)) # 4
print(next(evens)) # 6
#print(next(evens)) # StopIteration

default_multiples = get_multiples()
print(list(default_multiples)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_unlimited_multiples(num=1):
    x = 1 
    while True:
        yield num*x
        x += 1

sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)]) 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
print([next(ones) for i in range(20)])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''


'''
#Generator expressions - like comprehensions for lists

def nums():
	for num in range(1,10):
		yield num
g = nums()

#generator expression:
g = (num for num in range(1,10))

#function using list
sum([num for num in range(1,10)])

#function using generator
sum(num for num in range(1,10))
'''



import time
gen_start_time = time.time()
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time

print(f"sum with generator took: {gen_time}")
print(f"sum with list took: {list_time}")
print(f"generator was {(list_time-gen_time)/list_time*100}% faster then list")