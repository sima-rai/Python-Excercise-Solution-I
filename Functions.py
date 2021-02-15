
#1. Write a Python function to find the Max of three numbers

#Ans:

# def max_fun(n1,n2,n3):
#     l=[n1,n2,n3]
#     max_num=max(l)
#     print('Max num is:', max_num)
# max_fun(1,2,3)


#------------------------------------------------------------------------------------------------------------


#2. Write a Python function to sum all the numbers in a list.


#Ans:

# def sum_func(l):
#     result= sum(l)
#     print(result)
# sum_func( (8, 2, 3, 0, 7))


#------------------------------------------------------------------------------------------------------------


#3. Write a Python function to multiply all the numbers in a list.


#Ans:

# def mul_fun(l):
#
#     mul=1
#     for i in l:
#         mul=mul *i
#     print(mul)
#
# mul_fun((8, 2, 3, -1, 7)) #Since in the sample question tuple is given instead of list. So i am using tuple


#------------------------------------------------------------------------------------------------------------


#4. Write a Python program to reverse a string.


#Ans:

# def reverse_func(s):
#     reverse=s[::-1]
#     print(reverse)
#
# reverse_func('1234abcd')


#------------------------------------------------------------------------------------------------------------


# 5. Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.


#Ans:

# def factorial(n):
#
#     fact=1
#     for i in range(n,1,-1):
#         fact=fact*i
#     print(fact)
#
# factorial(n=5)


#------------------------------------------------------------------------------------------------------------


#6. Write a Python function to check whether a number is in a given range.


#Ans:

# def check(n,r):
#     if n in range(r):
#         print('The number is in a given range')
#     else:
#         print("The number is not in a given range")
#
# check(2, r=5)


#------------------------------------------------------------------------------------------------------------


# 7. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.

#Ans:

# def calculate_upperandlower(s):
#     uppercount=0
#     lowercount=0
#     for i in s:
#         if i.isupper() == True:
#             uppercount=uppercount+1
#         elif i.islower()==True:
#             lowercount=lowercount+1
#     print('No. of Upper case characters:', uppercount)
#     print('No. of Lower case Characters:', lowercount)
#
# calculate_upperandlower('The quick Brow Fox')


#------------------------------------------------------------------------------------------------------------


# 8. Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

#Ans:

# def unique(l):
#
#     uniquelist=list(set(l))
#     print('Unique list:', uniquelist)
#
# unique([1,2,3,3,3,3,4,5])


#------------------------------------------------------------------------------------------------------------


# 9. Write a Python function that takes a number as a parameter and check the
# number is prime or not


#Ans:

# def check_primeornot(n):
#     if n>1:
#         for i in range(2,n):
#             if (n % i)== 0:
#                 print ('It is not prime number')
#                 break
#         else:
#             print('It is prime number')
#     else:
#         print('It is prime number')
#
# check_primeornot(7)


#------------------------------------------------------------------------------------------------------------


#10. Write a Python program to print the even numbers from a given list


#Ans:

# def even_numbers(l):
#     newlist=[]
#     for i in l:
#         if i%2==0:
#             newlist.append(i)
#     print(newlist)
#
# even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])


#------------------------------------------------------------------------------------------------------------


# 11. Write a Python program to create a lambda function that adds 15 to a given
# number passed in as an argument, also create a lambda function that multiplies
# argument x with argument y and print the result.


#Ans:

# add=lambda n: n+15
# sum=add(5)
# print('Sum is:', sum)
#
# mul=lambda x,y: x*y
# result=mul(2,4)
# print('Product is:', result)


#------------------------------------------------------------------------------------------------------------


# 12. Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.


#Ans:

# def multiples(n1):
#     n2=int(input('Enter a number:'))
#     mul=n1*n2
#     print(mul)
#
# multiples(5)


#------------------------------------------------------------------------------------------------------------


#13. Write a Python program to sort a list of tuples using Lambda.


#Ans:

# x=lambda l: sorted(l)
# sorted_list=x([(1,2),(0,4),(3,4), (7,8), (2,3)])
# print(sorted_list)


#------------------------------------------------------------------------------------------------------------


#14. Write a Python program to sort a list of dictionaries using Lambda.


#Ans:

# dict1=([{'name':'Hari', 'age':30}, {'name':'Ram', 'age':20}, {'name':'Krishna', 'age':10}])
# print(sorted(dict1, key=lambda v: v['age']))


#------------------------------------------------------------------------------------------------------------


#15. Write a Python program to filter a list of integers using Lambda.


#Ans:

# even=lambda x: x%2==0
# result=filter(even, [1,2,3,4,5,6,7,8])
# print(list(result))


#------------------------------------------------------------------------------------------------------------


# 16. Write a Python program to square and cube every number in a given list of
# integers using Lambda


#Ans:

# sqr=lambda x: x**2
# result=map(sqr, [1,2,3,4,5])
# print(list(result))
#
# cube=lambda x: x*x*x
# result=map(cube, [1,2,3,4,5])
# print(list(result))


#------------------------------------------------------------------------------------------------------------


# 17. Write a Python program to find if a given string starts with a given character
# using Lambda.


#Ans:

# check=lambda str, c: True if str[0]==c else False
# print(check('apple', 'a'))


#------------------------------------------------------------------------------------------------------------


# 18. Write a Python program to check whether a given string is number or not
# using Lambda.


#Ans:

# n=lambda s:s.isdigit()
# print(n('1235'))


#------------------------------------------------------------------------------------------------------------


#19. Write a Python program to create Fibonacci series upto n using Lambda.


#Ans:

# from functools import reduce
# fib= lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],range(n-2), [0, 1])
# print(fib(5))


#------------------------------------------------------------------------------------------------------------


# #20. Write a Python program to find intersection of two given arrays using
# Lambda.


#Ans:

# array1=[1,2, 3, 5, 7, 8, 9, 10]
# array2=[1,2,5,7,8,4]
#
# intersection=list(filter(lambda x: x in array1, array2))
# print(intersection)

























