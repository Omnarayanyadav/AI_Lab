
# WAP to check if an input number is odd or even
def number(num):
     if num%2==0:
         return "EVEN"
     else:
         return "ODD"
num=int(input("Enter a number: "))
print("The number is: ",number(num))


# WAP to input the percentage and display the division
percentage=float(input("Enter the percentage:"))
if percentage>=80:
    print("Distinction")
elif percentage>=65:
    print("First Division")
elif percentage>=55:
    print("second Division")
elif percentage>=40:
    print("Third Division")
else:
    print("Fail")
    
    
# WAP to calculate sum, diff, product and quotient between two input numbers using a single function.

def arithmetic(x,y):
    add=x+y
    diff=x-y
    product=x*y
    if y==0:
        quotient="Undefined"
    else:
        quotient=x/y
    return add,diff,product,quotient
x=float(input("Enter the first number: "))
y=float(input("Enter the second number: "))
print("addition= ",sum)
add,diff,product,quotient=arithmetic(x,y)
print("diff= ",diff)
print("Product= ",product)
print("Quotient= ",quotient)
# WAP to display prime numbers from 1 to 100
for i in range(1,101):
    is_prime=True
    if i<2:
        is_prime=False
    else:
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
    if is_prime:
        print(i)
    

# WAP to enter the marks of 10 students and display it

def data():
    student_data = []
    #name and marks of 10 students.
    for i in range(1, 11):
        names = input(f"Enter name of student {i}: ")
        marks = float(input(f"Enter marks for {names}: "))
        student_data.append((names, marks))
    
    # Display the entered data
    print("\nEntered data for 10 students:")
    for i, (names, marks) in enumerate(student_data, start=1):
        print(f"Student {i}: Name: {names}, Marks: {marks}")

if __name__ == "__main__":
    data()
# WAP to calculate the factorial of an input number.

n=int(input("Enter the number: "))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
    
print("Factorial is: ",fact)
# WAP to ask for a sentence and count the number of words.
sentence=input("Enter a sentence: ")
words=sentence.split()
count=len(words)
print("The number of words in the sentence is:",count)
# WAP to sort the list {5, 4, 11, 13, 51}
def sort_list(list):
    list.sort()
    return list

list1 = [5, 4, 11, 13, 51]

sorted_list = sort_list(list1)
print("Sorted list:", sorted_list)
# WAP program to sum all the items in a list.
def sum_list(list):
    total = 0
    for item in list:
        total += item
    return total

listA = [5, 4, 11, 13, 51,67,98,500]

list_sum = sum_list(listA)

print("Sum of all items in the listA is: ", list_sum)

# WAP program to get the largest number from a list.
my_list=[11,450,988,76,33,95,120,488,677,577,905,710,880]
largest=max(my_list)
print("Largest number in the list is: ",largest)
# WAP to ask for a sentence and calculate the frequency of characters in the sentences.
sentence=input("Enter a sentence: ")
frequency={}
for char in set(sentence):
    count=sentence.count(char)
    frequency[char]=count
print("Frequency of characters: ")
for char,count in frequency.items():
    print(char,":",count)

# WAP to find the sum of all items in a dictionary
def sum_dict(dict):
    total_sum=sum(dict.values())
    return total_sum
dict1={'a':100,'b':200,'c':300}
dict2={'x':25,'y':18,'z':45}
print("Input1:",dict1)
print("output1:",sum_dict(dict1))
print("Input2:",dict2)
print("Output2:",sum_dict(dict2))

# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
string=input("Enter a string: ")
swapped_str=string.swapcase()
print("swappedcase string is:",swapped_str)
# Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle():
    def __init__(self,r):
        self.radius=r
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
    
r=float(input("Enter the radius of the circle:"))
newcircle=Circle(r)
print("Area of Circle is:",newcircle.area())
print("Perimeter of circle is:",newcircle.perimeter())
    
    
# Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age

