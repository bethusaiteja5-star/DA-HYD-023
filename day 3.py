#Numeric datatype ---> int,float,complex along with boolean

#Input formatting ---> Accepting input from the user ---> input()

#Accepting integer input from user
#by default input() accept any input ---> str
'''
age= input("enter the age:") 
print(age)
print(type(age)) #o/p is sai teja

age=int(input('enter the age:'))
print(age)
print(type(age))

#float(input()) -->  accepts integers, float values
age=float(input('enter the age:'))
print(age)
print(type(age))

#Accepting string integer from user

name= input("enter the name;")
print(name)
print(type(name))

#space separated values
marks = input().split() #now you enter spaces in output 
print(marks)
#comma separated values
marks=input("enter values;").split(',')
print(marks)

#list of integers
marks=int(input("enter values;")).Split(',')
print(marks)

#list of integers
marks= map(int(int,input("enter the values").split(',')))
print(marks)

#now we want to accept 2 values from user
age,salary=map(int,input("enter the values").split(','))
print(age)
print(salary)

#single input --> int(input())
#two inputs ---> a,b = map(int,input().split(','))
#any number result as list ---> a=list(map(int,input().split(',')))


#float of integers
marks = list(map(float,input("enter the values").split(',')))
print(marks)

#group of float values
age,salary=map(float,input("enter the values").split(','))
print(age)

#accepting input from user ---> int,float --> input forwarding

#operators ---> operators perform operations between value(operands)
#7 types -----> arithmetic,assignment,comparison
#membership,identity,logical,bitwise

#arithmetic operators ----> arithmetic operations
#+,-,-,*,/
print(5+3) # o/p is 8
print(15-3) # o/p is 12
print(2*10) # o/p is 20
print(2/8) # o/p is 0.20

#floor divion (integer division) ---> returns quotient
print(5//3) #o/p is 1
#modulus ---> divisible rules ---> returms remainder
print(5%4) # o/p is 1
#power(exponential)
print(5**4) # o/p is 625

#task ---> accept integer input as length,breadth ---> find the area of rectangele
#area =length*breadth
#length =10
#breadth=7
print(10&7) # o/p is 2
l,b=map(int,input("enter the length breadth values;").split(','))
c=l*b
print('result;',c) # o/p is 70

#Assignmnet operators ---> assign the values
# =,+,-,-=
a= 45
print(a)
#update the value of a
a=a+5
print(a) # o/p is 50
b=35
b+=a
print(b) # o/p is 85
b-=5
print(b) # o/p is 80
b*=5
print(b) # o/p is 400
b/=5
print(b) # o/p is 80.0
b//=5
print(b) # o/p ois 16.0
b%=5
print(b) # o/p is 1.0
b**=15
print(b) # o/p is 1.0

age=25
print(age==25) #returns boolean output # o/p is True
print(age !=35) # o/p is True
print(age==35)# o/p is False
print(age<35) # o/p is True
print(age>35) # o/p is False
print(age<=35)  # o/p is True
print(age>=35) # o/p is False

#membership operators ---> im,not in ---> boolean
#it checks for the existance of an object in a collection

marks = [ 56,75,45,85]
print( 35 in marks) # o/p is False
print(35 in 355) # Typeerror
print(56 in marks) #typerror
'''
#logical operators ---> logical decision making --> and,or,not
#and ---> all conditions to be satisfied

a= (25 in [24,45,65]) and 45<56 # o/p is false
print(a)
b=45>56 or 25 <=45
print(b) # o/p is true
c= not(True)
print(c) # o/p is falses