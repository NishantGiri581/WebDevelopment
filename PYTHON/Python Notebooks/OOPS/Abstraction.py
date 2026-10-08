#Abstraction in object-oriented programming (OOP) is about hiding the
#  complex internal workings of an object and exposing only the essential
#  features or functionalities. Think of it as providing a simplified,
#  high-level view of something, allowing you to use it without needing 
# to know all the messy details of how it works.


"""
Abstract Class: A class that acts as a blueprint.
 It can contain both abstract and concrete (regular) methods.
 You can't create an instance of an abstract class.

Abstract Method: A method declared in an abstract class that
 has no implementation (no code inside). It's essentially a
   contract that says, "any class that inherits from me must
     provide an implementation for this method."

Concrete Class: A regular class that inherits from an abstract
 class and provides an implementation for all of its abstract methods. 
 This is the class you can actually create objects from.
"""

# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius**2

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# circle = Circle(5)
# print(f"Area of the circle: {circle.area()}")
# print(f"Perimeter of the circle: {circle.perimeter()}")



# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# animals = [Dog(),Cat()] 

# for animal in animals:
#     print(animal.sound())



# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         return "Car Start with a key"
    
# class Bike(Vehicle):
#     def start_engine(self):
#         return "Bike Start with a self start"
    
# vehicles = [Car(),Bike()]    
# for v in vehicles:
#     print(v.start_engine())

# bike = Bike()
# print(bike.start_engine())



# from abc import ABC, abstractmethod
# class Payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     def refund(self,amount):
#         pass

# class CreditCardPayment(Payment):
#     def  pay(self,amount):
#         f"Paid ₹{amount} using Credit Card 💳"
#     def refund(self, amount):
#         return f"Refunded ₹{amount} to Credit Card 💳"


# class UPIPayment(Payment):
#     def pay(self, amount):
#         return f"Paid ₹{amount} using UPI 📱"

#     def refund(self, amount):
#         return f"Refunded ₹{amount} to UPI 📱"

# payments = [CreditCardPayment(), UPIPayment()]

# for p in payments:
#     print(p.pay(1000))
#     print(p.refund(500))




"""
from abc import ABC, abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass
    def withdraw(self,amount):
        pass

# Concrete Class 1
class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ₹{amount} in Savings Account. Balance = ₹{self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ₹{amount} from Savings Account. Balance = ₹{self.balance}"
        else:
            return "Insufficient balance in Savings Account."


# Concrete Class 2
class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ₹{amount} in Current Account. Balance = ₹{self.balance}"

    def withdraw(self, amount):
        # Current account allows overdraft up to -₹5000
        if self.balance - amount >= -5000:
            self.balance -= amount
            return f"Withdrew ₹{amount} from Current Account. Balance = ₹{self.balance}"
        else:
            return "Overdraft limit exceeded in Current Account."


# ✅ Usage
savings = SavingsAccount()
current = CurrentAccount()

print(savings.deposit(2000))
print(savings.withdraw(500))
print(savings.withdraw(2000))

print(current.deposit(1000))
print(current.withdraw(4000))
print(current.withdraw(3000))

"""


from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    

circle = Circle(5)
print(f"Area of circle : {circle.area()}")
print(f"Perimeter of the circle: {circle.perimeter()}")


