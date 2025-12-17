# Mocki - jeżeli mamy zależności zaprojekowane zgodnie z dobrymi praktykami powinny wystarczyć
import requests

def len_joke(get_joke_function):
    """Calculate length of a joke using dependency injection.
    
    Args:
        get_joke_function: Function that returns a joke string
        
    Returns:
        Length of the joke string
    """
    joke = get_joke_function()
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
    print(len_joke(get_joke))
