# Mock z parametrem spec - ograniczanie dostępnych atrybutów
import unittest


class JokeAPI:
    """Przykładowa klasa API do mockowania"""

    def fetch_joke(self):
        return "Chuck Norris joke"

    def get_status(self):
        return "OK"


class TestJokeAPIWithSpec(unittest.TestCase):
    ...


if __name__ == "__main__":
    unittest.main()
