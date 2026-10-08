#File I/O :- Python can be used to perform operation on a file.(read,write data)
#Types of all files
#1 Text Files : .txt , .docx , .log , etc.
#2 Binary Files : .mp4 , .mov , .png , .jpeg , etc

#operation 1 open,read and close file
"""we have to open a file before reading or writing."""
# f = open("file_name","mode")

#Open the loops file 

# f=open("/Users/nishantgiri/Desktop/Pythonprogramming.py/loops4.py","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

#line wise read
"""f=open("/Users/nishantgiri/Desktop/Pythonprogramming.py/loops4.py","r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close()"""

#Character and their meaning
"""   
'r' - open for reading.
'w' - open for writing.
'x' - create a new file and open for writing.
'a' - open for writing , append to the end of the file if it exists.
'b' - binary mode.
't' - text mode.
'+' - open a desk file for updating(reading and writing). 
'r+' - read and overwrite (ptr start) and no truncate.
'w+' _ read and overwrite and truncate.
'a+' - read and append (ptr end) and no truncate.
"""

#Writing to a file
"""f=open("demo.txt","r+")

f.write("you are my love")

f.close()"""

#With syntax
"""with open ("demo.txt","r") as f:
    data = f.read()
    print(data)"""

"""with open("demo.txt","w")as f:
    data=f.write("i am hero")"""

#Deleting a file :- using the os module.
#Module (like a library) is a file written by another programmer that generally has a function we can use.

"""import os
os.remove("demo.txt")"""

#Create a new file "practice.txt" using python. Add the following data in it:
"""
Hi everyone
we are learning file I/O
using java
i like programming i java. 
"""
"""with open("practice.txt","w")as f:
    f.write("Hi everyone\nwe are learning file I/O\nusing java\ni like programming i java.")"""

#Write a function that replace all occurances of "java" with "python" in above file
"""with open("practice.txt", "r")as f:
    data=f.read()

new_data = data.replace("java","Python")
print(new_data)

with open("practice.txt", "w")as f:
    f.write(new_data)"""

# Search if the word "learning" exists in the file or not. using function
"""def check_for_word():
    word="learning"
    with open("practice.txt","r")as f:
     data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

check_for_word() """

#WAF to find in which line of the file does the word "learning" occurs first.
# print -1 if word not found

"""def check_for_word():
    word="learning"
    with open("practice.txt","r")as f:
     data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")"""

"""def check_for_line():
    word="learning"
    data = True
    line_no = 1
    with open("practice.txt","r")as f:
        while data:
          data=f.readline()
          if(word in data) :
              print(line_no)
              return
          line_no +=1     

    return -1
print(check_for_line())"""

#From a file containing numbers separated by comma , print the count of even number.
"""count = 0
with open("practice.txt","r")as f:
    data=f.read()

    nums=data.split(",")
    for val in nums :
        if (int(val) %2 ==0) :
            count +=1
print(count)    """        