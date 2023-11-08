'''
# csv with reader
from csv import reader
with open("fighters.csv") as f:
	csv_reader = reader(f)
	
#	for row in csv_reader:
#		# each row is a list
#		print(row)
	next(csv_reader) # to skip headers
	for fighter in csv_reader:
		print(f"{fighter[0]} is from {fighter[1]}")


# csv with DictReader
from csv import DictReader
with open("fighters.csv") as f:
	csv_reader = DictReader(f)
	for row in csv_reader:
		# each row is an OrderedDict
		print(row)


# reader with different delimiter
from csv import reader
with open("example.csv") as f:
	csv_reader = reader(f, delimiter="|")
	for row in csv_reader:
		# each row is a list
		print(row)


# Writing csv with lists
from csv import writer
with open("fighters2.csv", "w") as f:
	csv_writer = writer(f)
	csv_writer.writerow(["Character","Move"])
	csv_writer.writerow(["Ryu","Hadouken"])


# capitaliser

# version 1

from csv import reader
with open("fighters.csv") as f:
	csv_reader = reader(f)
	fighters = [[s.upper() for s in row] for row in csv_reader]
	for row in fighters:
		print(row)

with open("screaming_fighters.csv","w") as f:
	csv_writer = writer(f)
	for fighter in fighters:
		csv_writer.writerow(fighter)


# version 2 nested

from csv import reader, writer
with open("fighters.csv") as f:
	csv_reader = reader(f)
	with open("screaming_fighters.csv","w") as f:
		csv_writer = writer(f)
		for fighter in csv_reader:
				csv_writer.writerow([s.upper() for s in fighter])

# Writing csv with dictionaries

from csv import DictWriter, DictReader
with open("cats.csv","w") as f:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(f, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	})

def cm_to_in(cm):
	return float(cm) * 0.393701

with open("fighters.csv") as f:
	csv_reader = DictReader(f)
	fighters = list(csv_reader)

with open("inch_fighters.csv","w") as f:
	headers = ("Name","Country","Height (in inches)")
	csv_writer = DictWriter(f, fieldnames=headers)
	csv_writer.writeheader()
	for fighter in fighters:
		csv_writer.writerow({
			"Name": fighter["Name"],
			"Country": fighter["Country"],
			"Height (in inches)": cm_to_in(fighter["Height (in cm)"])
		})

# examples
from csv import DictWriter, DictReader
def add_user(first,last):
    with open("users.csv","a") as f:
	    headers = ["First Name", "Last Name"]
	    csv_writer = DictWriter(f, fieldnames=headers)
	    # csv_writer.writeheader()
	    csv_writer.writerow({
		    "First Name": first,
		    "Last Name": last
	    })


add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson



from csv import reader
def find_user(first,last):
    with open("users.csv") as f:
        csv_reader = reader(f)
        users = [row for row in csv_reader]
        if any([user == [first, last] for user in users]):
            return users.index([first, last])
        else:
            return 'Not Here not found.'


find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''


# Pickling
import pickle
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


blue = Cat("Blue", "Scottish Fold", "String")

# To pickle an object:
with open("pets.pickle", "wb") as file:
	pickle.dump(blue, file)

# To unpickle something:
# with open("pets.pickle", "rb") as file:
# 	zombie_blue = pickle.load(file)
# 	print(zombie_blue)
# 	print(zombie_blue.play())