#1. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'


#Ans:

def count_string(str):
    dict = {}
    for value in str:
        c=str.count(value)
        dict[value]=c
    print(dict)

count_string('google.com')


#--------------------------------------------------------------------------------------------------------------------


#2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the
#string length is less than 2, return instead of the empty string.



#Ans:

def new_string(str):
    if len(str)>=2:
        first=str[0:2]
        second=str[-2:len(str)]
        str1= first + second
        print(str1)
    elif len(str)<2:
        str2=''
        print(str2)  #question was not clear to me so i have printed in two ways
        print('Empty String')
new_string('python')


#--------------------------------------------------------------------------------------------------------------------


# 3. Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.


#Ans:

def new_pattern(str1):
    count=0
    l=list(str1)
    for i in l:
        if l[0]==i and count>1:
            l[count]='$'

        count+=1
        newstr=str(l)
    print(newstr)

new_pattern('restart')


#--------------------------------------------------------------------------------------------------------------------


# 4. Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.


#Ans:

def single_str(s1, s2):
    #Convering string into list
    l1=list(s1)
    l1[0:2]=s2[0:2]

    l2=list(s2)
    l2[0:2]=s1[0:2]

    #Converting list into string

    l1.insert(len(s1)+1, " ")
    l3=l1+l2
    newstr=''
    print(newstr.join(l3))

single_str('abc', 'xyz')


#--------------------------------------------------------------------------------------------------------------------


# 5. Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.


#Ans:

def add_characters(s1):
    if len(s1)>=3:
        if s1[-3:len(s1)+1]=='ing':
            x='ly'
            s=s1+x
        else:
            x='ing'
            s=s1+x
        print(s)
    else:
        print(s1)

add_characters('abc')


#--------------------------------------------------------------------------------------------------------------------


# 6. Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.


#Ans:

def change_into_good(s1):


    indxNot=s1.find('not')
    indxPoor=s1.find('poor')


    if ('not' in s1 and 'poor' in s1):
        if indxNot<indxPoor:
            substr=s1[indxNot:(indxPoor+len('poor'))]
            newstr=s1.replace(substr, 'good')
            return newstr
        else:
            return s1
    else:
        return s1

print(change_into_good('The lyrics is not that poor'))


#------------------------------------------------------------------------------------------------------------


# 7. Write a Python function that takes a list of words and returns the length of the
# longest one.


#Ans:

def length_of_longest(list):
    l = []
    for i in list:
        l.append(len(i))

    longest=max(l)
    return longest

print(length_of_longest(['ram', 'shyam', 'krishna', 'ganesh']))


#--------------------------------------------------------------------------------------------------------------------


# 8. Write a Python program to remove the nth index character from a nonempty string.


#Ans:

def remove(str, n):
    l=list(str)
    c=l[n]
    l.remove(c)
    s=''
    newstr=s.join(l)
    print('Removed character is', c)

    return newstr

print('New string after removing nth character from given string is', remove('Capital', 4))


#--------------------------------------------------------------------------------------------------------------------


# 9. Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.


#Ans:

def exchange_characters(str):
    l=list(str)
    l[0]=str[-1]
    l[-1]=str[0]
    s=''
    newstr=s.join(l)
    print('New exchanged string is', newstr)

exchange_characters('country')


#--------------------------------------------------------------------------------------------------------------------


# 10. Write a Python program to remove the characters which have odd index
# values of a given string.


#Ans:

def remove_odd(str):

    l=list(str)
    count = 0
    print('The characters that have odd index in a given string are:')
    for i in l:
        if count % 2 != 0:
            print(i)
        count+=1

remove_odd('algebra')


#------------------------------------------------------------------------------------------------------------


# 11. Write a Python program to count the occurrences of each word in a given
# sentence.


#Ans:

def count_words(str):
    newstr=str.split()
    newdict={}

    for value in newstr:
        c=newstr.count(value)
        newdict[value]=c
    print(newdict)

count_words('Nepal is a beautiful country. It is a peaceful country.')


#------------------------------------------------------------------------------------------------------------


# 12. Write a Python script that takes input from the user and displays that input
# back in upper and lower cases.


#Ans:

def take_input(str):
    x=input(str)
    uppercase=x.upper()
    lowercase=x.lower()
    print('Uppercase:', uppercase)
    print('lowercase:', lowercase)

take_input('Enter your input:')


#------------------------------------------------------------------------------------------------------------


# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).


#Ans:

def sort_fun(str):
    l=str.split(',')
    unsorted_list=list(set(l))
    sorted_list=sorted(unsorted_list)

    #now joining list
    st=','
    newstr=st.join(sorted_list)
    print('Sorted sequence is:', newstr)

