from datasets import load_dataset, Features, Value
import pandas as pd


lyrics_df = pd.read_csv('../data_files/cleaned_lyrics.csv', encoding='utf-8')
annotations_df = pd.read_csv('../data_files/cleaned_annotations.csv', encoding='utf-8')



lyrics_df = lyrics_df.drop(['id', 'album', 'release_date'], axis=1)
annotations_df = annotations_df.drop(['id', 'album', 'release_date'], axis=1)

cleaned_file_path = '../data_files/lyrics_dataset.csv'
lyrics_df.to_csv(cleaned_file_path, index=False)
cleaned_file_path = '../data_files/annotations_dataset.csv'
annotations_df.to_csv(cleaned_file_path, index=False)



