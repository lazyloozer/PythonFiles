#if-elid-else
salary=int(input("Enter the salary"))
if salary<=50000:
    tax=0.05*salary
elif salary<=60000:
    tax=0.06*salary
elif salary<=75000:
    tax=0.07*salary
else:
    tax=0.10*salary
print(f"salary is-{salary}:Tax is-{tax}")

#wapp to accept character from user and diplay whether  it vomel or concont
ch=input("enter the char").lowe()
if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("vomel")   
else:
    print(ch,"consonant")
    


    
