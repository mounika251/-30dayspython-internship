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

a={"apple","banana","orange"}
b={2,3,4}
print("the value of a ",a) 
print("the value of b ",b) 
temp={}
for i in a:
  for j in b:
    temp[i]=j
    b.remove(j)
    break
print("after mapping two lists in a dictionary ",temp)
