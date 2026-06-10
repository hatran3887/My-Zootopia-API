"""
Responsible for fetching animals data from api ninjas with name
"""
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_KEY_PARAM = 'X-Api-Key'
NAME_PARAM = 'name'
REQUEST_URL = 'https://api.api-ninjas.com/v1/animals'


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    """Loads animals from api ninjas with name"""
    res = requests.get(f'{REQUEST_URL}?{API_KEY_PARAM}={API_KEY}&{NAME_PARAM}={animal_name}')
    parsed = res.json()
    return parsed
