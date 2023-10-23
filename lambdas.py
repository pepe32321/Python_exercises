def square(num): return num ** 2
print(square(7))

square2 = lambda num: num ** 2
print(square2(7))

add = lambda a,b: a+b
print(add(3,2))


#lambda is for temporary para-function(single line, no name)
'''
button = tk.Button(frame,
					text="Click me",
					fg="red",
					command=lambda: print("Hello"))
'''

# map to iterate lambda through the elements of object
def decrement_list (l): 
    return list(map(lambda num: num-1, l))
print(decrement_list([1,2,3]))

# filter to extract elements on true check 
l = [1,2,3,4]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)

def remove_negatives(l):
    return list(filter(lambda x: x >= 0,l))

print(remove_negatives([-7,0,1,2,3,4,5]))

