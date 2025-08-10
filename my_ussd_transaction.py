print("Welcome to my banking program!!!!!")
def withdraw():
    amount=float(input("enter the amount to be withdrawn "))
    if amount > balance:
       print("insufficient fund")
       return 0
    elif amount == 0:
       print("invalid amount to be withdrawn amount must be greater than 0")
       return 0
    else:
       print(f"you have been debited ${amount} your current balance is ${balance-amount:,.2f} only")
       return amount

def deposite():
    amount = float(input("enter the amount you want to deposite "))
    if amount < 0:
       print("this amount is too low to deposite, enter correct amount to be deposited")
       return 0
    else:
       print(f"transaction of ${amount:,.2f} is successful")
       return amount
def check_balance(balance):
    print(f"your balance is ${balance:,.2f} only")
def transfer():
    user_number = input("enter beneficiary account number ")
    if len(user_number) != 10:
        print("invalid account number")
        quit()
        if len(user_number) > 10:
             print("invalid account number")
             quit()
    else:
        if len(user_number) == 10:
           beneficiary_amount = float(input("enter the amount you  want to transfer "))    
     
           if beneficiary_amount > balance:
              print("insufficient fund for the amount enter")
              return 0
           elif beneficiary_amount <= 0:
              print('amount must be greater than 0')
              return 0
           else:
             if beneficiary_amount <= balance:
                print(f"you are about to transfer ${beneficiary_amount} to {user_number}")
                print("enter 'yes' confirm your transaction or 'No' to terminate")
                pas = input()
                if pas == "no":
                   print("thank you transaction terminted")
                   quit().lower()
                elif pas == "yes":
                   print(f"transaction successful your current balance is ${balance-beneficiary_amount:,.2f}.only")
                else:
                   print("invalid command")
                   quit()
               
                
def exit():
    pass

balance = 0
beneficiary_amount = 0
is_running = True
while is_running:
   print('''
   1. withdraw
   2. deposite
   3. check balance
   4. transfer
   5. exit''')
   user_input = input("select option to perform transaction ")
   if user_input == "1":
       balance -= withdraw()
   elif user_input == "2":
      balance += deposite()
   elif user_input == "3":
       check_balance(balance)
   elif user_input == "4":
       transfer()
       balance -= beneficiary_amount
   elif user_input == "5":
       is_running = False
   else:
     print("invalid input")
print("Thank you! Have a nice day")
