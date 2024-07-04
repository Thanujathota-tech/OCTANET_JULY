class ATM:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []
        self.pin = '1234'  # Default PIN

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposit: ${amount}')
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f'Withdraw: ${amount}')
            return True
        else:
            return False
    def get_transaction_history(self):
        return self.transaction_history

    def change_pin(self, current_pin, new_pin):
        if current_pin == self.pin:
            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                return True
        return False

def main():
    atm = ATM()
    while True:
        print("\n==== Welcome to the ATM ====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Change PIN")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            print(f"Your current balance is: ${atm.check_balance()}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            if atm.deposit(amount):
                print(f"Deposit of ${amount} successful")
            else:
                print("Deposit failed. Please enter a valid amount.")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if atm.withdraw(amount):
                print(f"Withdrawal of ${amount} successful")
            else:
                print("Withdrawal failed. Insufficient funds or invalid amount.")
        elif choice == '4':
            transactions = atm.get_transaction_history()
            if transactions:
                print("Transaction History:")
                for transaction in transactions:
                    print(transaction)
            else:
                print("No transactions yet.")

        elif choice == '5':
            current_pin = input("Enter your current PIN: ")
            new_pin = input("Enter new PIN (4 digits): ")
            if atm.change_pin(current_pin, new_pin):
                print("PIN changed successfully.")
            else:
                print("PIN change failed. Please enter correct current PIN and ensure new PIN is 4 digits.")

        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()