sort_fun('red, white, black, red, green, black')


#---------------------------------------------------------------------------------------------------------------


# 14. Write a Python function to create the HTML string with tags around the
# word(s).


#Ans:

def add_tags(s1, s2):
    print("HTML String is:")
    print(f"<{s1}>{s2}</{s1}>")

add_tags('i', 'Python')


#------------------------------------------------------------------------------------------------------------


# 15. Write a Python function to insert a string in the middle of a string.


#Ans:

def insert_string_middle(s1, s2):
    l1=list(s1)
    indx=(int(len(s1)/2))
    l1.insert(indx, s2)
    s=''
    newstr=s.join(l1)
    print('New string is:', newstr)

insert_string_middle('{{}}', 'PHP')


#------------------------------------------------------------------------------------------------------------


#16. Write a Python program to sum all the items in a list.


#Ans:

def summation(list):
    result=sum(list)
    print(result)

summation([1,2,3,4,5])


#------------------------------------------------------------------------------------------------------------


#17. Write a Python program to multiplies all the items in a list.


#Ans:

def multiplication(list):
    mul=1
    for i in list:
        mul=mul*i
    print('The product is', mul)

multiplication([2,3,5])


#------------------------------------------------------------------------------------------------------------


# 18. Write a Python program to get the largest number from a list.

#Ans:

def largest(list):

    x=max(list)
    print("Largest number from a given list is", x)

largest([1,2,3,4,5])


#------------------------------------------------------------------------------------------------------------


#19. Write a Python program to get the smallest number from a list.


#Ans:

def smallest(list):

    x=min(list)
    print("Smallest number from a given list is", x)

smallest([1,2,3,4,5])


#------------------------------------------------------------------------------------------------------------


# 20. Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.

#Ans:

def count_func(list):

    count=0
    for i in list:
        if len(i)>=2 and i[0]==i[-1]:
            count=count+1
    print("The count is", count)

count_func(['abc', 'xyz', 'aba', '1221'])


#------------------------------------------------------------------------------------------------------------


# 21. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.

#Ans:

def sort_fun(list):
    for i in list:
        def func1(t):
            x=t[-1]
            return x
        func1(i)
    print(sorted(list, key=func1))

sort_fun([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])


#------------------------------------------------------------------------------------------------------------


#22. Write a Python program to remove duplicates from a list.


#Ans:

def remove_duplicates(list):

    l2=[]
    for value in list:
        if list.count(value)==1:
            l2.append(value)

    print("New list is:", l2)

remove_duplicates(['apple', 'ball', 'ball', 2,2,1,3])


#------------------------------------------------------------------------------------------------------------


# 23. Write a Python program to check a list is empty or not.


#Ans:

def check_list(list):
    l=[]
    if list==l:
        print('List is empty')
    else:
        print('List is not empty')


check_list([1,2,3])


#------------------------------------------------------------------------------------------------------------


# 24. Write a Python program to clone or copy a list.


#Ans:

l1=[1,2,3,4,5,'apple']
l2=l1.copy()
print('Copied list is:', l2)


#------------------------------------------------------------------------------------------------------------


# 25. Write a Python program to check whether all dictionaries in a list are empty or
# not.


#Ans:

def check_fun(list):
    l=[]
    a={}
    for i in list:
        if i == a:
            l.append(True)

        else:
            l.append(False)

    x = all(l)
    return x

print(check_fun([{}, {}, {}]))


#------------------------------------------------------------------------------------------------------------


# 26. Write a Python program to insert a given string at the beginning of all items in
# a list.

#Ans:

def insert_fun(list1, string1):
    l=[]
    for i in list1:
        string2=str(i)
        s=string1 + string2
        l.append(s)
    print('New list is:', l)

insert_fun([1,2,3,4], 'emp')


#------------------------------------------------------------------------------------------------------------


# 27.Write a Python program to replace the last element in a list with another list


#Ans:

def replace_last_element(l1,l2):
    l1.pop(-1)
    l=l1+l2
    print(l)

replace_last_element( [1, 3, 5, 7, 9, 10], [2, 4, 6, 8])


#------------------------------------------------------------------------------------------------------------


# 28. Write a Python script to add a key to a dictionary.

#Ans:

def add_key(dict1):

    d={}
    value=0

    for i in range(3):
        key=i
        value=value+10
        d[key]=value
    print(d)

add_key({0: 10, 1: 20})


#------------------------------------------------------------------------------------------------------------


# 29. Write a Python script to concatenate following dictionaries to create a new
# one.

