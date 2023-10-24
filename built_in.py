#all - check if all elements are truth and returns bolean
people = ["Charlie", "Casey", "Cody"]
print(all([name[0] == "C" for name in people]))


#any - check if any elements is truth and returns bolean
nums = [1,2,3]
print(any([num % 2 == 0 for num in nums]))


def is_all_strings(l):
    return all([type(el) is str for el in l])

print(is_all_strings(["krkr", "wfwgfwegf"]))
print(is_all_strings(["krkr", 2]))


#sorted sorts only result, doesn't change object 
nums = [1,55,22,-5]
print(sorted(nums))
print(nums)


#max/min returns max/min value
names = ['Kaja','Iza','Paweł']
print(max(names, key = lambda n: len(n)))


def extremes(l):
    return (min(l),max(l))
    
print(extremes([1,2,3,4,5]))
print(extremes((99,25,30,-7)))
print(extremes("alcatraz"))


#reversed return reversed iterator without changing original
nums=[1,2,3]
print(reversed(nums))
print(nums)


#math functions
print(abs(-23))
print(sum([4,3]))
print(sum([1,2,3],10))
print(round(10.3))
print(round(3.51234,2))


def max_magnitude(l):
    return max([abs(num) for num in l])
    
print(max_magnitude([300,20,-900]))


def sum_floats(*args):
    return sum([arg for arg in args if isinstance(arg, float)])

print(sum_floats(1.5, 2.4, 'awesome', [], 1)) # 3.9
print(sum_floats(1,2,3,4,5)) # 0


#zip agregates elements with the same index in tuples
midterms = [80,91,78] 
finals = [98,89,53] 
students = ['dan','ang','kate'] 
print([x for x in zip(students,midterms,finals)])


final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms,finals)
            )
        )
    )
print(final_grades)


def sum_even_values(*nums):
    return sum([num for num in nums if num % 2 == 0])

print(sum_even_values(1,2,3,4,5,6)) # 12
print(sum_even_values(4,2,1,10)) # 16
print(sum_even_values(1)) # 0


def interleave(a,b):
    return ''.join([''.join(x) for x in zip(a,b)])

print(interleave('hi','ha'))    # 'hhia'
print(interleave('aaa', 'zzz'))  # 'azazaz'
print(interleave('lzr','iad')) #  'lizard'


def triple_and_filter(l):
    return [x*3 for x in l if x % 4 == 0]
    
print(triple_and_filter([1,2,3,4])) # [12]
print(triple_and_filter([6,8,10,12])) # [24,36]


def extract_full_name(l):
    return [" ".join(el.values()) for el in l]
    
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']