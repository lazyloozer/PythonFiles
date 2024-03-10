#Multilevel inhertiance
'''class demo1:
    def __init__(self):
        self.x=100
    def test(self):
        print("Inside test1")

class demo2(demo1):
    def __init__(self):
        self.x=200;
    def test2(self):
        print("inside test2")
class demo3(demo2):
    pass
d3=demo3()
print(d3.x)
d3.test2()'''
#Multiple using mro
'''class demo1:
    def __init__(self):
        self.x=100;
    def test(self):
        print("inside the test1")
class demo2:
    def __init__(self):
        self.x=200;
    def test(self):
        print("inside test2")
class demo0:
     def __init__(self):
            self.x=100;
        
     def test(self):
        print("inside the test1")
    
       
        
class demo3(demo2,demo1,demo0):
    pass
d3=demo3()
print(d3.x)
d3.test()
print(d3.x)
d3.test()'''
#super without method
'''class demo1:
    def __init__(self):
        self.x=100;
class demo2(demo1):
    def __init__(self):
        self.y=200;
d2=demo2()
print(d2.y)
print(d2.x)'''

#super method
class demo1:
    def __init__(self):
        self.x=100;
class demo2(demo1):
    def __init__(self):
        self.x=200;
        super().__init__()
d2=demo2()
#print(d2.y)
print(d2.x)

        
