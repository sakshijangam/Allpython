Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d1={1:"ok",2:"so",3:"as",4:"to",5:"or"}
>>> print(d1)
{1: 'ok', 2: 'so', 3: 'as', 4: 'to', 5: 'or'}
>>> x=d1[3]
>>> print(x)
as
>>> #another way to get value of 3 key
>>> x=d1.get(4)
>>> print(x)
to
>>> d1[3]="on"
>>> print(d1)
{1: 'ok', 2: 'so', 3: 'on', 4: 'to', 5: 'or'}
>>> x=d1.items()
>>> print(x)
dict_items([(1, 'ok'), (2, 'so'), (3, 'on'), (4, 'to'), (5, 'or')])
>>> x=d1.values()
>>> print(x)
dict_values(['ok', 'so', 'on', 'to', 'or'])
>>> x=d1.keys()
>>> print(x)
dict_keys([1, 2, 3, 4, 5])
>>> x=d1.popitem()
\
>>> print(x)
(5, 'or')
>>> x=d1.popitem()
>>> print(x)
(4, 'to')
>>> print(d1)
{1: 'ok', 2: 'so', 3: 'on'}
>>> d2={"a":"A","b":"B","c":"C"}
>>> print(d2)
{'a': 'A', 'b': 'B', 'c': 'C'}
>>> d2.add({1:"do"})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d2.add({1:"do"})
AttributeError: 'dict' object has no attribute 'add'
>>> #addis not a method insted we have update method
>>> d2.update({1:"do"})
>>> print(d2)
{'a': 'A', 'b': 'B', 'c': 'C', 1: 'do'}
>>> d1.update(d2)
>>> print(d1)
{1: 'do', 2: 'so', 3: 'on', 'a': 'A', 'b': 'B', 'c': 'C'}
>>> #update will do work for adding one item or many or dic also
>>> print(d1)
{1: 'do', 2: 'so', 3: 'on', 'a': 'A', 'b': 'B', 'c': 'C'}
>>> print(d2)
{'a': 'A', 'b': 'B', 'c': 'C', 1: 'do'}
>>> #functions of dictionary
>>> print(len(d1))
6
>>> 
>>> print(max(d1))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(max(d1))
TypeError: '>' not supported between instances of 'str' and 'int'
>>> #here values are in string form so this error will raise
>>> d3={"a":3,"f":4,"b":1}
>>> print(max(d3))
f
>>> print(min(d3))
a
>>> for x in d1.values():
	print(x)

	
do
so
on
A
B
C
>>> for x in d1.keys():
	print(x)

	
1
2
3
a
b
c
>>> for x,y in d1.items():
	print(x,y)

	
1 do
2 so
3 on
a A
b B
c C
>>> 