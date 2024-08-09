import pandas as pd

path = '../data_files/cleaned_lyrics.csv'

df = pd.read_csv(path)

if 'song_description' in df.columns:
    df['song_description'] = df['song_description'].apply(lambda x: "No description available" if x == '?' else x)

df.to_csv(path, index=False)