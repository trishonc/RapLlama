import pandas as pd

lyrics_df = pd.read_csv('../data_files/lyrics.csv')
annotations_df = pd.read_csv('../data_files/annotations.csv')

lyrics_cleaned = lyrics_df.drop_duplicates(subset=['song', 'artist'])
annotations_cleaned = annotations_df.drop_duplicates(subset=['referent'])

lyrics_cleaned.to_csv('cleaned_lyrics.csv', index=False)
annotations_cleaned.to_csv('cleaned_annotations.csv', index=False)
