#Recursion- when a function call itself repeatedly.
#print n to 1 backwards.

# def show(n):
#     if(n==0):
#          return
#     print(n)
#     show(n-1)
# print("end")
# show(5)

#return n! 
"""def fact(n):
    if(n==0 or n==1):
        return 1
    else:                     :- n! = (n-1)*n
        return n * fact(n-1)  :- this is recursive of factorial.
    
print(fact(4))"""

#Write a recursive function to calculate the sum of first n natural number.
"""def calc_sum(n):
    if(n==0):
        return 0
    print(n)
    return calc_sum(n-1) + n

sum= calc_sum(10) 
print(sum)"""

#Write a recursive function to print all elements in a list.
#Hint: use list and index as parameter.

"""def print_list(list, idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","apple","banana","orange"]  
print_list(fruits)"""
