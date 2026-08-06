'''
Tokens --> Variables, punctuators

Variables --> Named memory location, its a placeholder for data
#Rules are to be followed

#MultiAssignment of Variables

name,age,place = 'codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='--->')

#a,b=2,3,5 #valueError as too many values to unpack
#Reasoning variabeles

name="codegnan"
a,b = 45,1.5
print(a,b)
a,b = b,a
print(a,b,sep=',')
a,b = b,a #NameError as c is not defined
print(a,b)

#Deleting the varibales --->del
#del a
#print(a)
#del a,b
#print(a,b)

#punctuators ---> [](list),{}(Dict,sets),()(tuples)
name="sai teja";age=21
print(name,age)

'''
#Datatypes ---> Numeric (int,float,complex),boolean,None,
          #---> sequences ---> Lists,Tuples,Sets,Strings,Frozens,Mappings(Dict)

Numeric= int,float,complex
#int--> quantity,age..
manasa = 'Saiteja'
print(manasa)
print(type(manasa))

#quantity = 03 # it is not allowed
#print(quantity)

#float datatype --> temp,salary,price
price=200.3;dis=2.5
print(price,dis)
print(type(price))
'''

#complex ----> comnination of real and imag
i=5
data = 5+i
print(data)

data = 5j # j is imag representation
print(data)
print(type(data))

#boolean --> True / False

valid = True
print(type(valid))

error = False
print(type(error))
valid = 1.3
print(type(valid))
'''

#TypeCasting ---> converting one type to another
#python by default follows implicit type (we need not mention the datatype)

#we will gof for explicict conversion

#every built-in datatype is a built-in function
int,float,complex,bool

#TypeCasting --> int --> flaot,complex,bool
''
age= 21
print(type(age))
b=float(age)
print(b)
c=complex(age)
print(c)
d= bool(age)
print(type(age))
print(d)
e=bool(0)
print(type(age))
print(e)
#float ---> typecasting ---> int,complex,bool

a=25.4
print(type(a))
b=int(a)
print(b)
print(type(b))
e=complex(a)
print(e)
print(type(b))
f=bool(b)
print(f)
a=25
print(type(a))
b=float(a)
print(b)
data=2+5j
print(type(data)) #typerror

#example typecasting programs
e=int(float(bool(21)))
print(e)
f=bool(int(float(21)))
print(f)

f=45+2.5+2+3j+False  # olp is (49.5+3j)
print(f)









