import unittest


class TestFactorial(unittest.TestCase):
    
    def test_factorial_zero(self):
        """Test that factorial of zero returns one"""
        assert False  # TODO: Replace with proper assertion
    
    def test_factorial_small_numbers(self):
        """Test factorials for small numbers: 1! through 5!"""
        assert False  # TODO: Test factorial(1) through factorial(5)
    
    def test_factorial_five_specific(self):
        """Test specifically that factorial of 5 returns 120"""
        assert False  # TODO: Test factorial(5) is equal 120
    
    def test_negative_number_raises_error(self):
        """Test that negative number raises ValueError with appropriate message"""
        assert False  # TODO: Test that factorial(-1) raises ValueError
    
    def test_non_integer_float_raises_error(self):
        """Test that non-integer float raises ValueError"""
        assert False  # TODO: Test that factorial(30.1) raises ValueError
    
    def test_integer_float_works(self):
        """Test that integer float works the same as integer"""
        assert False  # TODO: Test that factorial(5.0) works correctly
    
    def test_very_large_number_raises_error(self):
        """Test that very large number raises OverflowError"""
        assert False  # TODO: Test that factorial(1e100) raises OverflowError


if __name__ == '__main__':
    unittest.main()
