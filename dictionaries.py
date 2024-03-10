Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1={1:'aksh',2.1:'para','three':neha}
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    d1={1:'aksh',2.1:'para','three':neha}
NameError: name 'neha' is not defined
d1={1:'aksh',2.1:'para','three':'neha'}
print(d1)
{1: 'aksh', 2.1: 'para', 'three': 'neha'}
d2={1.'pranav',2:'neha',2:'aha'}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
d2={1:'pranav',2:'neha',2:'aha'}
print(d2)
{1: 'pranav', 2: 'aha'}
d2={1.'pranav',2:'neha',3:'neha'}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
KeyboardInterrupt
d2={1:'pranav',2:'neha',3:'neha'}
print(d2)
{1: 'pranav', 2: 'neha', 3: 'neha'}
d2={1:'pranav',2:'neha',3:'neha'}
d2[1]='pawan'
print(d2)
{1: 'pawan', 2: 'neha', 3: 'neha'}
#deleting
del d2[2]
print(d2)
{1: 'pawan', 3: 'neha'}
d2.pop(3)
'neha'
print(d2)
{1: 'pawan'}



d2.['pawan']
SyntaxError: invalid syntax
d1={1:'pawan',2:'kalyan',3:'ram'}
d2={1:101,2:102,3:103}
d1.len()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d1.len()
AttributeError: 'dict' object has no attribute 'len'
>>> d1.append(200)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d1.append(200)
AttributeError: 'dict' object has no attribute 'append'
>>> d1.get(1)
'pawan'
>>> d1.append(4,'raj')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d1.append(4,'raj')
AttributeError: 'dict' object has no attribute 'append'
>>> d1.get(1)
'pawan'
>>> d1.get('pawan)
...        
SyntaxError: unterminated string literal (detected at line 1)
>>> #update
...        
>>> d1.update(4,'raj')
...        
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    d1.update(4,'raj')
TypeError: update expected at most 1 argument, got 2
>>> d1.update('raj')
...        
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d1.update('raj')
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> d1.update({4:'raj'})
...        
>>> print(d1)
...        
{1: 'pawan', 2: 'kalyan', 3: 'ram', 4: 'raj'}
