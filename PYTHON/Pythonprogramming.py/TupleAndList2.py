#Lists in python
"""A built in data type that store sets of values
-It can store elements of different types (integer, float,string,etc.)
-List is muitable"""

# marks = [94.4,87.5,95.2,66.4,45.1]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])

"""student = ["Nishant",98.5,"Delhi"]
print(student[0])
student[0]="Boss"
print(student[0])"""
 
#List slicing
#list_name [ starting_idx : ending_idx] #ending index is not included

"""marks=[87,64,33,76,58]
print(marks[1:4])"""

#List Methods
#list.append- add one elements at the end
"""list=[2,1,3]
list.append(6)
print(list)"""

#list.sort- sort in ascending order
"""list=[2,6,4]
list.append(7)
print(list.sort())
print(list)"""

#list.sort(reverse=True)- sorts in descending order
"""list=[6,4,8]
print(list.sort(reverse=True))
print(list)"""

#list.reverse()-reverse the list
"""list=[2,6,4,8]
list.reverse()
print(list)"""

#list.insert(idx,el)- insert elements at index
"""list=[6,8,29]
list.insert(2,5)
print(list)"""

#list.remove()- removes first occurance of elements
"""list=[2,1,3,1]
list.remove(1)
print(list)"""

#list.pop(idx)- remove elements at idx
"""list=[5,3,8,9]
list.pop(2)
print(list)"""

#Tuples in python
"""-It is immutable
-it is built in data type that lets us create immutable sequence of values"""

"""tup=(45,87,99,32,73)
print(type(tup))
print(tup[0])
print(tup[4])"""
#slicing"
"""tup=(1,6,8,9,0)
print(tup[1:3])"""

#Tuple Methods
#tup.index(el)-returns index of first occurance
"""tup=(6,3,7,8)
   print(tup.index(3))"""
#tup.count(el)-count the no. which occurance more 
"""tup=(1,4,4,7,6,9,7)
print(tup.count(7))"""

#Wap to ask the user to enters names of their 3 favorite movies and store them in a list
"""movies=[]
mov1=input("enter 1st movie: ")
mov2=input("enter 2nd movie: ")
mov3=input("enter 3rd movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)"""

#or we can write this same program
"""movies=[]
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2st movie: "))
movies.append(input("enter 3st movie: "))
print(movies)"""

#Wap to check if a list contains a palindrome of elements #Hint:- use copy()method
#[1,2,3,2,1]  [1,"abc","abc",1]
#list1=[1,2,1]
"""list1=["m","a","a","m"]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("Palindrome")
else:
    print("Not palindrome")"""

#Wap to count the number of students with the "A" grade in the following tuple
"""grade=("A","B","D","A","C","A","E","A")
print(grade.count("A")"""

# Store the above values in a list and store them "A" to "D"
"""grade=["A","B","D","A","C","A","E","A"]
grade.sort()
print(grade)"""


#1. Remove Duplicates from a List
# def remove_duplicates(lst):
#     return list(set(lst))
# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]

# def remove_duplicates(lst):
#     seen = set()
#     result = []
#     for i in lst:
#         if i not in seen:
#             result.append(i)
#             seen.add(i)
#     return result
# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4,

#2. Find the Second Largest Element
# def second_largest(lst):
#     unique = sorted(set(lst), reverse=True)
#     return unique[1] if len(unique) > 1 else None
# print(second_largest([4, 1, 9, 9, 3]))  

#3Reverse a List
# def reverse_list(lst):
#     return lst[::-1]
# print(reverse_list([1, 2, 3, 4, 5]))

#4find the Common Elements in Two Lists
# def common_elements(list1, list2):
#     return list(set(list1) & set(list2))
# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]

#5 Flaten a Nested List
# def flatten_list(nested_list):
#     flat_list = []
#     for sub_list in nested_list:
#         for item in sub_list:
#             flat_list.append(item)
#     return flat_list
# print(flatten_list([[1, 2], [3, 4], [5]]))  # Output: [1, 2, 3, 4, 5]

