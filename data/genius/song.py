import requests.cookies
from bs4 import BeautifulSoup
from genius import Genius
import os
from dotenv import load_dotenv

def extract_text(node):
    if isinstance(node, str):
        return node
    elif isinstance(node, dict):
        if 'children' in node:
            return ''.join(extract_text(child) for child in node['children'])
    elif isinstance(node, list):
        return ''.join(extract_text(item) for item in node)
    return ''

class SongInitializationError(Exception):
    pass

class Song(Genius):
    def __init__(self, name, artist, access_token):
        super().__init__(access_token)
        self.song_info = super().get_song_info(name, artist)
        if self.song_info is None:
            raise SongInitializationError(f'Song info not found for {name} by {artist}')
        self.id = self.song_info['id']
        self.artist = self.song_info['artist_names']
        self.title = self.song_info['title']
        self.date = self.song_info['release_date_for_display']
        self.description = Song.get_description(self)
        self.url = self.song_info['url']
        self.lyrics = Song.get_lyrics(self)
        self.annotations = Song.get_annotations(self)
    def get_description(self):
        url = self.base_url+self.song_info['api_path']

        response = requests.get(url, headers=self.headers)
        json_response = response.json()

        description = extract_text(json_response['response']['song']['description']['dom'])

        return description
    def get_lyrics(self) -> list:
        response = requests.get(self.url)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')

        divs = soup.select('div.Lyrics__Container-sc-1ynbvzw-1.kUgSbL')

        lyrics = []

        for div in divs:
            lyric = div.get_text(separator='<newline>', strip=True).replace('\u2005', ' ')
            lyrics.append(lyric)

        return lyrics

    def get_annotations(self) -> dict:
        dict = {}
        annotations = []
        referents = []

        url = f'{self.base_url}/referents'
        params = {'song_id': self.id, 'per_page': '50'}
        response = requests.get(url, params=params, headers=self.headers)
        json_response = response.json()
        items = json_response['response']['referents']

        for item in items:
            referents.append(item['fragment'])
            annotations.append(extract_text(item['annotations'][0]['body']['dom']))

        for referent, annotation in zip(referents, annotations):
            dict[referent] = annotation
        return dict
    def info(self):
        print(f' artist: {self.artist}\n title: {self.title}\n id: {self.id}\n url: {self.url}')


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('CLIENT_ACCESS_TOKEN')
    song = Song('a lot', '21 savage', token)
    song.info()
