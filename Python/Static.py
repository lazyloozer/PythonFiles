#Diffrent ways to create static variable
class demo:
    institute='Kodnest'
    def __init__(self):
        
        self.x=300
        demo.tech='MCP1'
        @staticmethod
        def static_method():
            print('Inside the static method')
            demo.fees=2500
        @classmethod
        def class_method(cls):
            demo.goal='JOB'
            cls.sub='Python'
print(demo.institute)
d1=demo();
print(d1.tech)
demo.static_method()

#table using static
'''class cal:
    @staticmethod
    def table(num):
        for i in range(1,11):
            print(num*i)
cal.table(int(input("Enter name")))'''
