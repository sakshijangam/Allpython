Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #variable rule
>>> 23v=4 #caanot begin with number
SyntaxError: invalid syntax
>>> a$=5 #no special characters except_
SyntaxError: invalid syntax
>>> a_1=5 #it is correct way
>>> print (a_1)
5
>>> x=200
>>> print(x,type(x)) #it will print data type of x
200 <class 'int'>
>>> x=34.5
>>> print(x,type(x))
34.5 <class 'float'>
>>> x="okay"
>>> print(x,type(x))
okay <class 'str'>
>>> #list
>>> x=[3,5,4,35]
>>> print(x,type(x))
[3, 5, 4, 35] <class 'list'>
>>> x={3,56,785,45,820}
>>> print(x,type(x))
{3, 45, 785, 820, 56} <class 'set'>
>>> x=(3,4,56,83,53)
>>> print(x,type(x))
(3, 4, 56, 83, 53) <class 'tuple'>
>>> x={1:apple,2:mango}
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x={1:apple,2:mango}
NameError: name 'apple' is not defined
>>> x{1:"apple",2:"mango",3:34}
SyntaxError: invalid syntax
>>> x={1:"apple",2:"mango",3:34}
>>> print(x,type(x))
{1: 'apple', 2: 'mango', 3: 34} <class 'dict'>
>>> x
{1: 'apple', 2: 'mango', 3: 34}
>>> a=3
>>> b
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> a=4
>>> b=2
>>> a+b=c
SyntaxError: cannot assign to operator
>>> c=a+b
>>> print(c)
6
>>> c=a-b
>>> print(c)
2
>>> c=a*b
>>> print(c)
8
>>> c=a/b
>>> print (c)
2.0
>>> c=a//b
>>> print(c,type(c))
2 <class 'int'>
>>> c=a**b
>>> print(c)
16
>>> a=45
>>> b=4
>>> c=a%b
>>> print(c)
1
>>> x=4
>>> y=8
>>> print("x==y",x==y)
x==y False
>>> print("x!=y",x!=y)
x!=y True
>>> print("x<y",x<y)
x<y True
>>> print("x>y",x>y)
x>y False
>>> print("x>=y"x>=y)
SyntaxError: invalid syntax
>>> print("x>=y",x>=y)
x>=y False
>>> print("x<=y",x<=y)
x<=y True
>>> #end of practical for logical operator we have to learn loop