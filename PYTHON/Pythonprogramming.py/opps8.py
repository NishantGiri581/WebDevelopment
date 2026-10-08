#Opp in python :- to map with real world senerios, we started in objects in code.
#This is called object oriented programming.

#Class and Object in python 

# Class is a blueprint for creating objects.
   #Creating class
"""class Student:
    name="Nishant"

    #creating object(instance)
s1 = Student()
print (s1.name)        
s2=Student()
print(s2.name)"""

"""class Car:
    color="red"
    brand="oddi" 
car1=Car()
print(car1.color)    
print(car1.brand)"""

#Constructor Function or __init__function
#:- All classes have a function called __init__(), which is always executed when 
# the object classes being initiated.

"""class Student:
  
    def __init__(self,fullname , marks):
        self.name=fullname
        self.marks=marks
        

s1=Student("Nishant",76)
print(s1.name, s1.marks)

s2=Student("Mohan",98)
print(s2.name,s2.marks)"""

#Class & Instance attributes
"""class Student:
    college_name= "Sanskar college"

    def __init__(self,fullname , marks):
        self.name=fullname
        self.marks=marks
        print("adding new student in database..")

s1=Student("Nishant",76)
print(s1.name, s1.marks)

s2=Student("Mohan",98)
print(s2.name,s2.marks)

print(Student.college_name)"""

#Methods :- Method are functions that belong to objects.
#creating class
"""class Student:
    def __init__(self,fullname):
        self.name=fullname

    def hello(self):
        print("hello",self.name) """   
#creating objects
# s1=Student("Nishant")
# s1.hello()        

"""class Student:
    college_name= "Sanskar college"

    def __init__(self,fullname , marks):
        self.name=fullname
        self.marks=marks
       
    def welcome(self):
        print("welcome student",self.name)

    def get_marks(self):
        return self.marks
    
s1=Student("Nishant",76)
s1.welcome()
print(s1.get_marks())"""

#create student class that takes name and marks of 3 subjects as arguments in constructors.
#then create a method to print the average'

"""class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum +=val
        print("hi",self.name,"your avg score is:",sum/3)    

s1=Student("Tony",[66,87,90])        
s1.get_avg()

s1.name="ironeman"
s1.get_avg()"""

#Static methods:- Methods that don't use the Self parameter (work at class level)

"""class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @staticmethod #decorator 
    def hello():
        print("hello")    

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum +=val
        print("hi",self.name,"your avg score is:",sum/3)    

s1=Student("Tony",[66,87,90])        
s1.get_avg()
s1.hello()"""

#Important of OOP
#Abstraction:- Hiding the implementation details of a class and only showing the essential features to the user
"""class Car:
    def __init__(self):
        self.acc= False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True #unessesary things hide
        self.acc=True    #unessesary things hide
        print("car started..")   #showing essential features 

car1=Car()
car1.start()"""

#Encapsulation:- Wrapping data and the function into a single unit(objects).


#Create account class with 2 attributes - balance and account no.
#Create methods for debit , credit and printing the balance

"""class Account():
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    #Debit
    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount,"was debited")
        print("total balance = ", self.get_balance())

    #Creadit
    def credit(self,amount):
        self.balance += amount
        print("Rs",amount,"was credit")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=Account(10000, 12345)
acc1.debit(1000) 
acc1.credit(500)  
acc1.credit(20000)
acc1.debit(10000)"""

#Del Keyword:- Used to delete object properties or object itself.
"""class Student:
    def __init__(self,name):
        self.name=name

s1=Student("Nishant")
print(s1.name)

del s1.name
print(s1.name)"""

#Private(like) attributes and method
      #Conceptual implementation in python
#Private attributes and methods are meant to be used only within the class and are not accessible from the class.

"""class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)



acc1 =Account("12123",8746)        

print(acc1.acc_no)
print(acc1.reset_pass)"""


#example for private the attributes 
"""class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person! ")

    def welcome(self):
        self.__hello()    

p1=Person()
print(p1.welcome())"""  

#Inheritance:- When one class(child/derived) derives the properties and method of another class(parent/base).

"""class Car:
    color="black"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")

class Toyotacar(Car):
    def __init__(self,name):
        self.name=name

car1=Toyotacar("Fortuner")
car2=Toyotacar("suzuki")

print(car1.color,car1.name,car1.stop())"""

#Types of Inheritance
"""
#Single Inheritance :- derived class inherit the base class."""
#Multilevel Inheritance:- the properties of base and derived class inherit by another derived class.
"""class Car:
   
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")

class Toyotacar(Car):
    def __init__(self,brand):
        self.name=brand

class Fortuner(Toyotacar):
    def __init__(self, type):
        self.type=type

car1=Fortuner("diesel")
car1.start() """        

#Multiple Inheritance:-derived class inherit multiple base class
"""class A:
    varA="welcome to class A"
class B:
    varB="welcome to claas B"

class C(A,B):
    varC="welcome to class C"

c1=C()
print(c1.varC)
print(c1.varA)
print(c1.varB) """

