#Loops in python 
"""Loops are used to repeat instruction"""
"""count=1
while count <= 5 :
    print("Hello World")
    count +=1
    print(count)"""

#print number 1 to 10
"""i =1
while i<=10:
    print(i)
    i+=1"""
"""i=10
while i>=1:
    print(i)
    i-=1"""
#wap to print multiplication table of a number n
"""i = 1
n=int(input("enter number"))
while i<=10:
    print(n*i)
    i+=1"""

#print the element of the following list using a loop ;
#traverse :- one by one print 
"""nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx <len(nums):
    print(nums[idx])
    idx +=1"""

"""mens=["Nishant","Aditya","Golu","sonu","Sujeet"]
idx=0
while idx<len(mens):
    print(mens[idx])
    idx+=1"""
#Search for number x in this tuple using loop:
"""nums=[1,4,9,16,25,36,49,64,81,100]
x=int(input("enter the number"))
i=0
while i<len(nums):
    if(nums[i] == x):
        print("found at idx",i)
        break
    else:
        print("finding...")
    i+=1"""

#Break :- It is used to terminate the loop when encountered
"""i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1

print("end of loop")"""
 
#Continue :- It is used terminate the iteration , Or it is used to skip the element 
"""i=0
while i<=10:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1"""
#Odd number print
"""i=1
while i<=100:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1"""

#Even number print
"""i=1
while i<=50:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i+=1"""

# For loop is used to for sequential traversal . for traversing list strings ,tuples , etc .
"""nums=[1,2,3,4,5,6,7,8,9,0]
for i in nums:
    print(i)
    i+=1"""
 
"""str="Apnacollege"
for char in str:
    print(char)
else:
    print("End")"""

#Using For loop :- Print the elements of the folloing list using a loop
"""nums=[1,4,9,16,25,36,49,64,81,100]
x=36
idx=0
for el in nums:
    if(el==x):
      print("number is found at idx",idx)
      break
    idx += 1"""

#Range()function returns a sequence of a numbers , starting from 0 by default, and increments by 1, and stops before a specified numbers
#range(start?,stop,step?)
"""for el in range(10):  # range(stop)
    print(el)"""

"""for el in range (1,10): #range(start,stop)
    print(el)"""

#odd number print
"""for el in range(1,10,2): #range(start,stop,step)
    print(el)"""

#print numbers 100 to 1
"""for el in range(100,0,-1):
    print(el)"""

#print the multipication table of a number n.
"""n=int(input("enter the number"))
for i in range (1,11):
    print(n*i)
    i+=1"""

#Pass statements is a null statement that does nothing. it is used as a placeholder for future code.
"""for i in range(10):
    pass
if i>5:
    pass

print("i am good boy")"""

#Wap to find the sum of first n numbers.(using for)
"""n=10
sum=0
for i in range(1, n+1):
    sum+=i

print("total sum=",sum)   """ 
#using while
"""n=10
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("total sum=",sum)   """ 

#Wap to find the factorial of first n numbers.(using for)

"""n=5
fact=1
for i in range(1,n+1):
    fact*=i

print("factoial of fact",fact)  """  






