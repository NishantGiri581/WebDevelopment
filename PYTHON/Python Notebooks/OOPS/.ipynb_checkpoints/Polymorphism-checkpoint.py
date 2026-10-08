#Polymorphism: This big word comes from Greek and means "many shapes." 
# In programming, it's the ability of an object to take on many forms. 
# The most common use of polymorphism in OOP is when a parent class reference is used to refer to a child class object.


class Circle:
    def draw(self):
        print("Drawing a circle: O")

class Square:
    def draw(self):
        print("Drawing a square: []")

class Triangle:
    def draw(self):
        print("Drawing a triangle: A")

# --- Let's draw some shapes ---

# Create a list of different shape objects
shapes = [Circle(), Square(), Triangle(), Square()]

# This loop doesn't care what type of object is in the list.
# It only cares that each object has a .draw() method. This is polymorphism!
for shape in shapes:
    shape.draw()

# Expected output:
# Drawing a circle: O
# Drawing a square: []
# Drawing a triangle: A
# Drawing a square: []


class FileLogger:
    def log(self,message):
        print(f"Logging '{message}' to the file.")
               
class ConsoleLogger:
    def log(self,message):
        print(f"Logging '{message}' to the console")
        
class DatabaseLogger:
    def log(self,message): 
        print(f"Logging '{message}' to the database")        
        
# --- 2. Demonstrate Polymorphism ---

# Create a list containing an instance of each logger class
loggers = [
    FileLogger(),
    ConsoleLogger(),
    DatabaseLogger()
]        


# Define a sample message
sample_message = "User logged in successfully."

print("--- Initiating logging process ---")
for logger in loggers:
    logger.log(sample_message)
print("--- Logging process complete ---")