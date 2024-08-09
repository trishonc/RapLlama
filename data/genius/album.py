from song import Song
from song import SongInitializationError
from concurrent.futures import ThreadPoolExecutor
import threading

class Album():
    def __init__(self, name, artist, song_names, access_token):
        self.name = name
        self.artist = artist
        self.token = access_token
        self.lock = threading.Lock()
        self.songs = Album.get_songs(self, song_names)

    def create_song(self, song_name):
        if 'instrumental' in song_name.lower():
            return None
        try:
            song = Song(song_name, self.artist, self.token)
            with self.lock:
                return song
        except SongInitializationError as e:
            print(e)
            return None

    def get_songs(self, song_names) -> list:
        songs = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_songs = [executor.submit(self.create_song, name) for name in song_names]
            for future in future_songs:
                song = future.result()
                if song is not None:
                    songs.append(song)
        return songs
