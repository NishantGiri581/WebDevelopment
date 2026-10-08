#Basic for loop program
#1 Print numbers from 1 to 10 using for loop.
# for i in range(1,11):
#     print(i,end=" ")

#2 Print square of numbers from 1 to 10.
# for i in range(1,11):
#     print(i*i,end=" ")    

#3 Print cube of above number.
# for i in range(1,11):
#     print(i**3,end=" ")   

#4 print sum of numbers of above numbers
# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print(sum,end=" ")

#5 print product of above number.
# product = 1
# for i in range(1,11):
#     product = product * i
# print(product,end=" ")

#6 print reverse order of above number.
# for i in range(10,0,-1):
#     print(i,end=" ")

# 7 print even number of above numbers.
# for i in range(1,11):
#     if i%2==0:
#         print(i,end=" ")

#8 Print odd number.
# for i in range(1,11):
#     if i%2!=0:
#         print(i,end=" ")

#9 print number divisible by 3 .
# for i in range(1,11):
#     if i%3==0:
#         print(i,end=" ")

#10 number not divisible by 2 or 3
# for i in range(1,11):
#     if i%2!=0 or i%3!=0:
#         print(i,end=" ")

#11 count how many number from 1 to 100 are divisible by 7.
# count = 1
# for i in range(1,100):
#     if i%7==0:
#         count +=1    
# print("From 1 to 100 are divisible by 7 are : ",count)

#12 print the number from 100 to 1 that are divisible by both 3 and 4.
# for i in range(100,1,-1):
#     if i%3==0 and i%4==0:
#       print(i)

#13 print factorial of number 5.
# fact = 1
# n=5
# for i in range(1,n+1):
#     fact *= i
# print(fact)

#14 print sum of all even number from 1 to 50.
# sum = 0
# for i in range(1,50):
#     if i%2==0:
#         sum += i
# print(sum,end=" ")

#15 print all number between 1 to 100 where the number ends with 7.
# for i in range(1,100):
#     if i%10 == 7:
#         print(i)

#16 Count how many digit from 1 to 100 have dight 5.
# count = 1
# for i in range(1,100):
#     if i % 10 == 5:
#         count +=1
#         print(i,end=" ")
# print(":",count)    

#17 Print reverse of number 123->321
# n = "123"
# rev = n[::-1]
# print(rev)

n = 123
rev = 0
for i in range(n):
    if n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n//=10
print(rev)       

