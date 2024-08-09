import csv
from album import Album
from scraper import scrape_song_names, scrape_album_names
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)

load_dotenv()
token = os.getenv('CLIENT_ACCESS_TOKEN')

file_path = "rappers.txt"
artists = []
with open(file_path, 'r') as file:
    for line in file:
        artist = line.strip()
        artists.append(artist)

logging.info(f"Created artist list with length {len(artists)}")
data1 = ['id', 'song', 'artist', 'album', 'release_date', 'song_description', 'song_lyrics']
data2 = ['id', 'song', 'artist', 'album', 'release_date', 'referent', 'annotation']

with open('data_files/lyrics.csv', mode='a', newline='') as file1, open('data_files/annotations.csv', mode='a', newline='') as file2:
    writer1 = csv.writer(file1)
    writer2 = csv.writer(file2)

    writer1.writerow(data1)
    writer2.writerow(data2)

    for artist in artists:
        album_names = scrape_album_names(artist)
        logging.info(f'Scraped album names for {artist}')
        for album_name in album_names:
            song_names = scrape_song_names(artist, album_name)
            logging.info(f'Scraped songs names for {album_name}')
            if len(song_names) > 10:
                album = Album(album_name, artist, song_names, token)
                logging.info('Created album')
            else:
                continue
            for song in album.songs:
                data1 = [song.id, song.title, song.artist, album.name, song.date, song.description, song.lyrics]
                writer1.writerow(data1)
                dict = song.annotations
                for referent, annotation in dict.items():
                    data2 = [song.id, song.title, song.artist, album.name, song.date, referent, annotation]
                    writer2.writerow(data2)
                logging.info(f'Added data for {song.title}')
            logging.info(f'Added the songs for {album.name} in the data list')

print("Csv files created")

