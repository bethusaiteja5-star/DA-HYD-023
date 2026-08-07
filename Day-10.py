'''
# cricket total score ...
b=[4,6,1,0,2,4,0,6]
score =0
boun =0
db=0
for i in b:
    score +=i
    if i==4 or i==6:
        boun +=1
    elif i==0:
        db +=1
print(db)
print(boun)
print(score)

ATM pin attempts
pin = "1777"
max_attempts = 3
current_attempt = 0
while current_attempt <= max_attempts:
    entered_pin = input("Enter the ATM PIN:")
    if entered_pin == pin:
        print("Login_successful")
        break
        #continue #it holds for this conditions and skips to the next part 0
    else:
       print("Entered PIN is wrong..Try again carefully")
       current_attempt +=1
else:
    print("Account Locked,try after 24hours...")
'''
# pattern attempts
passkey = "saiteja@0311"
max_attempts = 5
current_attempt = 0
while current_attempt <= max_attempts:
    entered_passkey = input("Enter the passkey:")
    if entered_passkey == passkey:
        print("Login_successful")
        break
        #continue #it holds for this conditions and skips to the next part 0
    else:
       print("Entered Passkey is wrong..Try again carefully")
       current_attempt +=1
       
