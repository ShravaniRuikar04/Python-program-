print("WELCOME TO BANK")
print("Create a Bank Account:")

name = input("Enter your name: ")
phone_no = input("Enter contact no.: ")
age = input("Enter your age: ")
balance = float(input("Enter initial balance: "))

def menu():
    global balance

    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance = balance + amount
            print("Money Deposited Successfully")
            print("Balance =", balance)
        else:
            print("Invalid amount")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Money Withdrawn Successfully")
            print("Balance =", balance)
        else:
            print("Insufficient balance")

    elif choice == "3":
        print("Contact Number:", phone_no)
        print("Balance =", balance)

    elif choice == "4":
        print("Thanks you!!")
        return False

    else:
        print("Invalid choice")

while True:
    if menu() == False:
        break
