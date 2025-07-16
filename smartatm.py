pin = "4321"
balance = 5000

entered_pin = input("Enter your ATM PIN: ")

if entered_pin == pin:
    print("Access granted")
    choice = input("Enter 'withdraw' or 'check': ").lower()

    if choice == "withdraw":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawn ₹{amount}. Remaining balance: ₹{balance}")
        else:
            print("Insufficient funds.")
    elif choice == "check":
        print(f"Your current balance is ₹{balance}")
    else:
        print("Invalid option.")
else:
    print("Wrong PIN. Access denied.")
