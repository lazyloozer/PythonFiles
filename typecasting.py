Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=5+6j
b=int(a.real)
print(b,type(b))
[DEBUG ON]
[DEBUG OFF]
print(b,type(b))
5 <class 'int'>
a=5+6j
b=int(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b=int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
a=5+6j
b=int(a.real)
SyntaxError: multiple statements found while compiling a single statement
a="123"
b=int(a)
print(b,type(a))
123 <class 'str'>
b=int(a)
print(b,type(b))
123 <class 'int'>
#str(float) to int
a="33.44"
print(a,type(a))
33.44 <class 'str'>
b=int(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    b=int(a)
ValueError: invalid literal for int() with base 10: '33.44'
a=True
b=int(a)
print(b,type(b))
1 <class 'int'>
a="5+6j"
b=int(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    b=int(a)
ValueError: invalid literal for int() with base 10: '5+6j'
a=5+3j
b=int(a.imag)
print(b,type(a))
3 <class 'complex'>
#converting in to float
a=44
b=float(a)
print(b,type(b))
44.0 <class 'float'>
#converting bool to float
a=True
b=float(a)
print(b,type(b))
1.0 <class 'float'>
a=False
b=float(a)
print(b,type(b))
0.0 <class 'float'>
#converting complex to float
a=44+7j
b=float(a)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    b=float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
a=44+7j
b=float(a.real)
print(b,type(b))
44.0 <class 'float'>
#converting float to float
a=33.4
b=float(a)
print(b,type(b))
33.4 <class 'float'>
a="123"
b=float(a)
print(b,type(b))
123.0 <class 'float'>
a="23.45"
b=float(a)
print(b,type(b))
23.45 <class 'float'>
a=123
b=bool(a)
print(b,type(b))
True <class 'bool'>
a=-123
b=bool(a)
print(b,typt(b))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(b,typt(b))
NameError: name 'typt' is not defined. Did you mean: 'type'?
a=0

b=bool(a)
print(b,typt(b))
SyntaxError: multiple statements found while compiling a single statement
a=0
b=bool(a)
print(b,type(b))
False <class 'bool'>
#convert into bool to float
a=23.44
b=bool(a)
print(b,typr(b))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(b,typr(b))
NameError: name 'typr' is not defined. Did you mean: 'type'?
a=23.44
b=bool(a)
print(b,type(b))
SyntaxError: multiple statements found while compiling a single statement
a=23.44
b=bool(a)
print(b,type(b))
True <class 'bool'>
#convrt bool to complex
a=3+4j
b=bool(a)
print(b,type(b))
True <class 'bool'>
a=0j
b=bool(a)
print(b,type(b))
False <class 'bool'>
a="122"
b=bool(a)
print(b,type(b))
True <class 'bool'>
a="0"
b=bool(a)
print(b,type(b))
True <class 'bool'>
[DEBUG ON]
[DEBUG OFF]
b="
SyntaxError: unterminated string literal (detected at line 1)
>>> a=""
>>> b=bool(a)
>>> print(b,type(b))
False <class 'bool'>
>>> #convert complex into all type
>>> a=124
>>> b=complex(a)
>>> print(b,type(b))
(124+0j) <class 'complex'>
>>> #convert complex to float
>>> a=12.34
>>> b=complex(a)
>>> print(b,type(b))
(12.34+0j) <class 'complex'>
>>> #convert complex into str
>>> a="123"
>>> b=complex(a)
>>> print(b,type(b))
(123+0j) <class 'complex'>
>>> a="123.44"
>>> b=complex(a)
>>> print(b,type(b))
(123.44+0j) <class 'complex'>
>>> a="kodnest"
>>> b=complex(a)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    b=complex(a)
ValueError: complex() arg is a malformed string
>>> #convert complex into bool
>>> a=True
>>> b=complex(a)
>>> print(b)
(1+0j)
>>> 
>>> a=False
>>> b=complex(a)
>>> print(b)
0j
