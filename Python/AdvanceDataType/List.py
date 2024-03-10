a=[10,20,30,40]
print(a)
[10, 20, 30, 40]
a=[10,20,30,40]
a=[10,20,'man',2+3j]
print(a)
[10, 20, 'man', (2+3j)]
#append
a.append(60)
print(a)
[10, 20, 'man', (2+3j), 60]
#remove
a.remove(60)
a.remove()
#pop
a.pop()
print(type(c))
l=list["hello"]
#concate with out +
n1.extend(n2)
print(n1)
[10, 20, 30, 40]
#insert at Specfic Index value
n1.insert(0,'mike')
print(n1)
['mike', 10, 20, 30, 40]
#replace at Specfic Index
n1[0]='jake'
print(n1)
['jake', 10, 20, 30, 40]
#find index value
print(n1.index('jake'))
0
#shallow copy or duplicate copy
a=[10,20,30,40,50]
b=a
print(b)
[10, 20, 30, 40, 50]
b.append(500)
print(a)
[10, 20, 30, 40, 50, 500]
#deep copy or orginal copy
a1=list(a)
print(a1)
[10, 20, 30, 40, 50, 500]
a1.append(60)
print(a)
[10, 20, 30, 40, 50, 500]
print(a1)
[10, 20, 30, 40, 50, 500, 60]


age=[22,22,34,54,22,34,23,45]
#count the number
print(age.count(22))
3
print(age.reverse())
None
age.reverse()
print(age)
[22, 22, 34, 54, 22, 34, 23, 45]
#reverse items
age.reverse()
print(age)
[45, 23, 34, 22, 54, 34, 22, 22]
#sort default is ascendenring order
age.sort()
print(age)
[22, 22, 22, 23, 34, 34, 45, 54]
#sort in decensing order not create seperate list changes happen in original data
age.sort(reverse=True)
print(age)
[54, 45, 34, 34, 23, 22, 22, 22]
#sort in different list
sorted_age=sorted(age)
print(sorted_age)
[22, 22, 22, 23, 34, 34, 45, 54]
#tuples
tup=(10,20,30,40)
print(tup)
(10, 20, 30, 40)
#tuple cont modify
tup.append(20)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    tup.append(20)
AttributeError: 'tuple' object has no attribute 'append'
tup.pop(2)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    tup.pop(2)
AttributeError: 'tuple' object has no attribute 'pop'
tup.clear()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    tup.clear()
AttributeError: 'tuple' object has no attribute 'clear'

# we can modify by converting to list
modify=list(tup)
print(modify)
[10, 20, 30, 40]
modify.append(300)
print(modify)
[10, 20, 30, 40, 300]
tup=tuple(modify)
print(tup)
(10, 20, 30, 40, 300)





