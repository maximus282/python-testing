# Spy
# Mock z parametrem wraps - częściowe mockowanie
import unittest


class JokeAPI:
    """Przykładowa klasa API do mockowania"""

    def fetch_joke(self):
        return "Chuck Norris counted to infinity twice"

    def get_status(self):
        return "OK"

    def log_request(self):
        print("API request logged")


class TestJokeAPIWithWraps(unittest.TestCase):
    ...


if __name__ == "__main__":
    unittest.main()
