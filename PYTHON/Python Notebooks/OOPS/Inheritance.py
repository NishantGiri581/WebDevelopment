# Inheritance: The mechanism by which one class (the child or subclass) 
#              can inherit the attributes and methods from another class (the parent or superclass).
#              This promotes code reuse. The relationship is an "is-a" relationship (e.g., a Golden Retriever is a Dog).

# Method Overriding: A child class can provide its own specific implementation of a method
#  that is already defined in its parent class.

# super(): A function that gives you access to methods in a parent class. 
# It's commonly used to call the parent's __init__ method from the child's __init__ method.
"""
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Generic Sound")   

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(self,species = "Dog")
        self.breed = breed

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(self,species = "Cat")
        self.color = color
    
    def make_sound(self):
        print("Meow!")

my_animal = Animal("Creature","Unknown") 
my_dog = Dog("Buddy","German Retriever") 
my_cat = Cat("Whiskers","Gray")

my_animal.make_sound()
my_dog.make_sound() 
my_cat.make_sound()

print(f"{my_dog.name} is a {my_dog.species} of breed {my_dog.breed}.")

"""


#Create a Person parent class with name and age attributes. 
# Then, create a Student child class that inherits from Person. 
# The Student class should also have a student_id attribute.

# The Parent Class (Superclass)
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")


# Create an instance of the Student class
student1 = Student("Nishant", 23, "581")

# Call the method to display the student's information
# This will call the overridden method in the Student class
student1.display_info()

# You can still access all attributes directly
print(f"\nStudent's Name: {student1.name}")
print(f"Student's Age: {student1.age}")
print(f"Student's ID: {student1.student_id}")   
 
"""
