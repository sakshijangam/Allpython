Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dic1 = {1: 10, 2: 20}
>>> dic2 = {3: 30, 4: 40}
>>> dic3 = {5: 50, 6: 60}
>>> 
>>> dic1.update(dic2)
>>> a=(dic1)
>>> print(a)
{1: 10, 2: 20, 3: 30, 4: 40}
>>> a.update(dic3)
>>> b=(a)
>>> print(b)
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
>>> 