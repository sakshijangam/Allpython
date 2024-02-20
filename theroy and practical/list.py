Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=list([1,2,3,4,5])#here we use list constructor to creating list
>>> print (list1)
[1, 2, 3, 4, 5]
>>> list2=list(range(1,6))#here by using range function list is created
>>> print (list2)
[1, 2, 3, 4, 5]
>>> list2.append(6)#it will add no number that is given as parameter at the end of list
>>> print (list2)
[1, 2, 3, 4, 5, 6]
>>> list1.clear()#it will remove all element in list
>>> print (list1)
[]
>>> list1.extend(list2)
>>> print (list1)
[1, 2, 3, 4, 5, 6]
>>> #here as u see list2 is added into list1
>>> list1.insert(2,8)
>>> print(list1)
[1, 2, 8, 3, 4, 5, 6]
>>> #here at postion 2 ,8 value will added in list1
>>> l2=[2,2,2,3,3,3,3,4,5,6,6,6]
>>> print(l2)
[2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6]
>>> l2.count(3)
4
>>> l2.pop(3)
3
>>> l2.pop(1)
2
>>> #here u see pop willshow the value of given index
>>> print (list2)
[1, 2, 3, 4, 5, 6]
>>> list2.reverse()
>>> print (list2)
[6, 5, 4, 3, 2, 1]
>>> #here list get reverse
>>> list1.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list1.sort(reverse=true)
NameError: name 'true' is not defined
>>> list1.sort(reverse=True)#here list will sort as decending order by defalut it sort as ascending order
>>> print(list1)
[8, 6, 5, 4, 3, 2, 1]
>>> list1.sort()
>>> print(list1)
[1, 2, 3, 4, 5, 6, 8]
>>> list1.remove(2)
>>> print(list1)
[1, 3, 4, 5, 6, 8]
>>> #here remove method will remove first occurence of 2
>>> print (l2)
[2, 2, 3, 3, 3, 4, 5, 6, 6, 6]
>>> l2.count(6)
3
>>> l2.remove(6)
>>> l2.count(6)
2
>>> #here is the proof
>>> print(len(l2))
9
>>> print("max no from list1",max(list1))
max no from list1 8
>>> print("min no from list1",min(list1))
min no from list1 1
>>> print(l2)
[2, 2, 3, 3, 3, 4, 5, 6, 6]
>>> print("sum of all items in list l2",sum(l2))
sum of all items in list l2 34
>>> print(list(1,10,2))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(list(1,10,2))
TypeError: list expected at most 1 argument, got 3
>>> print(list(1,10))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(list(1,10))
TypeError: list expected at most 1 argument, got 2
>>> print (list(range(1,10)))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l1=(list(range(1,20)))
>>> print(l1)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> print(l1[1:15:2])
[2, 4, 6, 8, 10, 12, 14]
>>> print(l1[1:15])
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
>>> #here index start from 0 ans the ending point is exclusive
>>> list3=[10,100,1000,10000]
>>> for x in list3:
	print(x)

	
10
100
1000
10000
>>> 