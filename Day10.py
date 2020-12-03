#1)Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re
def sample(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(sample("ABCDEFabcdef123450")) 
print(sample("*&%@#!}{"))
print(sample("hello@123"))
print(sample("hello123"))

#2)Write a Python program that matches a word containing 'ab'.

import re
def check(string) : 
    regex = re.compile("ab+\w*")
    match_object = regex.findall(string)
    if len(match_object) != 0 : 
        for word in match_object : 

            print("word containing ab in ",string, "is ")
            print(word) 

              

    else : 

        print("No match") 
if __name__ == '__main__' : 
    string = "I need a cab"
    check(string) 

#3)Write a Python program to check for a number at the end of a word/sentence.


import re 
s = "python is a popular programming language "
print ("The original string is : " +  s) 
res = len(re.findall(r'\w+', s)) 
print ("The number of words in string are : " +  str(res)) 

#4)Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string


import re
res = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 12,2,3and 13 are important")
print("Number of length 1 to 3")
for num in res:
     print(num.group(0))

#5)Write a Python program to match a string that contains only uppercase letters


     
    
import re
def demo(s):
        patterns = '^[A-Z]*$'
        if re.search(patterns, s):
                return (s, 'Found a match!')
        else:
                return(s,'Not matched!')

print(demo("PYTHON"))
print(demo("WELCOME"))
print(demo("HelloWorld"))
print(demo("python"))
print(demo("Python"))

	 
	 
    
