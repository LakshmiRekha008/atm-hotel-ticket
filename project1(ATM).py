# python program to create bank account and deposit , withdraw using functions 

import mysql.connector                      # using sql for storing data in database

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    password="rEkha@132",
    db="project1_db"

)

mycursor=mydb.cursor()


import random
import sys

# use class ATM
class ATM():
    def __init__(self,name, mobile_number, city_name, account_number, balance = 0):
        self.name = name
        self.mobile_number= mobile_number
        self.city_name=city_name
        self.account_number = account_number
        self.balance = balance

     # using function account_details() for view the details    
    def account_detail(self):

        sql=("insert into bank_account (Name, Mobile_number, City_name, Account_number) values (%s,%s,%s,%s)")

        val=(name, mobile_number, city_name, account_number)
        mycursor.execute(sql,val)
        mydb.commit()
        
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name .upper()}")
        print(f"Mobile number: {self.mobile_number}")
        print(f"City name: {self.city_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: {self.balance}\n")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance:", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is {self.balance} only/-.")
            print(f"So! we have only less than {self.balance}.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"{amount} withdrawal successful!")
            print("Current account balance:", self.balance)
            print()
 
    def check_balance(self):
        print("Available balance:", self.balance)
        print()
 
    def transaction(self):
        print("""
              TRANSACTION 
            ---------------
        * * * * * * * * * * * * *
        *       Choices:        *
        *   1. Account Detail   *
        *   2. Check Balance    *
        *   3. Deposit          *
        *   4. Withdraw         *
        *   5. Exit             *
        * * * * * * * * * * * * *
        """)
        
        while True:
            try:
                option = int(input("Enter your Choice:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                # call account_details() function
                    atm.account_detail()   
                elif option == 2:
                # call account_balance() function
                    atm.check_balance()
                elif option == 3:
                    print("********** DEPOSIT **********")

                    amount = int(input("How much you want to deposit:"))
                    atm.deposit(amount)
                elif option == 4:
                    print("********** WITHDRAW **********")

                    amount = int(input("How much you want to withdraw:"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt ..... please wait .....
                
          *******************************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: Nu.{self.balance}                    
 
              Thanks for choosing us as your bank                  
          ********************************************************
          """)
                    sys.exit()
                 
 
print("******* WELCOME TO BANK OF AXIS *******")
print("___________________________________________________________\n")

print("********** ACCOUNT CREATION ***********")

name = input("Enter your Name: ")
mobile_number=input("Enter Your Mobile Number: ")
city_name=input("Enter Your City Name: ")
account_number = input("Enter your account number: ")
print("Congratulations! Your Account created successfully......\n")

print("___________________________________________________________\n")
 
atm = ATM(name, mobile_number, city_name, account_number)
 
while True:
    trans = input("Do you want to do any transaction? (y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("""
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
   |                                       |
   |  Thanks for choosing us as your bank  |
   |         Visit us again!               |
   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
        
        """)
        break
    
    else:
        print("Enter only 'y' or 'n' only - 'y' for 'yes' & 'n' for 'no' .\n")
  




