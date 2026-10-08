# Json is JavaScript Object Notation, It is similar to python dictionaries. 
# It is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
# JSON is often used to transmit data between a server and a web application as text.


# Convert Python dictionary to JSON string
# import json
# user = {
#     "name": "Nishant",
#     "age": 25,
#     "skills": ["Python", "Django", "SQL"]
# }

# json_data = json.dumps(user)  
# print(json_data)
# print(type(json_data)) # Output: {"name": "Nishant", "age": 25, "skills": ["Python", "Django", "SQL"]}


# JSON → Python Dictionary
# import json

# json_data = '''
# {
#     "name": "Nishant",
#     "age": 25,
#     "skills": ["Python", "Django", "SQL"]
# }
# '''

# user = json.loads(json_data)

# print(user)
# print(type(user))



# # Real Backend Example
# import json

# def login(request_body):

#     data = json.loads(request_body)

#     username = data["username"]
#     password = data["password"]

#     print("Username:", username)
#     print("Password:", password)


# request_body = '''
# {
#     "username": "nishant",
#     "password": "12345"
# }
# '''

# login(request_body)