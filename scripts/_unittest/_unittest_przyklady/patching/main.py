# But we don't always deal with clean code (loose coupling).
import requests
import unittest


def len_joke():
    """Calculate length of a joke fetched from API.
    
    Returns:
        Length of the joke string
    """
    joke = get_joke()
    return len(joke)


def get_joke():
    """Fetch a random Chuck Norris joke from API.
    
    Makes HTTP request to Chuck Norris joke API and returns the joke text.
    
    Returns:
        String containing the joke, or empty string if request fails
    """
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()['value']
    else:
        joke = ""

    return joke


if __name__ == "__main__":
    unittest.main()
