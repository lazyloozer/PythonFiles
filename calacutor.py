choice=int(input("Enter 1-Add,2-sub,3-mu,4-div"))
num1=int(input("enter the number"))
num2=int(input("enter the number"))

if choice==1:
         print(f"{num1}+{num2}={num1+num2}")
elif choice==2:
    print(f"{num1}-{num2}={num1-num2}")
elif choice==3:
    print(f"{num1}*{num2}={num1-num2}")
elif choice==4:
    print(f"{num1}/{num2}={num1/num2}")
         
else:
     print("Invaild choice")