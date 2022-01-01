#Q1
#Print string in specified format
string = "Twinkle, twinkle, little star, \n \t How I wonder what you are! \n \t \t Up above the world so high, \n \t \t Like a diamond in the sky. \n Twinkle, twinkle, little star, \n \t How I wonder what you are"
print(string)

#Q2
#To find python version
import sys
print(sys.version)

#Q3
#To display current date and time
import datetime
current_time = datetime.datetime.now()
print(current_time)

#Q4
#To compute area from radius
Radius = int(input("Enter Radius of circle:"))
Area = 3.1416 * (Radius**2)
print(Area)

#Q5
#To show first and last name in reverse order with space in between
first_name = input("Enter First Name:")
last_name = input("Enter Last Name:")
print(last_name + " " + first_name)

#Q6
#Add after taking two inputs
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = a + b
print(c)
