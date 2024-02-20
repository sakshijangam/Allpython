Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set1 = {10, 20, 30}
>>> set2 = {20, 40, 50}
>>> set1.difference_update(set2)
>>> print(set1)
{10, 30}
>>> 