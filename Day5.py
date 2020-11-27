#1)Create a function getting two integer inputs from user. & print the following:

#Addition of two numbers is +value
#Subtraction of two numbers is +value
#Division of two numbers is +value
#Multiplication of two numbers is +value

num1=int(input("Enter 1st number :"))
num2=int(input("Enter 2nd number :"))
def add_num(a,b):
    print("addition of two numbers:",a+b)
    print("subtraction of two numbers:",a-b) 
    print("multiplication of two numbers:",a*b)
    print("division of two numbers:",a/b)

add_num(num1,num2)


#2)Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree

n=input("Enter patient name :")
def covid(name,temp):
    print("name  of patient:",name)
    print("body temperature:" ,temp) 
    

covid(n,98)

