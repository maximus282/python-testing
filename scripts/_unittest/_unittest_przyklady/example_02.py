class BankAccount:
    """Bank account class for managing transactions and balance.
    
    Attributes:
        ACCOUNT_COUNTER: Class variable tracking total accounts created
        balance: Current account balance
        transaction_history: List of transaction records
    """
    ACCOUNT_COUNTER = 0

    def __init__(self, initial_balance=0):
        """Initialize a new bank account.
        
        Args:
            initial_balance: Starting balance for the account (default 0)
        """
        self.balance = initial_balance
        self.transaction_history = []
        BankAccount.ACCOUNT_COUNTER += 1

    def deposit(self, amount):
        """Deposit money into the account.
        
        Args:
            amount: Amount to deposit (must be positive)
            
        Raises:
            ValueError: If amount is not positive
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        """Withdraw money from the account.
        
        Args:
            amount: Amount to withdraw (must be positive)
            
        Raises:
            ValueError: If amount is not positive or exceeds balance
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transaction_history.append(f"Withdraw: -{amount}")

    def get_balance(self):
        """Return current account balance.
        
        Returns:
            Current balance as a number
        """
        return self.balance

    def get_transaction_count(self):
        """Return number of transactions made.
        
        Returns:
            Number of transactions in history
        """
        return len(self.transaction_history)
