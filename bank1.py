import streamlit as st

class Bank:
    accbal = 10000

    def deposit(self):
        amount = st.number_input("Enter amount to deposit (100-50000, multiples of 100):", min_value=0, step=100)
        if 100 <= amount <= 50000 and amount % 100 == 0:
            self.accbal += amount
            st.success("Deposit successful!")
        else:
            st.error("Invalid amount. Deposit failed.")
        st.write("Account balance:", self.accbal)

    def withdraw(self):
        chance = 0
        while chance < 3:
            w_amount = st.number_input("Enter withdrawal amount (100-20000, multiples of 100):", min_value=0, step=100)
            if 100 <= w_amount <= 20000 and self.accbal - w_amount >= 500 and w_amount % 100 == 0:
                self.accbal -= w_amount
                st.success("Withdrawal successful!")
                st.write("Account balance:", self.accbal)
                return
            else:
                st.warning(f"Invalid withdrawal attempt. {2 - chance} attempts remaining.")
            chance += 1
        st.error("Chances exceeded. Transaction failed.")

    def view_balance(self):
        st.write("Account balance:", self.accbal)

    def view_options(self):
        choice = st.selectbox("Choose an option:", ["Deposit", "Withdraw", "Balance Enquiry", "Exit"])
        if choice == "Deposit":
            self.deposit()
        elif choice == "Withdraw":
            self.withdraw()
        elif choice == "Balance Enquiry":
            self.view_balance()
        elif choice == "Exit":
            st.info("Thank you for using the bank!")

    def validate(self):
        chance = 0
        while chance < 3:
            pin = st.text_input("Enter your 4-digit PIN:", type="password")
            if pin == "1234":
                st.success("Authentication successful!")
                self.view_options()
                return
            else:
                st.error(f"Invalid PIN. {2 - chance} attempts remaining.")
            chance += 1
        st.error("Authentication failed. Exiting.")

st.title("Banking System")
obj = Bank()
obj.validate()
