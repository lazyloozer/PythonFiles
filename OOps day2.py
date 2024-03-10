#examples
'''class institue:
    def __init__(self,name):
        self.name=name;
    def course(self):
        print("inside the method")
    def main():
        in1=institue('kodnest')
        in1.course()
        print(in1.name)
     main()
 print(in1.name)'''
#Access Modifier using Inhertiance
class demo1:
    def __init__(self):
        self.name='kodnest' #public
    def test1(self):
        print("Accessing inside test1 methods using self:",self.name)
d1=demo1()
d1.test1()
print(d1.name)

class demo2(demo1):
    def test2(self):
        
          print("Accessing inside test1 methods using d1:",self.name)
d2=demo2()
d2.test2()
d2.test1()
        
 
