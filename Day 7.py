'''
usuage of else with for ---> the else keyword will ony or execute when the loop is co,pletely done without any break
#for with else...

work_log = [0,1,1,1,0,1,0]
#result variable = longest_streak
longest_streak = 0
current_streak = 0
for day in work_log:
    if day == 1:
        #print(day)
        current_streak = current_streak = 1
        if current_streak > longest_streak:
            longest_streak = current_streak
            print(longest_streak)
            break
        #if break is removed the output will change
        else:
             current_streak = 0 #streak breaks
else:
    print(f'longest_streak is {longest_streak}')
print("execution done")

#for else with notification scenario

notifications = list(map(int,input("enter the values --> 0 or 1:").split(',')))
for notification in notifications:
    if notification == 1:
        print('unread notification')
        break
else:
    print('no notifications')
'''
#while ---> it relies on condition,it will be completely executed until the condition is satisfied
'''
syntax while:

while <condition>:
      statement(s)....
      ....
      ....
'''
i=10
while i >= 1:
    print(i)
    i=i-1

pin = "2613"
max_attempt = 3
current_attempt = 0
while current_attempt <= max_attempt:
    entered_pin = input("enter the ATM pin:")
    if entered_pin == pin:
        print("login sucessfull")
        break
    else:
         print("try again")
         current_attempt +=1
else:
    print("account locked,try again after 24 hours")
