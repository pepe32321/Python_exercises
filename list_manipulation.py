def list_manipulation(c,a,b,d=None):
    if a=='remove':
        if b=='beginning':
            return c.pop(0)
        elif b=='end':
            return c.pop()
    elif a=='add':
        if b=='beginning':
            return c.insert(0,d)
        elif b=='end':
            return c.append(d)
    return

list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]

e=[1,2,3]
print(e.pop(0))

f=[1,2,3]
print(f.pop())

g=[1,2,3]
g.insert(1,20)
print(g)


h=[1,2,3]
print(h.append(30))
