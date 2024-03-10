'''def alpha():
    try:
        
        print("Connection of alpha Establlished")
        a=10;
        b=0
        print(a/b)
        print("Connection of alpha Ended")
    except:
        print("Exception handles")
    
def beta():
    print("Connection of beta Establlished")
    alpha()
    print("Connection of beta Ended")

def gamma():
    print("Connection of gamma Establlished")
    beta()
    print("Connection of gamma Ended")
gamma()'''
#zerodivision error
'''def div():
    try:
        a=10
        b=0;
        print(a/"kodnest")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except:NameError:
        print("NameError")
    except:TypeError:
        print("TypeError")
        
div()
print("Futher statement")'''
#Custom error
'''class invalidAgeError(Exception):
    pass
def VaildateAge():
    age=int(input('Enter Age'))
    if(age>18):
        raise invaildAgeError
    else:
        print("Eligible")
VaildateAge()'''
#Custom Error As InvaildPinError
class InvaildPinError(Exception):
    pass
def vaildation():
    
    pin=int(input("Enter pin"))
    if pin==1927:
        print("Take Your Cash")
    else:
        raise InvaildPinError
try:
    vaildation()
except:
    print("Two Attempts Left")
    try:
        vaildation()
    except:
          
          print("One Attemp Remaiming")
    try:
        vaildation()
    except:
          
        print("Account Blocked")

        
