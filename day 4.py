'''
identity Operators ---> checks the identity of an object -->id()

a=5
b=a
print(id(a)) #o/p is 140730568066296
print(id(b)) #o/p is 1407305680662
c=5
print(id(c))  #o/p is 1407305680662
print(a is c) # o/p is True
print(5==5)  # o/p is True


a=[1,2,3,4]
b=a 
print(id(a))        # o/p is 1690619015040 
print(id(b))        # o/p is 1690619015040
c=[1,2,3,4]
print(id(c))        # o/p is 1690662467328

# as we have lists (multiple collection)
print(c is a )      # o/p is False
print(c==a)         # o/p is True
print(a is not c)   # olp is True

# bitwise operators ---> we perform bitwise operation over operands
#& (and), | (or), ^ (XOR), shifting operators(<<,>>)
#number will be converted to binary format

print(5&3) # both 5 and 3 to be converted binary and bitwise and is performed, # o,p is 1

print(5|3) # bitwise OR,       # o/p is 7

print(5^3) # bitwise XOR,      # o/p is 6

print( 5 or 3) # here and is logical operator checks for both existance   # o/p is 5 
#returns 5 in above case
#left shifting <<, right shifting >>
print(5<1)   # o/p is False comparison
print(5<<1) # left shift opeartion by 1 position      # o/p is 10
print(5>>1)  # right shift opeartin by 1 position    # o/p is 2
print(15<<2) # convert 15 to binary and perform 2 times left shifting    # o/p is 60                                               
print(15>>2) # convert 15 to binary and perform 2 times right  shifting   # o/p is 3

#input formatting --> input(),int(input()), float(input())
#you know --> single input
#2 or 3 inputs ---> map
#group of integers ----> list(map(int,input().split(','))

names= input("enter the names:").split(',')
print(names)            # o/p is ['saiteja shivakumar manasa']

name1,name2 =map(str,input("enter the brothers names:").split(','))
print(name1,name2)

#tokens ---> numeric datatype --> operators --> flow of the program
#control block statements --> they control the flow of the program
#when to execute, how to execute
#conditional statements --> if,else,elif,(rely on condition to be executed)
#repetition statements (loops) --> for,while

#conditional statements --> if usuage

syntax:
    if conditionn statement(s)...
        .....

#age=15
age=int(input("enter the age:"))
if age>=18:
    print('your age is:',age)  # o/p is 18
age= int(input("enter the age:"))
if age>=18 and age in[19,21,20]:
    print('your age is',age)
print(age)

#else keyword --> if-else

if <condition>:
    statement(s)...
    .....
'''
#vote eligibity --> to check his'her voter eligibility and give access....

age= int(input("enter the age:"))
if age>=18:
   print("you have voter eligibity and age is",age)
   print("Access granted")
else:
    age=18-age
    print("you dont have eligibility as your  age is",age,"years")  # o/p is enter the age:18 you have voter eligibity and age is 18 access granted
