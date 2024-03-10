'''def gen():
    yield 10
    print("hello")
    yield 20
res=gen()
print(next(res))
print(next(res))'''
#Wapp to create Generator function which will generate numbers of fibonacci series for every call of next()

'''def fib_series():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fib_gen=fib_series()
#print(next(fib_gen))
#print(next(fib_gen))
for i in range(5):
    print(next(fib_gen))'''
#Iterator
li=[10,20,30,40]
res=iter(li)
#print(next(res))
#print(next(res))
'''while True:
    try:
        print(next(res))
    except:
        break'''
#list silcing
li=[10,20,30,40,50]
print(li[::])#[10,20,30,40,50,60]
print(li[1:4:1])#[20,30,40]
print(li[::-1])#[60,50,40,30,20,10]
print(li[1:5:2])#[20,30]
