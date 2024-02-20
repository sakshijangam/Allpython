Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
>>> list_without_empty_strings = [string for string in list1 if string != ""]
>>> print("List without empty strings:", list_without_empty_strings)
List without empty strings: ['Mike', 'Emma', 'Kelly', 'Brad']
>>> 