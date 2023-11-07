# FILE IO

# story.txt
'''
This is a very short story,
here it begins
and here it ends.
 
'''

f = open("story.txt")
print(f.read()) # 'This is a very short story \n here it begins \n and here it ends.'
print(f.read()) # ''
# second read() shows nothing because cursor went to the end of file

f.seek(0) # moves cursor to the begining
print(f.read()) # 'This is a very short story\n...'

f.seek(10) # moves cursor to the begining
print(f.read()) # 'very short story\n...'

f.seek(0) # moves cursor to the begining
print(f.readline()) # 'This is a very short story\n'
print(f.readline()) # 'here it begins\n'
print(f.readline()) # 'and here it ends.\n'
print(f.readline()) # ''

f.seek(0) # moves cursor to the begining
print(f.readlines()) # returns a list of lines

print(f.closed) # False
f.close()
print(f.closed) # True

# with blocks
with open("story.txt") as f:
	f.read()

print(f.closed) # True

# "w" completly overwrites the old file
# also it creates a new file if it doesn't exist
with open("three_lines.txt", "w") as f:
	f.write("First line\n")
	f.write("Second line\n")
	f.write("Third line\n")

# "a" add things after older part
with open("three_lines.txt", "a") as f:
	f.write("Fourth line :o\n")

# "r+" allows to manipulate cursor position
with open("three_lines.txt", "r+") as f:
	f.seek(5)
	f.write(" r+ ")	# "First r+ e...""

# Examples

def copy(old,new):
    with open(old) as old:
        content = old.read()
    with open(new, "w") as new:
        new.write(content)

'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy_and_reverse(old,new):
    with open(old) as old:
        content = old.read()
        content = content[::-1]
    with open(new, "w") as new:
        new.write(content)

'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''



def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }

'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''


def find_and_replace(file, old, new):
    with open(file, "r+") as f:
        text = f.read()
        new_text = text.replace(old, new)
        f.seek(0)
        f.write(new_text)
        f.truncate()

'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''  