#1)Write a program to loop through a list of numbers and add +2 to every value to elements in list

l1=[1,2,3,4,5]
print("original list ",l1)
l2=[]
for i in range(0,len(l1)):
    l2.append(l1[i]+2)
print("resultant list is ",l2)

#2)Write a program to get the below pattern
#54321
#4321
#321
#21
#1

row=5
for i in range(0,row+1):
    for j in range(row-i,0,-1):
        print(j,end='')
    print()

#3)Python Program to Print the Fibonacci sequence

def fib(n):
    if(n==0):
        return 0
    elif(n==1):
         return 1
    else:
        return(fib(n-2)+fib(n-1))
n=int(input("enter the value of n"))
print("Fibonacci series",end='')
for n in range(0,n):
    print(fib(n),end='')

#4)Explain Armstrong number and write a code with a function

#Armstrong number:

#A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.

#For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.

num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  
    
#5)Write a program to print the multiplication table of 9

num=9
for i in range(1,11):  
   print(num,'x',i,'=',num*i)  

#6)Check if a program is negative or positive

num = int(input("Enter a number: "))  
  
if num > 0:  
 print(num,"is a positive number")  
elif num == 0:  
   print(num," is zero")
else:  
   print(num," is negative number")   

#7)Write a program to convert the number of days to ages

days=int(input("enter number of days: "))
years=int(days/365)
remaining_days=int(days%365)
m=int(remaining_days/30)
d=int(remaining_days%30)
print("number of years: ",years," years ",m," months ",d," days")

#8)Solve Trigonometry problem using math function write a program to solve using math function

import math
print(math. sin(0))
print(math.sin(45))
print(math.cos(45))
print(math.sin(0)+math. cos(0))

#9)Create a calculator only on a code level by using if condition (Basic arithmetic calculation)


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
  
choice = input("Enter choice(1/2/3/4):")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  
else:  
   print("Invalid input")  
