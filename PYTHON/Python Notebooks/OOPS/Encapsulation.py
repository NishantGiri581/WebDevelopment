#Encapsulation: The principle of bundling the data (attributes) and the methods that operate on the data into a single unit (a class). 
# It also involves restricting direct access to an object's components, which is known as data hiding.

#Public: Attributes and methods are public by default. They can be accessed from anywhere.

#Protected: By convention, attributes and methods prefixed with a single underscore (_) are considered "protected."
#  This tells other developers, "You shouldn't modify this directly, but you can if you must."

#Private: Attributes and methods prefixed with a double underscore (__) are considered "private." 
# Python performs "name mangling" to make it very difficult to access them from outside the class.

"""
class BankAccount:
    def __init__(self,owner,starting_balance):
        self.owner = owner
        self.__balance = starting_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}") 
        else:
            print("Insufficient funds.")
            
    def get_balance(self):
        return self.__balance
    
    
my_account = BankAccount("Nishant Giri", 1000)    

print(f"Account Owner: {my_account.owner}")       
my_account.deposit(500)   
my_account.withdraw(200)  
my_account.withdraw(2000)
print(f"Final balance for {my_account.owner}: ${my_account.get_balance()}")
"""

#Create a Car class with a private attribute __fuel_level.
# Add public methods drive() 
# (which reduces fuel) and refuel() (which increases fuel). 
# Ensure the fuel level can never go below 0 or above a max_fuel limit.
# Add a get_fuel_level() method to see the current fuel level.

class Car:
    def __init__(self,max_fuel, initial_fuel=0):
        self.max_fuel = max_fuel
        if 0 <= initial_fuel <= max_fuel:
            self.__fuel_level = initial_fuel
        else:
            self.__fuel_level = 0 
            
    def driver(self, fuel_to_use):
        if fuel_to_use  <= 0:
            print("fuel to use must be a positive number.")     
            return
        
        if self.__fuel_level >= fuel_to_use:
            self.__fuel_level -= fuel_to_use
            print(f"Drove the car, used {fuel_to_use} units of fuel.")
        else:
            print(f"Not enough fuel! You can only drive using {self.__fuel_level} units.")
            self.__fuel_level = 0
            
        print(f"Current Fuel: {self.__fuel_level:.1f}")

    def refuel(self, fuel_to_add):
        """Simulates refueling, which adds fuel to the tank."""
        if fuel_to_add <= 0:
            print("Fuel to add must be a positive number.")
            return
            
        if self.__fuel_level + fuel_to_add > self.max_fuel:
            added = self.max_fuel - self.__fuel_level
            self.__fuel_level = self.max_fuel
            print(f"Tank is full! Could only add {added:.1f} units of fuel.")
        else:
            self.__fuel_level += fuel_to_add
            print(f"Refueled with {fuel_to_add} units.")
            
        print(f"Current Fuel: {self.__fuel_level:.1f}")
        
    def get_fuel_level(self):
        """A public 'getter' method to safely check the current fuel level."""
        return self.__fuel_level

# --- Example Usage ---

# Create a car with a max fuel capacity of 50 units, starting with 10.
my_car = Car(max_fuel=50, initial_fuel=10)
print(f"Car created with {my_car.get_fuel_level()} units of fuel (Max: {my_car.max_fuel}).\n")

# Drive the car
my_car.driver(0)
print("-" * 20)

# Try to drive more than the available fuel
my_car.driver(5)
print("-" * 20)

# Refuel the car
my_car.refuel(30)
print("-" * 20)

# Try to overfill the tank
my_car.refuel(30)
print("-" * 20)

# Check the final fuel level
final_fuel = my_car.get_fuel_level()
print(f"\nFinal check: The car has {final_fuel} units of fuel.")

# Trying to access the private attribute directly will cause an error
try:
    print(my_car.__fuel_level)
except AttributeError as e:
    print(f"\nError received as expected: {e}")
