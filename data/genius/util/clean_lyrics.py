import pandas as pd
import re

def clean_lyrics(lyrics):
    lyrics = re.sub(r'\[Intro:?\s*(.*?)\]', 'Intro:', lyrics)

    lyrics = re.sub(r'\[Chrous:?\s*(.*?)\]', 'Chorus:', lyrics)

    lyrics = re.sub(r'\[Outro:?\s*(.*?)\]', 'Outro:', lyrics)

    lyrics = re.sub(r'\[Verse\s+(\d+):?\s*(.*?)\]', r'Verse \1:', lyrics)
    lyrics = lyrics.strip('[]')
    lyrics = re.sub(r'\[.*?\]', '', lyrics)
    lyrics = lyrics.replace(']', '')
    lyrics = lyrics.replace('[', '')
    lyrics = lyrics.replace('u205f', ' ')

    return '['+lyrics+']'

def remove_short_entries(df, column_name, min_length=10):
  filtered_df = df[df[column_name].str.len() >= min_length]

  return filtered_df

def remove_leading_backslash_n(entry):
    entry = re.sub(r"^\[\'\\n", '[\'', entry)
    entry = re.sub(r"^\[\"\\n", '[\"', entry)
    return entry

def replace_multiple_literal_backslash_n(entry):
    pattern = r'(\\n){2,}'
    entry = re.sub(pattern, '\\\\n', entry)
    return entry

def format_lyrics(entry):
    entry = re.sub(r'Intro:', '[Intro]', entry)
    entry = re.sub(r'Chorus:', '[Chorus]', entry)
    entry = re.sub(r'Outro:', '[Outro]', entry)
    entry = re.sub(r'Verse (\d+):', r'[Verse \1]', entry)

    return entry


df = pd.read_csv('../data_files/lyrics_dataset.csv', encoding='utf-8')

df['song_lyrics'] = df['song_lyrics'].apply(clean_lyrics)
filtered_df = remove_short_entries(df.copy(), 'song_lyrics')
filtered_df['song_lyrics'] = filtered_df['song_lyrics'].apply(replace_multiple_literal_backslash_n)
filtered_df['song_lyrics'] = filtered_df['song_lyrics'].apply(remove_leading_backslash_n)
filtered_df['song_lyrics'] = filtered_df['song_lyrics'].apply(format_lyrics)

filtered_df.to_csv('../data_files/lyrics_dataset_clean.csv', index=False)


