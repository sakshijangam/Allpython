Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l1=[1,2,3]
>>> s1={"hlo","ok"}
>>> s1.update(l1)
>>> print(s1)
{1, 2, 3, 'hlo', 'ok'}
>>> #here we update list in set so update will add no of items or datatype in set but add will only put single item
>>> s1.remove("ok")
>>> print(s1)
{1, 2, 3, 'hlo'}
>>> s1.discard("hlo")
>>> print(s1)
{1, 2, 3}
>>> set1={"or","so","as","ok","to","us","of","go"}
>>> print(set1)
{'to', 'so', 'ok', 'of', 'go', 'us', 'as', 'or'}
>>> set2={"sun","mon","tue","wens"}
>>> set2={"sun","mon","tue","wens",(12,13)}#here u can see we add tuplebut list and set will show error
>>> print(set2)
{'wens', 'sun', 'tue', (12, 13), 'mon'}
>>> #set does not have any indexing concept order change every time
>>> print(set2)
{'wens', 'sun', 'tue', (12, 13), 'mon'}
>>> set2={"sun","mon","tue","wens",(12,13),"fri"}
>>> print(set2)
{'wens', 'sun', 'tue', (12, 13), 'fri', 'mon'}
>>> 
>>> print(s1)
{1, 2, 3}
>>> print(set1)
{'to', 'so', 'ok', 'of', 'go', 'us', 'as', 'or'}
>>> print(set2)
{'wens', 'sun', 'tue', (12, 13), 'fri', 'mon'}
>>> s2=set("jabgedczrop")
>>> print(s2)#set can created using set() constructor
{'j', 'g', 'a', 'p', 'r', 'o', 'e', 'b', 'c', 'z', 'd'}
>>> s3=set(range(1,8))#set will create using range() function
>>> print(s3)
{1, 2, 3, 4, 5, 6, 7}
>>> for no in s3:
	print(s3)

	
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}
{1, 2, 3, 4, 5, 6, 7}
>>> for no in s3:
	print(no)

	
1
2
3
4
5
6
7
>>> 
>>> print(len(s3))
7
>>> 
>>> print(max(s3))
7
>>> print(min(s3))
1
>>> print(all(s3))
True
>>> s4=
SyntaxError: invalid syntax
>>> s4={}
>>> print(any(s4))
False
>>> #if set is empty then all function return false
>>> print(all(s4))
True
>>> 
>>> #if set is empty or not all method return always true,any function retuen false when set is empty
>>> print(sum(s3))
28
>>> print(s2)
{'j', 'g', 'a', 'p', 'r', 'o', 'e', 'b', 'c', 'z', 'd'}
>>> print(sorted(s2))
['a', 'b', 'c', 'd', 'e', 'g', 'j', 'o', 'p', 'r', 'z']
>>> #set basic and function done
>>> #set method like add remove
>>> print(set1)
{'to', 'so', 'ok', 'of', 'go', 'us', 'as', 'or'}
>>> print(set2)
{'wens', 'sun', 'tue', (12, 13), 'fri', 'mon'}
>>> print(s1)
{1, 2, 3}
>>> print(s2)
{'j', 'g', 'a', 'p', 'r', 'o', 'e', 'b', 'c', 'z', 'd'}
>>> print(s3)
{1, 2, 3, 4, 5, 6, 7}
>>> s3.add(8)
>>> print(s3)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> s1.update(s3)
>>> print(s1)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> #here u can see that douplicate items automatically ignore
>>> #add method will add only one items and update method will add no of items ,list tuple in sets
>>> s1.discard(3)
>>> print(s1)
{1, 2, 4, 5, 6, 7, 8}
>>> s1.remove(8)
>>> print(s1)
{1, 2, 4, 5, 6, 7}
>>> s1.pop()
1
>>> print(s1)
{2, 4, 5, 6, 7}
>>> print(s2)
{'j', 'g', 'a', 'p', 'r', 'o', 'e', 'b', 'c', 'z', 'd'}
>>> s2.pop()
'j'
>>> s2.pop()
'g'
>>> s2.pop()
'a'
>>> print(s2)
{'p', 'r', 'o', 'e', 'b', 'c', 'z', 'd'}
>>> #here is the basic function and methods over sets have special function it will be in part2
>>> 