#1)Create a lambda function that multiplies argument x with argument y

x = lambda a, b : a * b
print(x(5, 10))

#2)Write a Python program to create Fibonacci series to n using Lambda

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(fib(10))

#3)Write a Python program that multiply each number of given list with a given number 

l1 = [2, 4, 6, 9 , 11]
n = 5
print("Original list: ", l1)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,l1))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

#4)Write a Python program to find numbers divisible by 9 from a list of numbers 

list_1 = [81, 9, 54, 45, 102, 339, 221,]
result = list(filter(lambda x: (x % 9 == 0), list_1))
print("Numbers divisible by 9 are",result)

#5)Write a Python program to count the even numbers in a given list of integers 
 
l1=[10,40,5,20,9,7,55,4,29]
even=0
for i in l1:
	if(i%2==0):
		even+=1
print("even numbers in the list",even)
 
