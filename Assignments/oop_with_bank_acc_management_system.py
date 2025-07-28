
class Account():

    bank_name= "Misogi Bank"
    minimum_balance = 1000
    total_accounts = 0

    def __init__(self, account_number, holder_name, balance=0):
        if not holder_name or not isinstance(holder_name, str):
            raise ValueError("Holder name must be a non-empty string.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance

        Account.total_accounts += 1

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self._balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < Account.minimum_balance:
            raise ValueError(f"Cannot withdraw below minimum balance of {Account.minimum_balance}.")
        self.balance -= amount
        return self._balance
    
    def get_balance(self):
        return self._balance

    @classmethod
    def set_bank_name(cls, new_name):
        if not new_name or not isinstance(new_name, str):
            raise ValueError("Bank name must be a non-empty string.")
        cls.bank_name = new_name

    @classmethod
    def set_minimum_balance(cls, new_minimum):
        if new_minimum < 0:
            raise ValueError("Minimum balance cannot be negative.")
        cls.minimum_balance = new_minimum

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

class SavingsAccount(Account):
    interest_rate = 0.04  # 4% interest rate

    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return interest

class CheckingAccount(Account):
    overdraft_limit = 500  # Allow overdraft up to $500

    def __init__(self, account_number, holder_name, balance=0):
        super().__init__(account_number, holder_name, balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError(f"Cannot withdraw beyond overdraft limit of {self.overdraft_limit}.")
        self.balance -= amount
        return self._balance