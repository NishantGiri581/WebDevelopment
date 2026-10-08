# The __init__ Method: This is a special method, often called a constructor.
#  It gets called automatically whenever you create a new object from a class.
#  Its primary job is to set up the object's initial state by assigning values to its instance attributes.

# self: This keyword is a reference to the current instance of the class. 
# It is used to access variables that belong to the class.
#  You must include it as the first parameter in any method definition.

# Instance Attributes: These are attributes that are specific to each object.
#  A dog's name and age are instance attributes because your dog's name and age are different from my dog's.
#  They are defined inside the __init__ method using self.

class Dog:
    # Class attribute (shared by all)
    species = "Canis familiaris"

    # The constructor method
    def __init__(self, name, age):
        # These are instance attributes (unique to each object)
        self.name = name
        self.age = age
        print(f"A new dog named {self.name} has been created!")

    # An instance method
    def bark(self):
        print(f"{self.name} says Woof!")

    # Another instance method
    def describe(self):
        # We use 'self' to access the instance attributes
        return f"{self.name} is {self.age} years old."

# --- Let's use our improved blueprint ---

# When we create an object, Python automatically calls __init__
# We pass the arguments 'name' and 'age'
dog1 = Dog("Buddy", 4)  # Output: A new dog named Buddy has been created!
dog2 = Dog("Lucy", 2)   # Output: A new dog named Lucy has been created!

# Call methods on our unique dog objects
dog1.bark()  # Output: Buddy says Woof!
dog2.bark()  # Output: Lucy says Woof!

# Access their unique instance attributes
print(dog1.describe()) # Output: Buddy is 4 years old.
print(dog2.describe()) # Output: Lucy is 2 years old.