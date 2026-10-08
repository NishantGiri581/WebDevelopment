#File Handling: It is a way to intract with files on your computer.
# you can create ,read , update, and delete files.

#Opening and Closing of files
# file_object = open("filename.txt", "mode")
# file_object.close()

#mode():-
# "r": Read-only mode. The default mode.

# "w": Write mode. Creates a new file if it doesn't exist or truncates 
# (empties) the file if it does.

# "a": Append mode. Adds new content to the end of the file
#  without erasing the existing content.

# "r+": Read and Write mode. Allows you to both read from and 
# write to the file.


#Reading Method Mode("r")
# file_object = open("file.txt", "r")
# print(file_object)

#Using With
# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)

#single single open file by line
# with open("file.txt","r") as file:
#     line1 = file.read()  
#     print(line1)

#Writing method Mode("w")
# with open("file.txt", "w") as file:
#     file.write("This is Nishant Giri\n")
#     file.write("I am Python Developer")

#Appending 
# with open("file.txt","a") as file:
#     file.write("\nI am FullStack Developer")

# with open("file.txt","r") as file:
#     print(file.read())

# with open("file.txt","r") as file:
#     print(file.readline())   #read single line

# with open("file.txt","r") as file:
#     print(file.readlines())    #read all line


# Example of handling a binary file
# with open("image.jpg", "rb") as binary_file:
#     data = binary_file.read()
#     print(f"Read {len(data)} bytes from the image.")



# import os
# # Create a dummy file to be deleted
# with open("boss.txt", "w") as f:
#     f.write("I will be deleted.")

# # Check if the file exists before attempting to delete it
# if os.path.exists("boss_file.txt"):
#     os.remove("boss_file.txt")
#     print("File deleted successfully.")
# else:
#     print("File does not exist.")