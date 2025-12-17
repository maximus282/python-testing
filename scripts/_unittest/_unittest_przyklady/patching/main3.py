# Replace manual exception checking with `raise_for_status` (recommended by requests creators)
import requests


def len_joke():
    """Calculate length of a joke fetched from API.
    
    Returns:
        Length of the joke string
    """
    joke = get_joke()
    return len(joke)

def get_joke():
    """Fetch a random Chuck Norris joke from API using raise_for_status.
    
    Makes HTTP request to Chuck Norris joke API with proper error handling
    using raise_for_status() method.
    
    Returns:
        String containing the joke, 'No jokes' on timeout, 
        'HTTPError was raised' on HTTP errors, or empty string on other errors
        
    Raises:
        UnboundLocalError: If ConnectionError occurs (joke variable not defined)
    """
    url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

    except requests.exceptions.Timeout:
        return "No jokes"
    except requests.exceptions.ConnectionError:
        pass

    except requests.exceptions.HTTPError:
        return "HTTPError was raised"

    else:
        if response.status_code == 200:
            joke = response.json()['value']
        else:
            joke = ""

    return joke
