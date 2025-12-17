class BankAccount:

    def __init__(self, account_number, initial_balance=0.0):
        """
        Inicjalizuje nowe konto bankowe.
        """
        self.account_number = account_number
        self.balance = float(initial_balance)

    def deposit(self, amount):
        """
        Wpłaca środki na konto.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Wypłaca środki z konta.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        """
        Zwraca aktualne saldo.
        """
        return self.balance


def validate_email(email):
    """
    Waliduje adres email (uproszczona wersja).

    Args:
        email (str): Adres email do sprawdzenia

    Returns:
        bool: True jeśli email jest prawidłowy

    """
    import re
    if not email or not isinstance(email, str):
        return False

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
