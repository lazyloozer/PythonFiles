
'''li=[10,20,30,40]
dup_li=[i if i%2!=0 else -1 for i in li]#[-1,-1,-1,-1]
print(dup_li)
#predict the output of the folloeing code:
vowels=[char.upper() for char in "hello" if char in "aeiou"]
print(vowels)'''
#code3
'''li=[[1,2],[3,4],[5,6]]
list=[sub_ele for i in li for sub_ele in i]
#even number in sublist
list=[sub_ele for i in li for sub_ele in i if sub_ele%2==0 ]
print(list)'''
#code 2
'''number=[1,2,3,4]
even_odd=['even'if x%2==0 else'odd' for x in number]
print(even_odd)'''
#code 4
'''li=[1,2,3,-4,-5,6]
new_li=[i for i in li if i>0]
print(new_li)'''
#code 05
'''li=[(1,2),(3,4),(5,6)]
list=[sub_li for i in li for sub_li in i]
print(list)'''
#code 06
'''li=['abc123','dgf567','mno908']
list=[int(char) for i in li for char in i if char.isdigit()]
print(list)'''
#code 7 pailndrome
'''li=['python','radar','racecar','level']
reverse_li=[ for string in li if list(string)==list(reversed(list(string)))]
print(reverse_li)'''
#code 8
'''li=[1,2,3,4,5,6]
s=reversed(li)
print(s)'''
#code 9
'''color=['red','green','blue']
fruit=['apple','banana','orange']
com=[(i,j)for i in color for j in fruit]
print(com)'''
#code 10
'''com=[1+2j,3+4j,4+4j]
real=[int(i.real) for i in com]
print(real)'''
#code 11
com=[1+2j,3+4j,-4-4j,7-6j]
preal=[int(i.real) for i in com if i.real>0]
print(preal)