#6 Rotate a List by n Positions
# def rotate_list(lst, n):
#     n = n % len(lst)  # Handle cases where n > len(lst)
#     return lst[-n:] + lst[:-n]
# print(rotate_list([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]

#7Find missing Number in a List
# def find_missing_number(lst, n):
#     total = n * (n + 1) // 2
#     return total - sum(lst)
# print(find_missing_number([1, 2, 4, 5], 5))

#8Count Occurrences of an Element in a List
# def count_occurrences(lst, element):
#     return lst.count(element)
# print(count_occurrences([1, 2, 3, 2, 1, 2], 2))  # Output: 3

#9 Merge Two Sorted Lists into a Single Sorted List
# def merge_sorted_lists(list1, list2):
#     return sorted(list1 + list2)
# print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4,

#10Find intersection and union of Two Lists
# def union_intersection(list1, list2):
#     union =list(set(list1) | set(list2)) 
#     intersection = list(set(list1) & set(list2))  
#     return intersection, union      
# print(union_intersection([1, 2, 3], [2, 3, 4]))  # Output: ([2, 3], [1, 2, 3, 4])

#1 check two tuples are equal or not
# def are_tuples_equal(tup1, tup2):
#     return tup1 == tup2
# print(are_tuples_equal((1, 2, 3), (1, 2, 3)))  # Output: True
# print(are_tuples_equal((1, 2), (1, 2, 3)))  # Output: False   

#2 Convert List of Tuples to Dictionary
# pairs = [('a', 1), ('b', 2), ('c', 3)]
# def list_of_tuples_to_dict(pairs):
#     return dict(pairs)
# print(list_of_tuples_to_dict(pairs))  # Output: {'a': 1, 'b': 2, 'c': 3}

#3 Find Max and Min in a List Without Built-in Functions
# def find_max_min(lst):
#     min_val = lst[0]
#     max_val = lst[0]
#     for num in lst:
#         if num < min_val:
#             min_val = num
#         if num > max_val:
#             max_val = num
#     return min_val, max_val
# print(find_max_min([3, 1, 4, 1, 5, 9]))  # Output: (1, 9)

#4Remove Duplicates from a Tuple
# def remove_duplicates_from_tuple(tup):
#     return tuple(set(tup))
# print(remove_duplicates_from_tuple((1, 2, 2, 3, 4, 4, 5)))  # Output: (1, 2, 3,

#5sort a Tuple of Tuples Based on the Second Element
# def sort_tuple_of_tuples(tup):
#     return tuple(sorted(tup, key=lambda x: x[1]))
# print(sort_tuple_of_tuples(((1, 3), (2, 1), (3, 2))))  # Output: ((2, 1), (3,2), (1, 3))

#6Find All Pairs in a List That Sum to a Target
# def find_pairs_with_sum(lst, target):
#     pairs = []
#     seen = set()
#     for num in lst:
#         complement = target - num
#         if complement in seen:
#             pairs.append((complement, num))
#         seen.add(num)
#     return pairs
# print(find_pairs_with_sum([1, 2, 3, 4,    5], 5))  # Output: [(2, 3), (1, 4)]     

#7Nested Tuple Unpacking
# def unpack_nested_tuple(nested_tup):
#     a, (b, c), d = nested_tup
#     return a, b, c, d
# print(unpack_nested_tuple((1, (2, 3), 4)))

#8 check if a list is palindrome
# def is_palindrome(list):
#     return list == list[::-1]
# print(is_palindrome([1, 2, 3, 2, 1]))   

#9 find the frequency of the most common element in a list
# def most_common_frequency(lst):
#     frequency = {}
#     for item in lst:
#         frequency[item] = frequency.get(item, 0) + 1          
#     return max(frequency.values())
# print(most_common_frequency([1, 2, 2, 3, 3, 3, 4]))  # Output: 3  

#10Convert a List into Chunks of Size N
# def chunk_list(lst, n):
#     return [lst[i:i + n] for i in range(0, len(lst), n)]
# print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))  # Output: [[1, 2, 3], [4, 5, 6], [7]]    