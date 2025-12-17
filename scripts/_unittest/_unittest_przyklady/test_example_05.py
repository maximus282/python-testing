# Test suites - manual organization/grouping of tests
import unittest


class FastTests(unittest.TestCase):
    """Fast unit tests"""

    def test_fast_math_add(self):
        self.assertEqual(2 + 2, 4)

    def test_fast_string_upper(self):
        self.assertEqual("hello".upper(), "HELLO")


class SlowTests(unittest.TestCase):
    """Slower integration tests"""

    def test_slow_operation(self):
        """Simulation of slow operation"""
        import time
        time.sleep(0.1)  # Simulation
        self.assertTrue(True)

    def test_file_operation(self):
        """Simulation of file operation"""
        import tempfile
        import os

        # Creating temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("test content")
            temp_file = f.name

        try:
            # Check if file exists
            self.assertTrue(os.path.exists(temp_file))

            # Check content
            with open(temp_file, 'r') as f:
                content = f.read()
            self.assertEqual(content, "test content")
        finally:
            # Cleanup
            os.remove(temp_file)
