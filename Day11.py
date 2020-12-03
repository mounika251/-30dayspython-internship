#1)Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.


list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
s=list(zip(list_a, list_b))
print(s)

#2)First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.


lst1=['a','b','c','d','e','f','g','h']
rng1 = list(range(1,8))
lst = list(zip(rng1, lst1))
print(lst)

#3)Using sorted() function, sort the list in ascending order.


n=[100,20,50,40,5]
n. sort()
print(n)

#4)Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list

n=[100,20,50,40,5,80,55,7,42]
print(list(filter(lambda x:(x%2!=0),n)))
