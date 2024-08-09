import pandas as pd

df = pd.read_csv('../data_files/annotations_dataset.csv')

filtered_df = df[~df['referent'].astype(str).str.startswith('[')]

filtered_df.to_csv('annotations_dataset_clean.csv', index=False)

print("CSV file has been filtered and saved as 'filtered_file.csv'.")