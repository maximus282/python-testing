# Assertion methods overview
import unittest


class TestAssertMethods(unittest.TestCase):
    """Demonstration of various assert* methods"""

    def test_equality_assertions(self):
        """Equality tests"""
        # Basic equality tests
        self.assertEqual(2 + 2, 4)
        self.assertNotEqual(2 + 2, 5)

        # For float - use assertAlmostEqual
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
        self.assertNotAlmostEqual(0.1 + 0.2, 0.4, places=7)

    def test_truth_assertions(self):
        """Truth/false tests"""
        self.assertTrue(True)
        self.assertFalse(False)

        # None checks
        value = None
        self.assertIsNone(value)

        value = "not none"
        self.assertIsNotNone(value)

    def test_identity_assertions(self):
        """Object identity tests"""
        a = [1, 2, 3]
        b = a  # same reference
        c = [1, 2, 3]  # different reference, same value

        self.assertIs(a, b)  # same reference
        self.assertIsNot(a, c)  # different reference
        self.assertEqual(a, c)  # but equal values

    def test_membership_assertions(self):
        """Membership tests"""
        container = [1, 2, 3, 4, 5]

        self.assertIn(3, container)
        self.assertNotIn(6, container)

        # For strings
        text = "Hello World"
        self.assertIn("Hello", text)
        self.assertNotIn("Python", text)

    def test_comparison_assertions(self):
        """Comparison tests"""
        self.assertGreater(10, 5)
        self.assertGreaterEqual(10, 10)
        self.assertLess(5, 10)
        self.assertLessEqual(5, 5)

    def test_sequence_assertions(self):
        """Sequence tests"""
        list1 = [1, 2, 3]
        list2 = [1, 2, 3]
        list3 = [3, 2, 1]

        self.assertListEqual(list1, list2)
        self.assertCountEqual(list1, list3)  # ignores order

    def test_string_assertions(self):
        """String tests"""
        text = "Hello Python World"

        # Pattern matching
        import re
        self.assertRegex(text, r"P.*n")
        self.assertNotRegex(text, r"^Java")

        # Start/End
        self.assertTrue(text.startswith("Hello"))
        self.assertTrue(text.endswith("World"))

    def test_exception_assertions(self):
        """Exception tests"""
        # Test if exception is raised
        with self.assertRaises(ZeroDivisionError):
            result = 10 / 0

        # Test specific message
        with self.assertRaises(ValueError) as cm:
            int("not a number")

        # Check error message
        self.assertIn("invalid literal", str(cm.exception))
