'''def decor(function):
    def inner(name):
        if name=='Deep':
            print(name,'likes pulav')
        else:
            function(name)
    return inner
@decor
def food(name):
    print(name,"likes biryani")
food('Ayush')
food('Deep')'''

#example 2
def smartdiv(function):
    def inner(a,b):
        if b==0:
            print('b cannot be zero')
        else:
            function(a,b)
    return inner
@smartdiv
def div(a,b):
    print(a/b)
div(10,2)
div(10,0)