#Super Method :-super()method is used to access method of the parent class.

"""class Car:
    def __init__(self, type):
        self.type=type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")

class Toyotacar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()


car1=Toyotacar("Nishant","electric")        
print(car1.type)
print(car1.stop())"""

#class method
"""A class method is bound to the class and receives the class as an implicit first argument.
- note- static method can't access or modify class state and generally for utility .
"""
"""class Person:
    name="anonymous"

    #def changename(self,name):
       # Person.name=name #class name change
        #self.__class__.name="Boss"

    @classmethod #decorater 
    def changename(cls,name):
        cls.name=name    

p1=Person()
p1.changename("Boss")
print(p1.name)   
print(Person.name) """

#Property 
"""class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        #self.percentage=str((self.phy + self.chem + self.math)/3)+ "%"
    
    #def calcpercentage(self):
        #self.percentage=str((self.phy + self.chem + self.math)/3)+ "%"  use to normal calculate the percentage.
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3)+ "%"
    
stu1=Student(76,48,89)        
print(stu1.percentage)

stu1.phy = 67 
print(stu1.percentage)"""

#Polymorphism:- Operator Overloading 
#When the same operator is allowed to have different meaning according to the context .

#Operator and Dunder function 
"""
:- a+b     #addition              a.__add__(b)
:- a-b     #subtraction           a.__sub__(b)
:- a*b     #multiplication        a.__mul__(b)
:- a/b     #division              a.__truediv____(b)
:- a%b     #modulation            a.__mod____(b) 
"""


#All of these are implicit overloading
"""
#print(1+2) #3
#print(type(1))

#print("apna"+"college") #Concatenate
#print(type("apna"))

#print([1,2,3]+[4,5,6]) #merge
#print(type([1,2,3]))
"""
#Complex number 
"""1i real + 2j imagenary
   3i      + 5j  
"""
#addition
"""class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img 

    def shownumber(self):
        print(self.real,"i",self.img,"j")  
       
    def __add__(self,num2):    #__add__ used here  
        newreal=self.real + num2.real
        newimg=self.img + num2.img
        return Complex(newreal,newimg) 

num1=Complex(1,3) 
num1.shownumber() 

num2=Complex(4,6)   
num2.shownumber()

num3=num1 + num2
num3.shownumber()

#num3=num1.add(num2)
#num3.shownumber()"""

#subtraction
"""class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img 

    def shownumber(self):
        print(self.real,"i",self.img,"j")  
       
    def __sub__(self,num2):    #__sub__ used here  
        newreal=self.real - num2.real
        newimg=self.img - num2.img
        return Complex(newreal,newimg) 

num1=Complex(1,3) 
num1.shownumber() 

num2=Complex(4,6)   
num2.shownumber()

num3=num1 - num2
num3.shownumber()"""

#Multiplication
"""class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img 

    def shownumber(self):
        print(self.real,"i",self.img,"j")  
       
    def __mul__(self,num2):    #__mul__used here  
        newreal=self.real * num2.real
        newimg=self.img * num2.img
        return Complex(newreal,newimg) 

num1=Complex(1,3) 
num1.shownumber() 

num2=Complex(4,6)   
num2.shownumber()

num3=num1 * num2
num3.shownumber()"""


#Division
"""class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img 

    def shownumber(self):
        print(self.real,"i",self.img,"j")  
       
    def __truediv__(self,num2):    #__truediv__used here  
        newreal=self.real / num2.real
        newimg=self.img / num2.img
        return Complex(newreal,newimg) 

num1=Complex(1,3) 
num1.shownumber() 

num2=Complex(4,6)   
num2.shownumber()

num3=num1 / num2
num3.shownumber()"""

#Modulation
"""class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img 

    def shownumber(self):
        print(self.real,"i",self.img,"j")  
       
    def __mod__(self,num2):    #__mod__used here  
        newreal=self.real % num2.real
        newimg=self.img % num2.img
        return Complex(newreal,newimg) 

num1=Complex(1,3) 
num1.shownumber() 

num2=Complex(4,6)   
num2.shownumber()

num3=num1 % num2
num3.shownumber()"""

#1:-#Define a circle class to create a circle with radius r using the constructor.
    #define area() method of the class which calculate the area of the circle.                             pie r square
    #define a perierimeter() method of the class which allow you to calculate the parameter of the circle.    2 pie r
"""class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7) * self.radius ** 2    
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1= Circle(21)
print(c1.area())
print(c1.perimeter())"""

  
#2:-#Define a employee class with attributes role, departments and salary. This class also showdetail()method.
    #create an engineer class that iherits properties from employee and has additional attributes : name and age



"""class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showdetails(self):
        print("role =",self.role)  
        print("dept =",self.dept)
        print("salary =",self.salary)
    
class Engineer(Employee):
    def __init__(self,name,age):
           self.name=name
           self.age=age 
           super().__init__("Engineer","IT","75,000")


engg1 = Engineer("Elone mask", "45")           
engg1.showdetails()"""
