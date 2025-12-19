# Prosta klasa reprezentująca kalkulator
class Calculator:
    def __init__(self):
        self.result = 0
        self.last_error = None
    
    def add(self, a, b):
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        self.result = a - b
        return self.result
        
    def multiply(self, a, b):
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        if b == 0:
            self.last_error = "Cannot divide by zero"
            return None
        self.result = a / b
        return self.result