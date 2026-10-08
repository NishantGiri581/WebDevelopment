# Dictionary in python
"""-It is used to store data values in key:value pairs.
-They are unordered , mutable(changeable) and don't allow dupilicate keys"""

"""info = {
    "name" : "nishant",
    #list and tuple can be store
    "subject" : ["python","hindi"],
    "class" : (2,3,4,6,8,9),
    "key" : "values",
    "learn" : "coding",
    "age" : 22,
    #keys can be integer but list and tuple cannot
    12 : 877,
    "is_adult" : True
}
print(type(info))
#dict["  "]
print(info["class"])
print(info["learn"])

#assigned another value in key , values change into Nishant
info["key"]= "Nishant"
print(info)

#keys value add 
info["surname"] = "Giri"
print(info)
# add null_dict {}
null_dict ={}
null_dict["name"]="values"
print(null_dict)"""


# Nested dictionary
"""if-else
if():
    if()"""

"""student = {
    "name" : "Nishant",
    "subject": {
        "phy" : 97 ,   
        "chem" : 76 ,
        "math" : 82 
    }
}
print(student["subject"]["chem"])"""

#Dictionary methods
#myDict.key()- returns all keys of outer layers

"""student = {
    "name" : "Nishant",
    "subject": {
        "phy" : 97 ,   
        "chem" : 76 ,
        "math" : 82 
    }
}"""

#print(len(list(student.keys())))

#myDict.values- returns all the values
#print(student.values())

#myDicttems()-returns of all pairs
"""print(list(student.items()))
pairs= list(student.items())
print(pairs[0])"""

#myDict.get("keys")- returns the keys according to values
#print(student.get("subject"))

#myDict.update(newDict)-insert the specified items to the dictionary
"""new_dict={"city" : "Delhi"}
student.update(new_dict)
print(student)"""


#Sets in Python 
"""Sets is the collection of unorderd items.
Sets is mutable But
Each elements in the sets must be unique and immutable(not changeable).
List and Tuples does not stored in set.
Dublicate items are stored once"""

"""Collection={1,2,3,4,"Hello"}
print(Collection)
print(type(Collection))
print(len(Collection))#Total number of items"""

#Empty sets
"""collection={}
print(type(collection))"""

#Set Method
#set.add(el)
"""collection=set()
collection.add(1)
collection.add(2)
collection.add("Nishant")
collection.add((19,2,5,6))
#collection.remove(2)
#collection.clear()
print(len(collection))"""

"""collection={"Nishant","Apnacollege","Python","Boss"}
print(collection.pop())"""

#set.union() combine both set and return new
#set.intersection() only common elements are print
"""set1={1,2,3,4}
set2={3,2,4,5}
print(set1.union(set2))
print(set1.intersection(set2))"""
 
 #practice question
""" Store following word meanings in python dictionaries
table: "a piece of furniture", "list of facts and figures" 
cat : " a small animals" """

"""dictionary={
    "cat": " a small animals",
    "table": ["a piece of furniture","list of facts and figures"]
}
print(dictionary)"""

"""subject={"python","c++","java","c","python","java","c","javascript","html" }
print(len(subject))"""

#Wap to enter marks of 3 subjects from the users and store them in dctionary .
#starts with an empty dictionary and add one by one . use subject name as key and marks as value .
"""marks = {}
x = int(input("enter phy : "))
marks.update({ "phy" :x })

y = int(input("enter math : "))
marks.update({ "math" :x })

z = int(input("enter chem : "))
marks.update({ "chem" :x })

print(marks)"""


#Find frequency of elements using dictionary
# def frequency_of_elements(s):
#     freq = {}
#     for char in s:
#         if char in freq:
#             freq[char] += 1
#         else:
#             freq[char] = 1
#     return freq 
# print(frequency_of_elements("banana"))  # Output: {'a': 3, 'b': 2, 'c': 1}

#find duplicate elements in a list using dictionary
# def find_duplicates(lst):
#     seen = set()
#     duplicates = set()
#     for item in lst:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)
#     return list(duplicates) 
# print(find_duplicates([1, 2, 3, 2, 1, 4, 5]))  # Output: [1, 2]

#Merge two dictionaries using dictionary comprehension
# def merge_dicts(dict1, dict2):
#    return {**dict1, **dict2}

# print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  # Output: {'a': 1, 'b': 3, 'c': 4}

#check if two strings are anagrams using dictionary
# def is_anagram_dict(s1,s2):
#     freq = {}
#     for c in s1:
#       freq[c] = freq.get(c,0) + 1
#     for c in s2:
#       freq[c] = freq.get(c,0) - 1
#     return all(value == 0 for value in freq.values())
# print(is_anagram_dict("listen", "silent"))  # Output: True  
    

# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)
# print(is_anagram("listen", "silent"))  # Output: True   

#find the first non-repeating character in a string using dictionary
# def non_repeating_char(s):
#     freq = {}
#     for c in s:
#         freq[c] = freq.get(c, 0) + 1
#     for c in s:
#         if freq[c] == 1:
#             return c
#     return None
# print(non_repeating_char("swiss"))  # Output: 'w'

#invert a dictionary (swap keys and values) using dictionary comprehension
# def invert_dict(d):
#     return {v: k for k, v in d.items()}
# print(invert_dict({'a': 1, 'b': 2, 'c': 3}))  # Output: {1: 'a', 2: 'b', 3: 'c'}

#Find Common Elements Between Two Lists Using Sets
# def common_elements(list1, list2):
#     return list(set(list1) & set(list2))
# print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  # Output: [3, 4]    