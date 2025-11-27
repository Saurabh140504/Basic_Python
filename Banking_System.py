# [ BASIC BANKNG SYSTEM ]

# Step1:Account Details
Holder_Name="Saurabh Chaudhari"
Account_Number = 9344
Balance =500

# Step 2: Banking Menu
print("------ Welcome to Simple Banking System ------")

while True:
    print("\n/Options")
    print("1. Check Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exist Program")
    
    choose =int(input("Enter a input:(1-5): "))

    # 1.Check Account
    if choose ==1:
        Name = input("Enter Account Holder Name: ").title()
        Acc =int(input("Enter Account Number:"))
        if Name == Holder_Name and Acc == Account_Number:
            print("Your Account Found Successfully")
        else:
            print("Account Not Found")

    # 2.Deposit Money:
    elif choose == 2:
        Acc =int(input("Enter Account Number: "))
        if Acc == Account_Number:
            Amount =int(input("Enter Deposit Amount: "))
            Balance = Balance + Amount
            print(f"₹{Amount} Deposited Successfully. New Balance = ₹{Balance}")
        else:
            print("Invalid Account Number")
            
    # 3.Withdraw Amount 
    elif choose == 3:
        Acc=int(input("Enter Account Number: "))
        if Acc == Account_Number:
            Amount =int(input("Enter Withdraw Amount: "))
            if Amount <= Balance:
                Balance  = Balance - Amount
                print(f"₹{Amount} is Successfully Withdraw")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid Account Number")
    

    # 4.Check Balance
    elif choose ==4:
        print("Your Current Balance is:₹",Balance)
    
    # 5.Existing Program
    elif choose ==5:
        print("Exiting Program... Thank You!")
        break
        
    else:
        print("Invalid Input , Please try again.")