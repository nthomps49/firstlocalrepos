import requests
import webbrowser

search_term = input("Enter what you are looking for: ")

URL = 'https://www.youtube.com/search'

PARAMS = {'q': search_term}

r_get = requests.get(url = URL, params = PARAMS)

webbrowser.open(r_get.url)