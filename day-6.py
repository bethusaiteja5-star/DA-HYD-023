'''
control statement ---> control of flow of execution of the program
                  ---> conditional statement ---> if,elif,else..
                  ---> repetition statements (loops) ---> for,while(for with else)(while with else)
                  
                  ---> jumping statements ---> break,continue,pass
'''
#loops --> loops are helpful for repetative(automative task)
#for keywords will be helpful to iterate over a sequence / range
#syntax for (for keywords);
'''
for <temp var> in sequence/range:
    statements(s)....

#range(start,stop,step)
# by default range picks as 0 start value
for i in range(12):
   print(i)
#for above case we can got 10 iterations
for i in range(1,10):
    print(f"value of i in {i}")

for i in range(1,10):
    if i>5 and i%2 == 0:
        print(f"the final value o fi is ---> {i}")
#range(start,stop,step) --> here step ---> interval
for i in range(1,10,4):
    print(i)

for  i in range(10,0,-1):
    print(i)
for i in range(-10,0,1):
    print(i)

#[] ---> we generally lists
names = ['saiteja','shivakumar','manasa']
print(len(names)) #len(obj) ---> returns the number of items in a container

#calculate the sum of first 10 numbers
#first understand your input ---> range(11) ---> 10 numbers
#second understand your output ---> sum(number)
#third we need to map the logic

result = 0 #target variable
for  i in range(11):
    #print(i)
    #print(f'result is {i+i}')
    result = result + i #result +=i
    print(f'now the result is {result}')
print(f'sum of 10 numbers is {result}')
'''
#calculate teh first 10 even numbers
result = 0
for i in range(11):
    if i % 2 == 0:
       result = result + i
print(f'now the result is {result}')
print(f'sum of 10 even numbers is {result}')

