# ============================ ACCOUNT CLASSES ============================ #

class Accounts:
    """
    Base class representing a generic bank account.

    This class provides common banking operations such as
    depositing money, withdrawing money, viewing balance,
    transaction history, and displaying account details.
    """

    def __init__(self, acc_no, holder_name, balance=1000):
        """
        Initializes a bank account.

        Args:
            acc_no (int): Unique account number.
            holder_name (str): Name of the account holder.
            balance (float): Initial account balance.
        """
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        """
        Deposits money into the account.

        Args:
            amount (float): Amount to deposit.

        Returns:
            bool:
                True if deposit is successful.
                False otherwise.
        """
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited - ₹{amount}")
            return True

        return False

    def withdraw(self, amount):
        """
        Withdraws money from the account.

        Args:
            amount (float): Amount to withdraw.

        Returns:
            bool:
                True if withdrawal is successful.
                False otherwise.
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrawn - ₹{amount}")
            return True

        return False

    def show_balance(self):
        """
        Displays the current account balance.
        """
        print(f"\nCurrent Balance: ₹{self.balance:.2f}")

    def show_transactions(self):
        """
        Displays the complete transaction history.
        """
        print("\n========== TRANSACTION HISTORY ==========")
        print(f"Account Holder : {self.holder_name}")

        if not self.history:
            print("No transactions available.")
        else:
            for transaction in self.history:
                print(transaction)

    def display_details(self):
        """
        Displays all account details.
        """
        print("\n========== ACCOUNT DETAILS ==========")
        print(f"Account Number : {self.acc_no}")
        print(f"Account Holder : {self.holder_name}")
        print(f"Balance        : ₹{self.balance:.2f}")


# ============================ SAVINGS ACCOUNT ============================ #

class SavingAccount(Accounts):
    """
    Represents a savings account.

    A savings account earns interest
    on the available balance.
    """

    def __init__(self, acc_no, holder_name, balance=1000, interest_rate=6.5):
        """
        Initializes a savings account.

        Args:
            acc_no (int): Account number.
            holder_name (str): Account holder name.
            balance (float): Initial balance.
            interest_rate (float): Annual interest rate.
        """
        super().__init__(acc_no, holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        """
        Calculates the interest earned.

        Returns:
            float: Interest amount.
        """
        return self.balance * self.interest_rate / 100

    def display_details(self):
        """
        Displays savings account details.
        """
        super().display_details()
        print(f"Interest Rate  : {self.interest_rate}%")



# ============================ CURRENT ACCOUNT ============================ #

class CurrentAccount(Accounts):
    """
    Represents a current account.

    Current accounts allow withdrawals
    beyond the available balance
    up to a specified overdraft limit.
    """

    def __init__(self, acc_no, holder_name, balance=1000, overdraft_limit=500):
        """
        Initializes a current account.

        Args:
            acc_no (int): Account number.
            holder_name (str): Account holder name.
            balance (float): Initial balance.
            overdraft_limit (float): Maximum overdraft amount.
        """
        super().__init__(acc_no, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """
        Withdraws money using overdraft if necessary.

        Returns:
            bool:
                True if withdrawal is successful.
                False otherwise.
        """
        new_balance = self.balance - amount

        if amount > 0 and new_balance >= -self.overdraft_limit:
            self.balance -= amount
            self.history.append(f"Withdrawn - ₹{amount}")
            return True

        return False

    def display_details(self):
        """
        Displays current account details.
        """
        super().display_details()
        print(f"Overdraft Limit: ₹{self.overdraft_limit:.2f}")


# ============================ SAMPLE ACCOUNTS ============================ #

saving_accounts = [
    SavingAccount(113, "Maneesh"),
    SavingAccount(112, "Vamsee"),
    SavingAccount(117, "Varshi"),
]

current_accounts = [
    CurrentAccount(121, "Vamsee"),
    CurrentAccount(141, "Maneesh", 1000),
    CurrentAccount(111, "Varshi"),
]
# ============================ HELPER FUNCTIONS ============================ #

def find_account(account_list, account_number):
    """
    Searches for an account using its account number.

    Args:
        account_list (list): List of bank accounts.
        account_number (int): Account number to search.

    Returns:
        Accounts | None:
            Returns the account object if found,
            otherwise returns None.
    """
    for account in account_list:
        if account.acc_no == account_number:
            return account
    return None


def deposit_money(account):
    """
    Handles the deposit operation.

    Args:
        account (Accounts): Selected bank account.
    """
    try:
        amount = float(input("Enter amount to deposit: ₹"))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if account.deposit(amount):
        print("Amount deposited successfully.")
    else:
        print("Deposit failed.")


def withdraw_money(account):
    """
    Handles the withdrawal operation.

    Args:
        account (Accounts): Selected bank account.
    """
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if account.withdraw(amount):
        print("Withdrawal successful.")
    else:
        print("Insufficient balance or overdraft limit exceeded.")


def show_account_balance(account):
    """
    Displays the account balance.

    Args:
        account (Accounts): Selected bank account.
    """
    account.show_balance()


def show_account_details(account):
    """
    Displays complete account details.

    Args:
        account (Accounts): Selected bank account.
    """
    account.display_details()


def show_transaction_history(account):
    """
    Displays the transaction history.

    Args:
        account (Accounts): Selected bank account.
    """
    account.show_transactions()


def show_interest(account):
    """
    Displays the interest amount for a savings account.

    Args:
        account (SavingAccount): Savings account.
    """
    if isinstance(account, SavingAccount):
        print(f"Interest Earned: ₹{account.calculate_interest():.2f}")
    else:
        print("Current accounts do not earn interest.")


def account_menu(account):
    """
    Displays the menu for a selected account.

    Args:
        account (Accounts): Logged-in account.
    """
    while True:
        print("\n========== BANK MENU ==========")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Display Account Details")

        if isinstance(account, SavingAccount):
            print("6. Calculate Interest")
            print("7. Logout")
        else:
            print("6. Logout")

        try:
            choice = int(input("Choose: "))
        except ValueError:
            print("Enter only numbers.")
            continue

        if choice == 1:
            show_account_balance(account)

        elif choice == 2:
            deposit_money(account)

        elif choice == 3:
            withdraw_money(account)

        elif choice == 4:
            show_transaction_history(account)

        elif choice == 5:
            show_account_details(account)

        elif isinstance(account, SavingAccount) and choice == 6:
            show_interest(account)

        elif (isinstance(account, SavingAccount) and choice == 7) or (
            isinstance(account, CurrentAccount) and choice == 6
        ):
            print("Logged out successfully.\n")
            break

        else:
            print("Invalid choice.")
# ============================ MAIN BANKING SYSTEM ============================ #

def bank_function():
    """
    Runs the banking system.

    Allows users to choose an account type,
    log in using their account number,
    and perform banking operations.
    """
    while True:
        print("\n========== SBI BANK ==========")
        print("1. Savings Account")
        print("2. Current Account")
        print("3. Exit")

        try:
            account_type = int(input("Choose your account type: "))
        except ValueError:
            print("Please enter only numbers.")
            continue

        if account_type == 3:
            print("Thank you for banking with SBI.")
            break

        elif account_type not in (1, 2):
            print("Invalid option.")
            continue

        try:
            account_number = int(input("Enter your account number: "))
        except ValueError:
            print("Account number must be an integer.")
            continue

        # ---------------- Savings Account ---------------- #

        if account_type == 1:
            account = find_account(saving_accounts, account_number)

            if account:
                print(f"\nWelcome {account.holder_name}!")
                account_menu(account)
            else:
                print("Savings account not found.")

        # ---------------- Current Account ---------------- #

        elif account_type == 2:
            account = find_account(current_accounts, account_number)

            if account:
                print(f"\nWelcome {account.holder_name}!")
                account_menu(account)
            else:
                print("Current account not found.")


# ============================ START APPLICATION ============================ #

if __name__ == "__main__":
    bank_function()