from datetime import date,datetime
class Person():
    def __init__(self,name,country,date_of_birth):
       self.name=name
       self.country=country
       self.date_of_birth=datetime.strptime(date_of_birth,"%Y-%m-%d").date()
    
    def calc_age(self):
        today=date.today()
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age = today.year - self.date_of_birth.year - 1
        else:
            age = today.year - self.date_of_birth.year
        
        # Calculate remaining months and days
        if today.month < self.date_of_birth.month or (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            months = (12 - self.date_of_birth.month) + today.month - 1
        else:
            months = today.month - self.date_of_birth.month
        
        # Calculate remaining days
        if today.day < self.date_of_birth.day:
            days = (date(today.year, today.month - 1, self.date_of_birth.day) - date(today.year, today.month - 1, today.day)).days
        else:
            days = today.day - self.date_of_birth.day

        return age, months, days
    
name=input("Enter your name:")
country=input("Enter your country name:")
date_of_birth=input("Enter your date of birth (YYYY-MM-DD): ")

person=Person(name,country,date_of_birth)

print("Name:",person.name)
print("Country:",person.country)
print("Date of birth:",person.date_of_birth)
age,months,days=person.calc_age()
print("Age:",age,"Years",months,"Months",days,"Days")
# Define a class Vehicle with attributes make and model, and a method drive() which prints "Driving the [make] [model]". Then, create a subclass Car that inherits from Vehicle and overrides the drive() method to print "Driving the [make] [model] car"
class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def drive(self):
        print(f"Driving the {self.make} {self.model}")
    
class Car(Vehicle):
    def drive(self):
        print(f"Driving the {self.make} {self.model} car")
                  
                  
vehicle=Vehicle("Toyota","Fortuner")
car=Car("Mercedes-Benz", "A-Class Limousine")
                  
vehicle.drive()
car.drive()
                  
# Create a class BankAccount with private attributes balance and account_number.Implement methods deposit() and withdraw() to modify the balance. Ensure that the balance cannot be accessed directly from outside the class
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Amount Deposited is: Rs {amount} \nYour New balance is: Rs {self.__balance}")
        else:
            print("Deposit amount must be positive!!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Amount Withdrawn is: Rs {amount}.\nYour New balance is: Rs {self.__balance}")
            else:
                print("Insufficient balance!!!")
        else:
            print("Withdrawal amount must be positive!!")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

if __name__ == "__main__":
    account = BankAccount("123456789111519", 5000)
    # what user would like to do:
    while True:
        action = input("Would you like to Deposit or Withdraw?\nEnter d for deposit and w for withdrawal (d/w): ").strip().lower()
        if action == 'd':
            amount = float(input("Enter amount to be deposited: "))
            account.deposit(amount)
        elif action == 'w':
            amount = float(input("Enter amount to be withdrawn: "))
            account.withdraw(amount)
        else:
            print("Invalid action. Please enter 'd' to deposit or 'w' to withdraw.")

        # Display the current balance:
        print(f"Account balance: {account.get_balance()}")

        # Ask if the user wants to perform another transaction
        continue_action = input("Do you want to perform another transaction? (yes/no): ").strip().lower()
        if continue_action != 'yes':
            print("THANK YOU FOR USING OUR SYSTEM.")
            break

# Implement a class Shape with a method area() which returns 0. Then, create subclasses Rectangle and Circle. Overload the area() method in both subclasses to calculate and return the area of a rectangle and a circle respectively.

import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

# Taking input from user for rectangle
width = float(input("Enter width of the rectangle: "))
height = float(input("Enter height of the rectangle: "))
rectangle = Rectangle(width, height)
print("Area of rectangle:", rectangle.area())

# Taking input from user for circle
radius = float(input("Enter radius of the circle: "))
circle = Circle(radius)
print("Area of circle:", circle.area())

# Define classes Engine, Wheel, and Car. Engine and Wheel classes have attributes type and methods start() and stop(). The Car class should have instances of Engine and Wheel classes as attributes. Implement a method start_car() in the Car class which starts the engine and prints "Car started".
class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        print(f"{self.type} Engine started.")

    def stop(self):
        print(f"{self.type} Engine stopped.")


class Wheel:
    def __init__(self, type):
        self.type = type

    def start(self):
        print(f"{self.type} wheel started.")

    def stop(self):
        print(f"{self.type} wheel stopped.")


class Car:
    def __init__(self, engine_type, wheel_type):
        self.engine = Engine(engine_type)
        self.wheel = Wheel(wheel_type)

    def start_car(self):
        self.engine.start()
        print("Car started.")

engine_type = input("Enter Engine type: ")
wheel_type = input("Enter Wheel type: ")
my_car = Car(engine_type, wheel_type)
my_car.start_car()

# 20(a) WAP to represent the following graphs using a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H']
}

# Print the graph
for node, neighbors in graph.items():
    print(f"{node} -> {', '.join(neighbors)}")

# 20(b)
#representing graph in dictionary:

#B=Biratnagar,I=Ithari,Bi=BiratChowk,R=Rangeli,Dh=Dharan,K=kanepokhari,U=Urlabari,D=Damak

graph={
    'B': {'I': 22, 'R': 25,'Bi':30},
    'I': {'Dh': 20, 'Bi': 11},
    'Bi': {'K': 10},
    'R': {'K': 25, 'U': 46},
    'K':{'U':12},
    'U':{'D':6}
}

# Print the graph
for node, neighbors in graph.items():
    print(f"{node} -> {', '.join(f'{neighbor} ({weight})' for neighbor,weight in neighbors.items())}")



