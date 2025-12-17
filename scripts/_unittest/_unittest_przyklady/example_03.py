class Person:
    """Person class representing an individual with basic information.
    
    Attributes:
        name: Full name of the person
        age: Age in years
        email: Email address
    """

    def __init__(self, name, age, email):
        """Initialize a new Person instance.
        
        Args:
            name: Full name of the person
            age: Age in years
            email: Email address
        """
        self.name = name
        self.age = age
        self.email = email

    def is_adult(self):
        """Check if person is an adult (18 years or older).
        
        Returns:
            True if person is 18 or older, False otherwise
        """
        return self.age >= 18

    def get_initials(self):
        """Get initials from the person's name.
        
        Returns:
            String containing uppercase initials from each part of the name
        """
        parts = self.name.split()
        return ''.join([part[0].upper() for part in parts])

    def __str__(self):
        """Return string representation of the person.
        
        Returns:
            String in format 'Name (Age)'
        """
        return f"{self.name} ({self.age})"
