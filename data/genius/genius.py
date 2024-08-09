import requests
import os
from dotenv import load_dotenv
import re

def clean_song_name(song_name):
    pattern = r'\s*(?:\(?(?:ft\.|featuring)\s+[^\)]+\)?)|\s+by\s+\S.*'

    cleaned_name = re.sub(pattern, '', song_name, flags=re.IGNORECASE)

    return cleaned_name.strip()

class Genius():
    def __init__(self, access_token):
        self.base_url = 'https://api.genius.com'
        self.token = access_token
        self.headers = {'Authorization': f'Bearer {self.token}'}

    def get_artist_info(self, artist_name):
        search_url = f'{self.base_url}/search'
        params = {'q': artist_name}

        response = requests.get(search_url, headers=self.headers, params=params)

        if response.status_code == 200:
            json_response = response.json()
            hits = json_response['response']['hits']

            for hit in hits:
                if hit['result']['primary_artist']['name'].lower() == artist_name.lower():
                    return hit['result']['primary_artist']

            return None
        else:
            print(f'Error: {response.status_code}')
            return None
    def get_song_info(self, name, artist):
        url = f'{self.base_url}/search'
        name = clean_song_name(name)
        params = {'q': f'{artist} {name}'}

        response = requests.get(url, params=params, headers=self.headers)

        if response.status_code == 200:
            json_response = response.json()
            hits = json_response['response']['hits']
            for hit in hits:
                artist_result = hit['result']['artist_names'].lower()
                artist_input = artist.lower()
                if artist_input in artist_result:
                    return hit['result']
                else: print(f'{artist_input} != {artist_result}')
            return None

if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('CLIENT_ACCESS_TOKEN')
    genius = Genius(token)
    song = genius.get_song_info('Seduction')
    print(song)
