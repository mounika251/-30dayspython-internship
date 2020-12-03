#1)list down all the error types and check all the errors using a python program for all errors 
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
except MoudleNotFoundError:
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

#2)design a simple calculator app with try and except for all use cases
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
try:
    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
                break
            else:
                print("Invalid Input")
except Exception as e:
    print(e)
    
#3)print one message if the try block raises a name error and another for other errors
 try:
        print(l)
 except NameError:
    print("variable is not defined")

#5)Try getting gan input  inside the try catch block
try:
    n1=int(input("enter num1: "))
    n2=int(input("enter num2: "))
    div=n1/n2
    print("result ",div)
except Exception as e:
    print(e)
