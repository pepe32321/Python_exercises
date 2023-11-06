# Assertion - statement that returns None if True and AssertionError if False

'''
def add_positive_numbers(x,y):
	assert x > 0 and y > 0, "Both numbers must be positive!"
	return x + y

print(add_positive_numbers(1, 1)) # 2
print(add_positive_numbers(1, -1)) # "Both numbers must be positive!" 
'''


'''
def eat_junk(food):
	assert food in ["pizza", "ice cream", "candy", "fried butter"], "food must be a junk food!"
	return f"NOM NOM NOM I'm eating {food}"

food = input("Enter a food, please: ")
print(eat_junk(food))
'''


# Assertion warning
# using .py with -O flag ignores assertions 
# DO NOT put important things in assertions



# Doctests
'''
def add(a,b):
	"""
	>>> add(2,3)
	5
	>>> add(100,200)
	300
	"""
	return a + b

# To run doc test:
# py -m  doctest -v testing.py 
'''
# TDD - red -> green -> refactor
'''

def double(values):
	""" double values in a list
	
	>>> double([1, 2, 3, 4])
	[2, 4, 6, 8]

	>>> double([])
	[]

	>>> double(['a', 'b', 'c'])
	['aa', 'bb', 'cc']

	>>> double([True, None])
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

	"""
	return [a + a for a in values]

'''

# doctests are not flexible with syntax
# strings must be with '' not with ""
# there must be spaces after , like [1, 2, 3] not like [1,2,3]
# there must not be any unnessessery white space

# unittest - for testing units of code
# example:

# activities.py
'''
from random import choice
def eat(food, is_healthy):
	if not isinstance(is_healthy, bool):
		raise ValueError("is_healthy must be a boolean")
	ending = "because YOLO!"
	if is_healthy:
		ending = "because my body is a temple"
	return f"I'm eating {food}, {ending}"

def nap(num_hours):
    if num_hours >= 2:
    	return f"Ugh I overslept.  I didn't mean to nap for {num_hours} hours!"
    return f"I'm feeling refreshed after my {num_hours} hour nap"

def is_funny(person):
	if person is 'tim': return False
	return True

def laugh():
	return choice(('lol', 'haha', 'tehehe'))
'''

# tests.py
# run with py tests.py -v
'''
import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
    	"""eat should have a positive message for healthy eating"""
    	self.assertEqual(
			eat("broccoli", is_healthy=True),
			"I'm eating broccoli, because my body is a temple"
    	)
    def test_eat_unhealthy(self):
    	"""eat should indicate you've given up for eating unhealthy"""
    	self.assertEqual(
			eat("pizza", is_healthy=False),
			"I'm eating pizza, because YOLO!"
    	)
    def test_eat_healthy_boolean(self):
    	"""is_healthy must be a bool"""
    	with self.assertRaises(ValueError):
    		eat("pizza", is_healthy="who cares?")

    def test_short_nap(self):
    	"""short naps should be refreshing"""
    	self.assertEqual(
    		nap(1),
    		"I'm feeling refreshed after my 1 hour nap"
    	)
    def test_long_nap(self):
    	"""long naps should be discouraging"""
    	self.assertEqual(
    		nap(3), "Ugh I overslept.  I didn't mean to nap for 3 hours!"
    	)
    def test_is_funny_tim(self):
    	self.assertEqual(is_funny("tim"), False)
    	# self.assertFalse(is_funny("tim"), "tim should not be funny")

    def test_is_funny_anyone_else(self):
    	"""anyone else but tim should be funny"""
    	self.assertTrue(is_funny("blue"), "blue should be funny")
    	self.assertTrue(is_funny("tammy"), "tammy should be funny")
    	self.assertTrue(is_funny("sven"), "sven should be funny")
    
    def test_laugh(self):
    	"""laugh returns a laughing string"""
    	self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))

if __name__ == "__main__":
    unittest.main()
'''

# Another example

'''
# robot.py
class Robot:
	def __init__(self, name, battery=100, skills=[]):
		self.name = name
		self.battery = battery
		self.skills = skills

	def charge(self):
		self.battery = 100
		return self

	def say_name(self):
		if self.battery > 0:
			self.battery -= 1
			return f"BEEP BOOP BEEP BOOP.  I AM {self.name.upper()}"
		return "Low power.  Please charge and try again"

	def learn_skill(self, new_skill, cost_to_learn):
		if self.battery >= cost_to_learn:
			self.battery -= cost_to_learn
			self.skills.append(new_skill)
			return f"WOAH. I KNOW {new_skill.upper()}"
		return "Insufficient battery. Please charge and try again"

# robot_tests.py
import unittest
from robot import Robot


class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()
'''


