import pandas as pd

lyrics_df = pd.read_csv('../data_files/cleaned_lyrics.csv')
annotations_df = pd.read_csv('../data_files/cleaned_annotations.csv')


data1 = ['id', 'song', 'artist', 'album', 'release_date', 'song_description', 'song_lyrics']
data2 = ['id', 'song', 'artist', 'album', 'release_date', 'referent', 'annotation']
mask1 = (lyrics_df == data1).all(axis=1)
mask2 = (annotations_df == data2).all(axis=1)
lyrics_cleaned = lyrics_df[~mask1]
annotations_cleaned = annotations_df[~mask2]

lyrics_cleaned.to_csv('cleaned_lyrics.csv', index=False)
annotations_cleaned.to_csv('cleaned_annotations.csv', index=False)