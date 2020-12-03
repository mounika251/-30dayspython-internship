print("types of errors")
print("1.index error")
a=[1,2,3]
try:
    print(a[4])
except IndexError:
    print("index not found in array")
    
print("2.key error")
d={"1":1,"2":2,"3":3}
try:
    print(d[4])
except KeyError:
    print("key not found in dictionary")
    
print("3.module not found error")
try:
    import list 
except:
    print("module not found")

print("4.zero division error ")
try:
    a=10/0
except ZeroDivisionError :
    print("unable to divide by zero")

print("5.Name error")
try:
    print(s)
except NameError:
    print("varible s is not defined")

print("6.type error  ")
try:
    n=2
    str="hello"
    print(str+n+str)
except TypeError :
    print("must be string,not int ")
   
print("7.null pointer error")
try:
    s1=none
    print(len(s1))
except:
    print("null pointer exception")



