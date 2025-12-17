# Custom assertions
import unittest

from example_03 import Person


class TestPersonWithCustomAssertions(unittest.TestCase):
    """Tests with custom assertions"""

    def assertIsAdult(self, person, msg=None):
        """Custom assertion checking if person is adult"""
        if not isinstance(person, Person):
            raise TypeError("Expected Person object")

        if not person.is_adult():
            standard_message = f"{person.name} (age {person.age}) is not adult"
            self.fail(self._formatMessage(msg, standard_message))

    def assertIsMinor(self, person, msg=None):
        """Custom assertion checking if person is minor"""
        if not isinstance(person, Person):
            raise TypeError("Expected Person object")

        if person.is_adult():
            standard_message = f"{person.name} (age {person.age}) is not minor"
            self.fail(self._formatMessage(msg, standard_message))

    def assertValidEmail(self, email, msg=None):
        """Custom assertion checking email validity"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(pattern, email):
            standard_message = f"'{email}' is not a valid email address"
            self.fail(self._formatMessage(msg, standard_message))

    def assertPersonValid(self, person):
        """Complex assertion checking entire person validity"""
        with self.subTest(person=person.name):
            # Check basic properties
            self.assertIsInstance(person, Person)
            self.assertIsInstance(person.name, str)
            self.assertIsInstance(person.age, int)
            self.assertIsInstance(person.email, str)

            # Check values
            self.assertGreater(len(person.name), 0, "Name cannot be empty")
            self.assertGreaterEqual(person.age, 0, "Age cannot be negative")
            self.assertLessEqual(person.age, 150, "Age seems unrealistic")

            # Check email
            self.assertValidEmail(person.email)

    # Unit tests
    def create_test_person(self, name="John Doe", age=25, email="john@example.com"):
        """Factory for creating test Person objects"""
        return Person(name, age, email)

    def test_adult_person(self):
        """Test adult person"""
        adult = self.create_test_person("Alice Smith", 30, "alice@example.com")

        self.assertPersonValid(adult)
        self.assertIsAdult(adult, )
        self.assertEqual(adult.get_initials(), "AS")

    def test_minor_person(self):
        """Test minor person"""
        minor = self.create_test_person("Bob Johnson", 16, "bob@example.com")

        self.assertPersonValid(minor)
        self.assertIsMinor(minor)
        self.assertEqual(minor.get_initials(), "BJ")

    def test_edge_case_adult(self):
        """Test adult age boundary"""
        just_adult = self.create_test_person("Charlie Brown", 18, "charlie@example.com")
        almost_adult = self.create_test_person("David Wilson", 17, "david@example.com")

        self.assertIsAdult(just_adult)
        self.assertIsMinor(almost_adult)

    def test_multiple_people_with_subtests(self):
        """Test multiple people using subTest"""
        people = [
            ("Emma Watson", 33, "emma@example.com", True),
            ("Tom Holland", 27, "tom@example.com", True),
            ("Millie Brown", 19, "millie@example.com", True),
            ("Jacob Tremblay", 17, "jacob@example.com", False),
        ]

        for name, age, email, should_be_adult in people:
            with self.subTest(name=name, age=age):
                person = self.create_test_person(name, age, email)
                self.assertPersonValid(person)

                if should_be_adult:
                    self.assertIsAdult(person)
                else:
                    self.assertIsMinor(person)

    def test_invalid_email_formats(self):
        """Test invalid email formats"""
        invalid_emails = [
            "invalid",
            "@example.com",
            "user@",
            "user.example.com",
            "user@.com",
            ""
        ]

        for email in invalid_emails:
            with self.subTest(email=email):
                with self.assertRaises(AssertionError):
                    self.assertValidEmail(email)

    def test_valid_email_formats(self):
        """Test valid email formats"""
        valid_emails = [
            "user@example.com",
            "user.name@example.co.uk",
            "user+tag@example-domain.org",
            "123@example.com"
        ]

        for email in valid_emails:
            with self.subTest(email=email):
                # Should not raise exception
                self.assertValidEmail(email)
