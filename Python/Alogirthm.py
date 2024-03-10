#Display elememts and index values
'''li=[10,20,30,40]
for i,j in enumerate(li):
    print('index:',i,'element value:',j)'''
#display elements and index at specfic position
'''li=[10,20,30,40]
for i,j in enumerate(li,start=2):
    print('index:',i,'element value:',j)'''
#Linear Search:
'''mylist=[10,30,40,50,60,70,90]
target=60;

def linear_search(mylist,target):
    for ind,ele in enumerate(mylist):
        if ind==target:
            return ele
        return -1
result =linear_search(mylist,target)
if result==-1:
    print(f"Element:{target}  found")
else:
    print(f"Element:{target} fount at index:{result}")'''
#
'''mylist=[10,30,40,50,60,70,90]
target=60;


def linear_search(mylist,target):
    index_li=[]
    for ind,ele in enumerate(mylist):
        if ele==target:
            index_li.append(ind)
        
        return index_li
result =linear_search(mylist,target)
if result:
    print(f"Element:{target}not found")
else:
    print(f"Element:{target} fount at index:{result}")'''
#insertion using bisect
'''import bisect
mylist=[10,20,30]
item=11
ind=bisect.bisect(mylist,item)
bisect.insort(mylist,item)'''
#
dict={1:'a',2:'b',3:'c'}
for i,ele in enumerate(dict):
    print(i,ele)
        
