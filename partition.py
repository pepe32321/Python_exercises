'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''

def partition(a,fn):
    truthy_list=[]
    falsy_list=[]
    for i in range(0,len(a)):
        if fn(a[i]):
            truthy_list.append(a[i])
        else:
            falsy_list.append(a[i])
    return [truthy_list,falsy_list]