#Ans:

def concatenate_dicts(d1, d2, d3):
    d1.update(d2)
    d1.update(d3)
    print(d1)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

concatenate_dicts(dic1, dic2, dic3)


#------------------------------------------------------------------------------------------------------------


# 30. Write a Python script to check whether a given key already exists in a
# dictionary.


#Ans:

def check_key(dict1, k):
    if k in dict1.keys():
        print('Given key already exists')
    else:
        print('Given key does not exist')


check_key({1: 10, 2: 20}, 2)


#------------------------------------------------------------------------------------------------------------


#31. Write a Python program to iterate over dictionaries using for loops.


#Ans:

dict1={1:10, 2:20, 3:30}
for item in dict1.items():
    print(item)


#------------------------------------------------------------------------------------------------------------


# 32. Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).


#Ans:

def generate_dict(n):

    d={}
    for i in range(1, n+1):
        key=i
        value=i*i
        d[key]=value

    print(d)

generate_dict(n=5)


#------------------------------------------------------------------------------------------------------------


# 33. Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys


#Ans:

def print_dict(n):

    d={}
    for i in range(1, n+1):
        key=i
        value=i*i
        d[key]=value

    print(d)

print_dict(n=15)


#------------------------------------------------------------------------------------------------------------


# 34. Write a Python script to merge two Python dictionaries.

#Ans:

def merge_dicts(d1, d2):
    d1.update(d2)
    print(d1)

merge_dicts({1:10, 2:20}, {3:30, 'a':40})


#------------------------------------------------------------------------------------------------------------


#35. Write a Python program to iterate over dictionaries using for loops.


#Ans:

dict1={1:10, 2:20, 3:30}
for item in dict1.items():
    print(item)


#------------------------------------------------------------------------------------------------------------


#36. Write a Python program to sum all the items in a dictionary.

#Ans:

d={'a':10, 'b':20, 'c':30}
total=sum(d.values())
print(total)


#------------------------------------------------------------------------------------------------------------


#37. Write a Python program to multiply all the items in a dictionary

#Ans:

d={'a':2, 'b':2, 'c':3}
mul=1
for i in d.values():
    mul=mul*i
print(mul)


#------------------------------------------------------------------------------------------------------------


#38. Write a Python program to remove a key from a dictionary.


#Ans:

def remove_key(dict, removekey):
    k=dict.pop(removekey)
    print(f'Removed key is {removekey} and removed value is {k}')
    print('New dict is', dict)

remove_key({1:10, 2:20, 3:30}, removekey=1)


#------------------------------------------------------------------------------------------------------------


#39. Write a Python program to unpack a tuple in several variables.

#Ans:

test_tuple=('Ram', '30', 'Nepali')
name, age, nationality=test_tuple
print(f'Name is: {name}, Age is: {age}, Nationality is {nationality}')


#------------------------------------------------------------------------------------------------------------


#40. Write a Python program to add an item in a tuple.


#Ans:

def add_in_tuple(t, additem):

    l=list(t)
    l.append(additem)
    newtuple=tuple(l)
    print(newtuple)

add_in_tuple((1,2,3), additem=9)


#------------------------------------------------------------------------------------------------------------


#41. Write a Python program to convert a tuple to a string.


#Ans:

def tuple_to_string(t):
    l=[]
    for i in t:
        l.append(str(i))
    s=''
    newstr=s.join(l)
    print('Given tuple is converted to string as:', newstr)

tuple_to_string((1,2,3,4))


#------------------------------------------------------------------------------------------------------------


#42. Write a Python program to convert a list to a tuple.

#Ans:

l=[1,2,3]
t=tuple(l)
print(f'List {l} is converted to tuple {t}')


#------------------------------------------------------------------------------------------------------------


#43. Write a Python program to remove an item from a tuple.

#Ans:

def remove_from_tuple(t, removeitem):

    l=list(t)
    l.remove(removeitem)
    newtuple=tuple(l)
    print(newtuple)

remove_from_tuple((1,2,3,4), removeitem=2)


#------------------------------------------------------------------------------------------------------------


#44. Write a Python program to slice a tuple.


#Ans:

t=(1,2,3,4,5,6,7)
print('Sliced tuple is', t[2:5])


#------------------------------------------------------------------------------------------------------------


#45. Write a Python program to find the index of an item of a tuple


#Ans:

t=(1,2,3,4,5)
l=list(t)
i=l.index(4)
print(i)


#------------------------------------------------------------------------------------------------------------


#46. Write a Python program to find the length of a tuple


#Ans:

t=(1,2,3,4,5)
print('length is:', len(t))





























