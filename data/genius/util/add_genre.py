import pandas as pd

lyrics_df = pd.read_csv('../data_files/lyrics.csv')
annotations_df = pd.read_csv('../data_files/annotations.csv')

position1 = lyrics_df.columns.get_loc("song") + 1
position2 = annotations_df.columns.get_loc("song") + 1

lyrics_df.insert(position1, 'genre', 'rap')
annotations_df.insert(position2, 'genre', 'rap')

lyrics_df.to_csv('cleaned_lyrics.csv', index=False)
annotations_df.to_csv('cleaned_annotations.csv', index=False)
