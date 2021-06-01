import random 
currentbalance = 500
accountno = random.randint(1000000000, 9999999999)
transaction = ["          500  CR"]

def Address():
    addr = input("Enter Your Address [Kothrud/Deccan/Shivajinagar]: ")
    adr = addr.lower()
    if adr == 'kothrud':
        return addr
    elif adr == 'deccan':
        return addr
    elif adr == 'shivajinagar':
        return addr
    else:
        print("Enter Again....")
        _Address()

def phoneno():
    phoneno = int(input(" enter your 10 digit no = "))
    mno = str(pno)
    if len(mno) == 10:
         return mno
    else:
        print("enter valid no")
    phoneno()

def adharcardno():
    adharcardno= int(input("enter adhar card no = "))
    adhno= str(adh)
    if len(adh)  == 12:
        return adh
    else:
        print("enter valid no")
    adharcardno()

def gender():
    gender = input("enter your gender [Male/Female] = ")
    if gender == 'Male':
        return gender
    elif gender == 'female':
        return gender
    else:
        print(" enter valid information ")
    gender()

def acctype():
    acctype =input("enter your account type [saving/current] ")
    acctype = acctype.lower
    if acctype == 'saving':
         return acctype
    elif acctype == 'current':
        return acctype
    else:
        print("enter valid information")
    acctype()

def createAccount():
    global accountno
    name = input("enter your name = ")
    add = address()
    DOB = input("enter your DOB [dd/mm/year]")
    gender = gender()
    phono = phoneno()
    emailid= input("enter your emailid =  ")
    adharno = adharcardno()
    panno = input("enter your pan no =  ")
    acctype = acctype()

    print(f"\nCongrants Your Account With Account Number {accountno} created successfully.")
    print("\nYour Account Information as Follows")
    print(f"\nName : {name}\nAddress : {add}\nDOB : {dob}\nGender : {gender}\nPhone No : {phno}\
        \nEmail Id : {emailid}\nPAN Number : {panno}\nAadhar Number : {adharno}\nAccount Type : {acctype}\
        \nYour Current Balance is Rs.{currentBalance}")


def depositeMoney():
    #global accountno
    global currentBalance
    global transaction
    accountno = int(input("Enter Account Number : = "))
    deposite = int(input("Enter Amount To Deposite := "))
    if deposite  > 0:
        currentBalance = currentBalance + deposite
        transaction.append(f"        {deposite}      CR")
        print(f"\nAmount of Rs.{deposite} Successfully Credited into Account Number {accountno}.\nTotal Balance : Rs {currentBalance}")
    else:
        print(f"Please valid Amount to deposite.\nTotal Balance : Rs {currentBalance}")

def withdrawMoney():
    global currentBalance
    global transaction
    accountno = int(input("Enter Account Number : "))
    withdraw = int(input("Enter Amount To Withdraw : "))
    if currentBalance > 500:
        currentBalance = currentBalance - withdraw
        transaction.append(f"        {withdraw}      DR")
        print(f"\nAmount of Rs.{withdraw} Successfully Debited into Account Number {accountno}.\nTotal Balance : Rs {currentBalance}")
    else:
        print(f"Insufficient Balance.\nTotal Balance : Rs {currentBalance}") 




def miniStatement():
    global currentBalance
    global transaction
    accountno = int(input("Enter Account Number : "))
    print(f"Your Mini Statement\nYour Account Number : {accountno}")
    print("\nSr No    Amount     CR/DR\n---------------------------")
    transaction = transaction[::-1]
    ministate = transaction[:5]
    for i in range(0, 5):
        print(f"{i+1}{ministate[i]}")
    print(f"\nTotal Balance : Rs {currentBalance}")

while(True):
    print("\n*****Welcome To SBI***")
    print("\nSBI Offers following services")
    print("\n1] Create Account\n2] Deposite Money\n3] Withdraw Money\n4] Mini Statement [Last 5 Transaction]\n5] Exit")
    choice = int(input("\nEnter Your Choice [1/2/3/4/5] : "))
    if(choice in [1, 2, 3, 4]):
        if choice == 1:
            createAccount()
        elif choice == 2:
            depositeMoney()
        elif choice == 3:
            withdrawMoney()
        elif choice == 4:
            miniStatement()
    elif choice == 5:
        exit()
    else:
        print("Wrong Choice.Please enter correct choice.")
