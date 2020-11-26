#1) write a program to create a list in of n integer values and do the following
a.add an item in to the list(using funtion)

using  append() method

a=["apple","banana","mango"]
print("before adding an item in to the list",a)
a.append("cherry")
print("After adding an item in to the list",a)

using insert() method

a=["apple","banana","mango"]
a.insert(2,"orange")
print(a)

b.delete(using function)

using remove() method

l1=[1,2,3]
l1.remove("2")
print(l1)

using pop() methood

l1=[1,2,3,4]
l1.pop()
print(l1)

using clear() method
l1=[1,2,3,4,5]
l1.clear()
print(l1)

c.store the largest number from the list to a variable

a=[1,2,3,10,7,8,20]
l=max(a)
print(l)

d.store the smallest number from the list to a variable

l1=[200,800,100,600,700]
l=min(l1)
print(l)

2.create a tuple and print the reverse of the created tuple

t1=(1,2,3,4,5)
print(t1)
rev=reversed(t1)
print(tuple(rev))

3.create a tuple and convert tuples into list

tuple1=(1,2,3,4,5)
print("list of items in tuple 1",tuple1)
list1=list(tuple1)
print("after converting tuple into list",list1)
