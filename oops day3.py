'''class Demo1:
    def __init__(self):
        self.__name='kodnest'
    def test(self):
        print('Accessing inside',self.__name)
d1=Demo1()
d1.test()
print("private outside",d1._Demo1__name)

class Demo2(Demo1):
    def test2(self):
        print('Accessing test2 inside',d1._Demo1__name)
        print('Accessing test2 inside2',d2._Demo1__name)
d2=Demo2()
d2.test2()
print(d2._Demo1__name)'''
#Inheritance
'''class Demo1:
    def __init__(self):
        self.x=100
    def test1(self):
        print("inside method")
class demo2(Demo1):
    pass
d2=demo2()
print(d2.x)
d2.test1()'''
'''class student:
    def __init__(self):
        self.name='kodnest'
        self.id=10
    def study(self):
        print("stuyding")
class friend(student):
    pass
f1=friend()
print(f1.name)
print(f1.id)
f1.study()'''
#Hierarchial inheritance
class Demo1:
    def__init__(self):
        self.x=100;
        
