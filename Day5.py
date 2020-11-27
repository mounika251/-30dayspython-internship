#1)Create a function getting two integer inputs from user. & print the following:

#Addition of two numbers is +value
#Subtraction of two numbers is +value
#Division of two numbers is +value
#Multiplication of two numbers is +value

def add_num(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div;
num1=int(input("Enter 1st number :"))
num2=int(input("Enter 2nd number :"))
print("add,sub,mul,div",add_num(num1,num2))



#2)Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree

def covid(name,temp=98):
    return n,temp
n=input('enter name: ')
print('patient name and body temperature',covid(n))
