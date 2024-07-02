class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    def get_balance(self):
        return self.balance
    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: {interest}. New balance: {self.balance}")
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Overdraft limit exceeded.")
        else:
            print("Withdrawal amount must be positive.")
def main():
    print("Welcome to the Banking Application")
    owner = input("Enter the account owner's name: ")
    account_type = input("Enter the account type (savings/checking): ").lower()
    initial_balance = float(input("Enter the initial balance: "))
    if account_type == "savings":
        account = SavingsAccount(owner, initial_balance)
    elif account_type == "checking":
        account = CheckingAccount(owner, initial_balance)
    else:
        print("Invalid account type.")
        return

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        if account_type == "savings":
            print("3. Add Interest")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3' and account_type == "savings":
            account.add_interest()
        elif choice == '4':
            print(f"Current balance: {account.get_balance()}")
        elif choice == '5':
            print("Thank you for using the Banking Application.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()


