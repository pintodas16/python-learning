class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'Name {self.name}, Age {self.age}')

alice = Person('Alice',25)
alice.display_info()


# car speed controller 
class Car:
    def __init__(self,brand,speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self,amount):
        self.speed= self.speed + amount
        print(f'increase the speed by {self.speed}')

    def brake(self,amount):
        if self.speed <=0 or self.speed - amount <=0:
            return 
        self.speed = self.speed - amount
        print(f'decrease the speed by {self.speed}')
    
    def display_speed(self):
        print(f'Current speed is {self.speed}')

bmw = Car('BMW')

bmw.accelerate(20)
bmw.brake(30)
bmw.display_speed()



# Student and course Relationship 
class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def __str__(self):
        return f'{self.name} (Id:{self.id})'

class Course(Student):
    
    def __init__(self, course_name):
        self.course_name = course_name
        self.students_list =[]
    
    def add_student(self,student_obj):
        self.students_list.append(student_obj)
    
    def list_students(self):
        print(f'students  in {self.course_name}')
        for student in self.students_list:
            print(f" - {student}")



# Testing the classes
s1 = Student("Alice", "S101")
s2 = Student("Bob", "S102")

course = Course("Python Programming")
course = Course("java Programming")

course.add_student(s1)
course.add_student(s2)

course.list_students()


# 5. Bank Account
# Goal: Practice encapsulation and method access.

class BankAccount:
    def __init__(self,acount_holder,balance=0):
        self.account_holder = acount_holder
        self._balance = balance
    
    def deposit(self,amount):
        self._balance +=amount
        print(f'In your account creatied amount is {self._balance}')
    
    def withdraw(self,amount):
        if(self._balance - amount < 0) :
            print(f'You have not enough money to withdraw. your current balance is {self._balance}')
            return 
        self._balance -= amount
        print(f"yor withdrawl ${amount} from your account. you'r current balance is ${self._balance}")
    def get_balance(self):
        print(f"your current balance is ${self._balance}")
        
        
p1 = BankAccount('person One')
p1.deposit(500)
p1.withdraw(700)
p1.get_balance()

p2 = BankAccount('person two')
p2.deposit(500)
p2.withdraw(500)
p2.get_balance()


# 6. Inheritance - Shape Classes
# Goal: Practice inheritance.
import math
class Shape:
    
    def area(self):
        raise NotImplementedError("Subclasses must override area() method")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width  * self.height
    
rect = Rectangle(5, 4)
print("Rectangle area:", rect.area())   # Output: 20

circle = Circle(3)
print("Circle area:", circle.area())   # Output: 28.27...