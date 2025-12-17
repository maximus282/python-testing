# Kompletny przykład z modułem, klasą i jakimiś funkcjami pomocniczymi
# I na tym wszystkie dobre praktyki
"""
Moduł demonstracyjny z klasą BankAccount i funkcjami pomocniczymi.

Przykłady użycia na poziomie modułu:

>>> account = BankAccount("TEST001", 100)
>>> account.deposit(50)
150.0
>>> validate_email("test@example.com")
True

Sprawdzenie że klasa działa poprawnie:
>>> acc = BankAccount("123")
>>> acc.deposit(25)
25.0
>>> acc.withdraw(10)
15.0
"""
import doctest


class BankAccount:
    """
    Reprezentuje konto bankowe.

    Examples:
        Tworzenie konta:
        >>> account = BankAccount("12345", 100.0)
        >>> account.account_number
        '12345'
        >>> account.balance
        100.0

        Operacje na koncie:
        >>> account.deposit(50)
        150.0
        >>> account.withdraw(30)
        120.0

        Sprawdzanie salda:
        >>> account.get_balance()
        120.0

        NiewystarIsolatedAsyncioTestCaseczające środki:
        >>> account.withdraw(200)
        Traceback (most recent call last):
            ...
        ValueError: Insufficient funds
    """

    def __init__(self, account_number, initial_balance=0.0):
        """
        Inicjalizuje nowe konto bankowe.

        >>> account = BankAccount("54321")
        >>> account.balance
        0.0
        """
        self.account_number = account_number
        self.balance = float(initial_balance)

    def deposit(self, amount):
        """
        Wpłaca środki na konto.

        >>> account = BankAccount("123", 100)
        >>> account.deposit(25)
        125.0

        Nieprawidłowa kwota:
        >>> account.deposit(-10)
        Traceback (most recent call last):
            ...
        ValueError: Amount must be positive
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Wypłaca środki z konta.

        >>> account = BankAccount("123", 100)
        >>> account.withdraw(25)
        75.0
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

        >>> account = BankAccount("123", 42.50)
        >>> account.get_balance()
        42.5
        """
        return self.balance


def validate_email(email):
    """
    Waliduje adres email (uproszczona wersja).

    Args:
        email (str): Adres email do sprawdzenia

    Returns:
        bool: True jeśli email jest prawidłowy

    Examples:
        Prawidłowe emaile:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("test.user+tag@domain.co.uk")
        True

        Nieprawidłowe emaile:
        >>> validate_email("invalid")
        False
        >>> validate_email("@example.com")
        False
        >>> validate_email("user@")
        False
        >>> validate_email("")
        False

        Przypadki brzegowe:
        >>> validate_email("a@b.co")
        True
        >>> validate_email("very.long.email.address@very.long.domain.name.com")
        True
    """
    import re
    if not email or not isinstance(email, str):
        return False

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
