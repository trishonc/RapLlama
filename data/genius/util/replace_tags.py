import pandas as pd

df = pd.read_csv('../data_files/final_annotations_dataset.csv')

def replace_tags(text):
    if isinstance(text, str):
        text = text.replace('_', ' ')
    return text  

df['themes'] = df['themes'].apply(replace_tags)
#df['song_description'] = df['song_description'].apply(replace_tags)

df.to_csv('../data_files/final_annotations_dataset.csv', index=False)
