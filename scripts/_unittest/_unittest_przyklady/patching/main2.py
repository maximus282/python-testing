# Let's add some exceptions and test them

import requests


def len_joke():
    """Calculate length of a joke fetched from API.
    
    Returns:
        Length of the joke string
    """
    joke = get_joke()
    return len(joke)


def get_joke():
    """Fetch a random Chuck Norris joke from API with exception handling.
    
    Makes HTTP request to Chuck Norris joke API with timeout and error handling.
    
    Returns:
        String containing the joke, 'No jokes' on timeout, or empty string on other errors
        
    Raises:
        UnboundLocalError: If ConnectionError occurs (joke variable not defined)
    """
    url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(url, timeout=30)
    except requests.exceptions.Timeout:
        return "No jokes"
    except requests.exceptions.ConnectionError:
        pass
    else:
        if response.status_code == 200:
            joke = response.json()['value']
        else:
            joke = ""

    return joke
