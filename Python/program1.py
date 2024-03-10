'''a=list(input("Enter the values"))
a_list=[]
for  i in range(a):
    ele=int(input(f"enter element{i+1}:"))
    print(ele)'''
    
#wap to create a list and ask user to enter int.without using for loop
    
'''li=list(eval(input('enter the values seperated by comma')))'''

                   
#wap to create dict winners with the usernames of 5 players with their total co
'''players=5
win={}
for i in range(5):
    name=input(f"enter the name for player{i+1}")
    matches_won=int(input(f"enter the matches won by {name}"))
    win[name]=matches_won
    print(win)'''
#break continue
'''for i in range(1,11):
    if(i==7):
        break
    else:
        print(i)
print("outside")'''
#control
'''for i in range(1,11):
    if(i==7):
        continue
    else:
        print(i)
print("continue")'''
#even elements in list
'''li=list(eval(input("enter the elment sepeated by comma")))
even_list=[]
for i in li:
    if(i%2==0):
        even_list.append(i)
print(li)
print(even_list)'''
  #reverse order of list
'''li=list(eval(input("enter the values")))
rev_li=[]
for i in range(len(li)-1,-1,-1):
    rev_li.append(li[i])
print(rev_li)'''
#square list
'''li=list(eval(input("enter the values")))
sq_li=[]
for i in li:
    sq_li.append(i**2)
print(li)
print(sq_li)'''
#display list whose names starts with A
li=list(eval(input("enter the values")))
A_li=[]
for i in li:
    if(i[0]=='A'):
        A_li.append(i)
print(A_li)
   
        
