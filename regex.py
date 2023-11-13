# regex in python
import re

'''
regex cheat sheet
https://www.rexegg.com/regex-quickstart.html

testing regex with pythex
https://pythex.org/
'''

# define a mobile phone number regex
pattern = re.compile(r'\+48 \d{3} \d{3} \d{3}')

# search a string with regex
res = pattern.search('Call me at +48 222 333 444.')
# print(res)
# print(res.group())
res2 = pattern.findall('Call me at +48 222 333 444 or +48 111 555 666.')
# print(res2)
# print(re.search(r'\+48 \d{3} \d{3} \d{3}', "Call me at +48 222 333 444.").group())



# Some simple functions using regex

# import re

def extract_phone(input):
	phone_regex = re.compile(r'\B\+48 \d{3} \d{3} \d{3}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	return None


# print(extract_phone("my number is +48 111 222 333."))
# print(extract_phone("my number is +48 111 222 3336464644."))
# print(extract_phone("sdhsdfh+48 111 222 333"))
# print(extract_phone("+48 111 222 333"))

def extract_all_phone(input):
	phone_regex = re.compile(r'\B\+48 \d{3} \d{3} \d{3}\b')
	return phone_regex.findall(input)

# print(extract_all_phone("my number is +48 111 222 333 or +48 111 222 3336464644."))

def is_valid_phone(input):
	phone_regex = re.compile(r'^\+48 \d{3} \d{3} \d{3}$')
	match = phone_regex.search(input)
	if match:
		return True
	return False

# print(is_valid_phone("+48 111 222 333"))
# print(is_valid_phone("+48 111222333"))
# print(is_valid_phone("+48 111 222 333fgdg"))
# print(is_valid_phone("kkk +48 111 222 333 sdgsg"))



def is_valid_time(input):
    time_regex = re.compile(r'^\d{1,2}:\d{2}$')
    match = time_regex.search(input)
    if match:
        return True
    return False


# print(is_valid_time("10:45"))       #True
# print(is_valid_time("1:23"))        #True
# print(is_valid_time("10.45"))       #False
# print(is_valid_time("1999"))        #False
# print(is_valid_time("145:23"))      #False

# print(is_valid_time("it is 12:15")) #False
# print(is_valid_time("12:15"))       #True

# print(is_valid_time("34:55")) #True




def parse_bytes(input):
    bytes_regex = re.compile(r'\b\d{8}\b')
    return bytes_regex.findall(input)
	
# print(parse_bytes("11010101 101 323"))    # ['11010101']
# print(parse_bytes("my data is: 10101010 11100010"))    # ['10101010', '11100010']
# print(parse_bytes("asdsa"))   # []



# url regex
url_regex = re.compile(r'(https?)://(www\.[A-za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
match = url_regex.search("https://www.my-website.com/bio?data=blah&dog=yes")

# print(f"Protocol: {match.group(1)}")
# print(f"Domain: {match.group(2)}")
# print(f"Everything Else: {match.group(3)}")
# print(match.groups())
# print(match.group())


# group labels
def parse_name(input):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	matches = name_regex.search(input)
	print(matches.group())
	print(matches.group('first'))
	print(matches.group('last'))

# parse_name("Mrs. Tilda Swinton")



def parse_date(input):
    date_regex = re.compile(r'^(?P<d>\d\d)(\.|\,|\/)(?P<m>\d\d)(\.|\,|\/)(?P<y>\d{4})$')
    matches = date_regex.search(input)
    if matches:
        return {
            'd' : matches.group('d'),
            'm' : matches.group('m'),
            'y' : matches.group('y')
        }


# print(parse_date("01/22/1999")) # {'d': '01', 'm': '22', 'y': '1999'}
# print(parse_date("12,04,2003"))  #{'d': '12', 'm': '04', 'y': '2003'}
# print(parse_date("12.11.2003"))  #{'d': '12', 'm': '11', 'y': '2003'}
# print(parse_date("12.11.200312")) #None



# Flags

# Without Verbose Flag...
# pat = re.compile(r'^([a-z0-9_\.-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')

# With Verbose Flag...
pattern = re.compile(r"""
	^([a-z0-9_\.-]+)	#first part of email	
	@					#single @ sign
	([0-9a-z\.-]+)		#email provider
	\.					#single period
	([a-z\.]{2,6})$		#com, org, net, etc.
""", re.X | re.I)

match = pattern.search("ThomaS123@Yahoo.com")
# print(match.group())
# print(match.groups())

match2 = pattern.search("thomas123@yahoo.com")
# print(match2.group())
# print(match2.groups())


# text substitution
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
result = pattern.sub("\g<1> \g<2>", text)
# print(result)

def censor(input):
    pattern = re.compile(r'(frack|Frack)([a-z]+)?', re.I)
    return pattern.sub("CENSORED", input)

# print(censor("Frack you"))                #"CENSORED you"
# print(censor("I hope you fracking die"))  #"I hope you CENSORED die"
# print(censor("you fracking Frack"))       #"You CENSORED CENSORED"



# another text substitution example
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]
titles.sort()
fixed_titles = []

pattern = re.compile(r'(?P<title>^[\w ]+) \((?P<date>\d{4})\)')
for book in titles:
    result = pattern.sub("\g<date> - \g<title>", book)
    fixed_titles.append(result)

fixed_titles.sort()
print(fixed_titles)