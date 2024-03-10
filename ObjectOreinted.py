'''def extract(component):
    return[int(ele.imag)for tup in component for ele in tup if ele.img>0]
component=input()
component=eval(component)
result=extract(component)
print(result)'''
#oops
'''class demo:
    print("im first")
    def display(self):
        print("im second")'''
#
'''class student:
    def __init__(self):
        self.name='Mike'
        self.age=34
    def work(self):
        print("work")
        s1=student()
        s1.work()
        print(s1.name)'''
#
'''class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def work(self):
        print("Working")
emp1=Employee('Mike',20)
emp2=Employee('jake',40)
print(emp1.name)
print(emp2.name)
print(emp1.age)
print(emp2.age)'''
#Ex2
'''class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        def work():
            print('Working')
emp=Employee('jake',60000)
print(emp.name)'''
#Bank
'''class Bank:
    balance=5000;
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def deposite(self):
        print('Deposing')
        y=300
    def saving(self):
        print('Saving')
b1=Bank('SBI','Banglore')
b2=Bank('Kotax','BTM')
print(b1.name)
print(b1.branch)
print(b2.name)
print(b2.branch)
b1.saving()
b1.deposite()
print(b1.balance)
print(b2.balance)
print(y)'''
#example2:Method Overloading not support
'''class bank:
    def saving(self):
        print("saving method")
    def saving(self,a):
        print("Saving 1 parametr")
    def saving(self,a,b):
        print("saving a, b parameter")
b1=bank()
#b1.saving()
#b1.saving(10)
b1.saving(10,30)'''
#Constructor overloading not support
class bank:
    def __init__(self):
        print("Saving Method")
    def __init__(self,a):
        print("saving a,metod")
    def __init__(self,a,b):
        print('Saving a,b')
#b=bank()
#b=bank(10)
b=bank(10,20)

    
