############################### Day 3 ###############################

''' 
# 🧩 Concept 4: Nested if Statements
# You can have an if inside another if.


try: 
    age = int(input("Enter your age: "))
    
    if age>=18:
        citizen = input("Are you Indian? Yes/No")
        if citizen == "Yes":
            print("You are eligible for vote!")
        else:
            print("You are not eligible for vote because you are not Person of this Country. ")
    else:
        print("Sorry! Your age are not old enough to do vote.")

except ValueError: 
    print("Invalid Age! Enter the Valid AQge in the Interger format.")

    
'''
'''
# 🧩 Concept 5: Combining Conditions
# You can combine multiple conditions using and / or / not.


try:
    age = int(input("Enter your age: "))
    has_license = input("Do you have license? Yes/No.")
    if age>=18 and has_license== 'Yes':
        print("You are eligible for Passport.")
    elif age>=18 and has_license== 'No':
        print("First Get Driving Licence and then apply for the Passport.")
    else:
        print("You are not eligible for Passport.")

except ValueError: 
    print("Invalid Input!! Enter the valid input.")

    '''

# ⚙️ Intermediate Level

# 5️⃣ Marks → Grade Calculator
'''
try: 
    marks = int(input("Enter your marks:"))
    if marks >=90 and marks <=100:
        print(f"You recieved {marks} makrs and you get Grade A+")
    elif marks<90 and marks >= 80:
        print(f"You recieved {marks} marks and get Grade A")
    elif marks<80 and marks>=70:
        print(f"You recieved {marks} marks and get Grade B")
    
    elif marks<70 and marks>=60:
        print(f"You recieved {marks} marks and get Grade C")
    
    else:
        print(f"You recieved {marks} and Sorry! You are not qualified for next steps. Try Again." )

except ValueError:
    print("Invalid Input!!, Enter Marks Value in Integer format. ")

'''
'''
# Leap Year Checker:
try:
    get_year = int(input("Enter year:"))
    if get_year%4==0 and get_year%100 != 0:
        print(f"Year {get_year} is Leap Year.")
    elif get_year%400==0 and get_year%100!=0:
        print(f"Year{get_year} is Leap Year.")
    else:
        print(f"Year{get_year} is not a Leap Year.")

except ValueError:
    print("Invalid Year Entered, So enter the Year in the Correct Integer Value. ")

'''

# Login System (2-level validation)
# Take a username and password as input and verify them.
'''
assigne_username = "subh@123"
assigne_pass = "Ram@54321"

try:
    username = input("Enter  Your User Name: ")
    password = input("Enter  Your Password: ")
    if username == assigne_username and password==assigne_pass:
        print("Welcome!")
    else:
        print("Invalid credentials.") 

except ValueError:
    print("Invalid Login / Password.")

    ''' 

# Simple ATM Machine code created by ME
''' 

Assign_PIN = 1234


try:
    balance = 500
    user_pin = int(input("Enter your pin:"))
    if user_pin == Assign_PIN:
        print("Login Successful!")
        print("""
              Select the Option :
            1. Check Balance
            2. Deposit Money
            3. Withdraw Money
            4. Exit
          """)
        user_option = int(input("Enter you Transection Option Number:"))
        if user_option==1:
            print(f"Your Current Balance is {balance}")
        
        elif user_option==2:
            Deposite_AMT = int(input("Enter your deposite amount:"))
            balance = balance+Deposite_AMT
            print(f"Your current balance is {balance} after the deposite the amount.")
        
        elif user_option==3:
            Withdra_money = int(input("Enter How Much amount you want to withdra:"))
            if Withdra_money > balance:
                print("Insuffiecent balance in your account.")
            else:
                balance = balance-Withdra_money
                print(f"You Withdraw the amount is {Withdra_money} and remaining amount is {balance}")
        elif user_option==4:
            print("Exite!")
        else:
            print("You enter the invalid Option Number.")
  
    else:
        print("Inconrrect PIN, Please Enter Correct PIN.")

except ValueError:
    print("Incorrect Transection.")



''' 

# ATM machine code created by Trainer.
#  Simple ATM System with PIN Tries, Last Transaction, and Dynamic Balance

ASSIGNED_PIN = 1234
balance = 500
last_transaction = "No transaction yet."

# Allow three PIN attempt

tries = 3
while tries > 0:
    try:
        user_pin = int(input("Enter your PIN:"))
        if user_pin == ASSIGNED_PIN:
            print("\n Login Successful!")

            while True:
                print("""

                -----------------------------------------
                Choose an option:
                1. Check Balance
                2. Deposit Money
                3. Withdraw Money
                4. View Last Transaction
                5. Exit
                ---------------------------
              """) 
                try:
                    choice = int(input("Enter your choice (1-5):"))

                    if choice == 1:
                        print(f"Your current balance is ${balance}")
                    
                    elif choice == 2:
                        deposit_amt = int(input("Enter deposit amount: $ "))
                        balance += deposit_amt
                        last_transaction = f"Deposite ${deposit_amt}"
                        print(f"Deposite successfully! New balance: ${balance}")
                    
                    elif choice == 3:
                        withdraw_amt = int(input("Enter withdrawal amount: $ "))
                        if withdraw_amt > balance:
                            print(" Insufficient balance!")
                        else:
                            balance -= withdraw_amt
                            last_transaction = f"Withdrew ${withdraw_amt}."
                            print(f"Withdrawal successfull Remaining Balance: ${balance}")
                    
                    elif choice ==4:
                        print(f"Last Transaction: {last_transaction}")
                    
                    elif choice == 5:
                        print("Thank You for using our ATM!.")
                        break 
                    else:
                        print("Invalid option. Please select between 1-5.")
                except ValueError:
                    print("Invalid input! Please enter numbers only.")
            break # Exit outer loop after successful login
        else:
            tries -= 1
            print(f"Incorrect PIN. {tries} tries remaining.")
            if tries == 0:
                print("Account locked. Too many incorrect attempts.")
    except ValueError:
        print("Invalid input! Please enter a numeric PIN.")


