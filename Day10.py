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


  
    
