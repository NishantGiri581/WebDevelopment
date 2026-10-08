"""str1= (" This is nishant giri \n I am from delhi")
print(str1)"""
#concatanation
"""str1 =(" This is arti") 
str2 =("This is nishant")
final_str=(str1+str2)
print(final_str)"""
#Length
"""str1= "Nishant"
len1=len(str1)
print(len1)
str2= "Giri"
len2=len(str2)
print(len2)
final_str= str1+" "+str2
print(final_str)
print(len(final_str))"""
#Indexing
"""str="Apna College"
print(str[3])"""
#Slicing = accessing parts of string
#str( starting_idx : ending_idx) forward
"""str="Apna college"
print(str[1:4])"""
#backward
"""str="Apple"
print(str[-3:-1])"""
#String Function
#endswith()
"""str="i am from apna college"
print(str.endswith("ege"))"""
#capitalize of 1st char
"""str="i am nishant giri"
print(str.capitalize())"""
#replace old value to new
"""str= "i am studying python from apna college"
print(str.replace("a","o"))"""
#find (word)
"""str="i am nishant giri"
print(str.find("s"))"""
#count function
"""str=" i am from delhi and from bihar"
print(str.count("from"))"""

#WAP to input user's first name & print its length
"""name= (input ("Enter the name :"))
print(len(name))"""
#Wap to find the occurance of $ in a string
"""str="Hi, i am $ and i love $ to build my $"
print (str.count("$"))"""

#Condition statement 
#if condition 
"""age=21
if(age>18):
    print("can vote")
    print("can drive")"""
#elif condition 
"""light="green"

if (light=="red"):
   print("stop")
elif(light=="green"):
   print("go")   
elif(light=="yellow"):  
   print("look") 

print("end of code")"""

#else condition 
"""age=14

if(age>=18):
    print("can vote")
else:
    print("cannot vote") """

#Grade student based on marks

"""marks= int(input("enter student marks :"))

if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"     
else:
    grade="D"

print("grade of the student ->", grade) """  

#Nesting  

"""age=43
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")    
else:
    print("cannot drive")  """

#wap to check if a number enter by the user is odd or even 
"""num= int(input("Enter the number"))
if(num % 2 ==0):
    print("even")
else:
    print("odd") """
#wap to find the greatest of 3 numbers enter by the user  
"""a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>=b and a>=c):
    print("first number is largest",a)
elif(b>=c):  
    print("second number is largest",b)
else:
    print("third number is largest",c)  """  

#wap to check if a number is a multiple of 7 or not
"""num=int(input("enter the number:"))

if(num%7==0):
    print("multiple of 7")
else:
    print("not a multiple")"""


    
"""num=int(input("enter the number"))
if (num%8==0):
    print("multiple of even")
else:
    print("multiple of odd")"""

#Factorial of n given by user
"""num = int(input("Enter the number"))
factorial = 1

for i in range(1 , num + 1):
    factorial *= i
    
print("The factorial of ",num, "is" ,factorial)"""


# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH

# s = input("Enter a string: ")
# reversed_s = s[::-1]
# print("Reversed string:", reversed_s)


# def reverse_string(s):
#     reversed = ""
#     for char in s:
#         reversed = char + reversed
#     return reversed 
# print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH


#Check if a string is palindrome or not
# def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]
# print(is_palindrome("Racecar"))  # Output: True

#Find the Largest Number in a List
# def find_largest_number(numbers):
#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num
#     return largest
# print(find_largest_number([3, 5, 2, 8, 1]))  # Output: 8

#Fibonacci Series
# def fibonacci_series(n):
#     a,b = 0,1
#     result = []
#     for _ in range(n):
#         result.append(a)
#         a,b = b, a+b
#     return result
# print(fibonacci_series(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Factorial of a Number
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))  # Output: 120
    
#Check if a String has Duplicate Characters
# def has_duplicates(s):
#     seen = set()
#     for char in s:
#         if char in seen:
#             return True
#         seen.add(char)
#     return False
# print(has_duplicates("hello"))  # True (l repeats)

#Swap Two Numbers (without a third variable)
# a = 5
# b = 10
# a = a+b
# b = a-b
# a = a-b

# print("After swapping: a =", a, ", b =", b)  # Output: a = 10, b = 5

#Find Second Largest Number in a List
# def second_largest(numbers):
#     unique = sorted(set(numbers), reverse=True)
#     if len(unique) < 2:
#         return None  # Not enough unique numbers
#     return unique[1]
# print(second_largest([4, 1, 9, 9, 3]))  # 4

#Count Frequency of Each Character in a String
# def char_frequency(s):
#     frequency = {}
#     for char in s:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     return frequency
# print(char_frequency("banana"))