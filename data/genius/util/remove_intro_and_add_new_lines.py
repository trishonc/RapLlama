import pandas as pd
import re

df = pd.read_csv('../data_files/final_lyrics_dataset.csv')

def remove_intro_to_verse1(lyrics):
    pattern = r'\[Intro].*?\[Verse 1]'
    modified_lyrics = re.sub(pattern, '[Verse 1]', lyrics, flags=re.DOTALL)
    return modified_lyrics

def remove_newlines_parentheses(text):
    text = re.sub(r'\(\n+', '(', text)
    text = re.sub(r'\n+\)', ')', text)
    return text

#df['song_lyrics'] = df['song_lyrics'].str.replace('\\n', '\n')
df['song_lyrics'] = df['song_lyrics'].apply(remove_newlines_parentheses)
df.to_csv('../data_files/final_lyrics_dataset4.csv', index=False)


