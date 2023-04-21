# Relative files
import os

# Environment variables
from dotenv import load_dotenv

# To contact Instagram's API
import requests


load_dotenv()


def getUsername():
    return os.getenv('USER')


def getHeaders():
    return {'cookie': os.getenv('COOKIE')}


def getUserID():
    USERNAME = getUsername()
    HEADERS = getHeaders()
    URL = f"https://www.instagram.com/web/search/topsearch/?query=${USERNAME}"
    response = requests.get(url=URL, headers=HEADERS)

    return response.json()['users'][0]['user']['pk']
