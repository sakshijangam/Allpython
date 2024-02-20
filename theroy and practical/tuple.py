Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuple1=tuple((1,2,3,4))
>>> print(tuple1)
(1, 2, 3, 4)
>>> tuple1=(1,2,3,4,5,6)
>>> Print(Tuple1[3])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Print(Tuple1[3])
NameError: name 'Print' is not defined
>>> print(tuple1)
(1, 2, 3, 4, 5, 6)
>>> print(tuple1[3])
4
>>> print(tuple1[-2])
5
>>> #here negative index start from -1 with backword direction
>>> # and postive index start from 0 with forward direction
>>> if 3 in tuple1:
	print("yes 4 is present in tuple")

	
yes 4 is present in tuple
>>> my_tuple = (1, 2, 3, 4, 1, 1)
>>> print(my_tuple.count(1))
3
>>> #count will show occurence
>>> my_tuple = ('a', 'b', 'c', 'd', 'e')
>>> print(my_tuple.index('c'))
2
>>> #it will give first occurance in tuple of that passed parameter
>>> my_tuple = (1, 2, 3, 4, 5)
>>> print(len(my_tuple))
5
>>> print(max(my_tuple))
5
>>> print(min(my_tuple))
1
>>> print(sum(my_tuple))
15
>>> print(sorted(my_tuple))
[1, 2, 3, 4, 5]
>>> x=("a","b”,"c","d")
   
SyntaxError: invalid syntax
>>> 
KeyboardInterrupt
>>> x=("a","b","c")
>>> y=list(x)
>>> y[2]="A"
>>> x=tuple(y)
>>> print(x)
('a', 'b', 'A')
>>> mytuple=("A","")
>>> os=("Abhi","basker home",34566)
>>> (name,address,phno)=os
>>> print(name)
Abhi
>>> print(phno)
34566
>>> x=("a","b","c","d")
>>> (A,B,*C)=x
>>> print(c)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(c)
NameError: name 'c' is not defined
>>> print(C)
['c', 'd']
>>> for y in x:
	print(y)

	
a
b
c
d
>>> for i in range(len(x))
SyntaxError: invalid syntax
>>> for i in range(len(x)):
	print(x)

	
('a', 'b', 'c', 'd')
('a', 'b', 'c', 'd')
('a', 'b', 'c', 'd')
('a', 'b', 'c', 'd')
>>> i=0
>>> while i<len(x):
	print(x)
	i=i+1

	
('a', 'b', 'c', 'd')
('a', 'b', 'c', 'd')
('a', 'b', 'c', 'd')
('a', 'b', 'c', 'd')
>>> 