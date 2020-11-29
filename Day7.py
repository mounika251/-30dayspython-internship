#1)Create a python module with list and import the module in another .py file and change the value in list

#list1.py
l1=[4,2,6,8]

#demo.py
import list1 as li
k=[]
k=li.l1
for i in range(len(k)):
	k[i]=k[i]+10
print(k)


#3)Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run

import random 
n=random.randint(1,100)
print(n)

#4)Import sys package and find the python path

import sys,os
file=sys.argv[0]
pathname=os.path.dirname(file)
print(pathname)
