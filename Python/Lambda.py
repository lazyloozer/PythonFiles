'''#filter
li=[1,2,3,4]
even=list(filter((lambda ele:ele%2==0),li))
print(even)
#map
sq=list(map((lambda ele:ele**2),li))
print(sq)
#reduce
from functools import *
res=reduce((lambda a,b:a*b),li)
print(res)'''
#Decorators:
def decor(function):
    def inner(name):
        if name=='Ankit':
            print(name,'likes Pulao')
        else:
            function(name)
    return inner

@decor
def food(name):
    print(name,'likes Biryani')
food('Ayush')
food('ankit')
food('Nikitha')
           
