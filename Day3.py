#1) write a python script to merge two python dictionaries

x={"a":1,"b":2}
y={"c":3,"d":4}
x. update(y)
print(x)

#2) write a python program to remove a key from dictionary 

fruits={"apple":2,"banana":3,"orange":4}
fruits.pop("banana")
print(fruits)

#3)write a python program to two lists into a dictionary 

a=["apple","banana","orange"]
b=[2,3,4]
print("the value of a ",a) 
print("the value of b ",b) 
temp={}
For i in a:
  For j in b:
    temp[i]=j
    b.remove(j)
  Break
print("after mapping two lists in a dictionary ",temp)

#4) write a python program to find the length of a set

a={"apple","orange","banana","mango"}
print(len(a))

#5) write a python program to remove the intersection of a 2nd set from the 1st set

a={1,2,3,4,5}
b={4,5,6,7,8}
print("the set value of a ",a)
print("the set value of b ",b)
a.difference_update(b)
print("remove the intersection of 2nd set from set from the 1st set ",a)
