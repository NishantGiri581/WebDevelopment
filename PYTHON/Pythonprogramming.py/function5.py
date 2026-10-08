#Function in python :- 
# Block of statements that perform a specific task.

"""def func_name(param 1, param 2..):
         #some work
          return val 
    func_name(arg1, arg2..)#function call"""

#add to number
# def sum(a,b):
#     sum=a+b
#     return sum
# print(sum(5,7))
# print(sum(35,54))
#fuction definition
"""def calc_sum(a,b): #parameters
    return a+b

sum=calc_sum(12,43) #function call ; arguements
print(sum)"""

"""def print_Hello():
    print("Hello")

print_Hello()   """


#Average of three number
"""def calc_avg(a,b,c):
    sum= a+b+c 
    avg= sum/3
    print(avg)
    return avg
calc_avg(2,4,5)"""

#Function types
#Built in Function         # User defined function
"""                        already in python
print()
len()
type()
range()
"""
#Default Parameters
# Assigning a default vale to parameter, which is used when no argument is passed.
"""def calc_prod(a=4,b=3):
    print(a*b)
    return a*b
calc_prod()"""

#Wap to print the lenth of a list.(list is the parameter)
"""cities=["Delhi","pune","goa","patna"]
heroes = [1,2,3,4,5,6,7,8,9,]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)"""

#Wap to print the elements of a list in a single line.(list in a parameter)

"""cities=["Delhi","pune","goa","patna"]
heroes = ["rohit","sonu",2,3,4,5,6,7,8,9,]

print(heroes[0],end=" ") # end=" " - it is used to print in same line.
print(heroes[1],end=" ")

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)
print()"""

#Wap to find the factorial of n.(n is the parameter)
"""n=5
fact=1
for i in range(1,n+1):
    fact *=i
    print(fact)   this logic in use in function"""

"""n=5
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    print(fact)    

calc_fact(5)"""

#Wap to convert USD to INR.
"""def converter(usd_val):
    inr_val=usd_val * 83
    print(usd_val,"USD= ",inr_val,"INR= ")
converter(10)"""
