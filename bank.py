print("Welcome to Union bank")
class Bank:
    accbal = 10000

    def deposit(self):
        amount = int(input("Enter amount: "))
        if 100 < amount < 50000 and amount % 100 == 0:
            print("Deposit successful")
            self.accbal = amount + self.accbal
            print("Account balance:", self.accbal)
        else:
            print("Deposit failed")

    def withdraw(self):
        w_amount = int(input("Enter withdraw amount: "))
        chance = 0
        while chance < 3:
            if 100 < w_amount < 20000 and self.accbal > 500 and w_amount % 100 == 0:
                print("Amount withdrawn")
                self.accbal -= w_amount
                print("Account balance:", self.accbal)
                break
            else:
                chance += 1
                print("Invalid withdrawal attempt. Chances left:", 3 - chance)
        if chance == 3:
            print("Chances exceeded. No withdrawal made.")

    def viewOptions(self):
        while True:  
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance Enquiry")
            print("0. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.deposit()
            elif choice == 2:
                self.withdraw()
            elif choice == 3:
                print("Account balance:", self.accbal)
            elif choice == 0:
                print("Exiting program...")
                return  
            else:
                print("Invalid choice, please try again.") 

    def validate(self):
        chance = 0
        while chance < 3:
            pin = int(input("Enter pin number: "))
            if pin == 1234:
                print("Pin validated successfully!")
                self.viewOptions() 
                return  
            else:
                chance += 1
                print("Invalid pin, attempt", chance, "of 3.")
        if chance == 3:
            print("Authentication failed. Exiting...")
obj = Bank()
obj.validate()
