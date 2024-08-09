import pandas as pd

df = pd.read_csv('../data_files/final_lyrics_dataset2.csv')


def remove_rows_by_index(df, index_list):
    index_list = list(set(index_list))

    new_df = df.drop(index=index_list).reset_index(drop=True)
    return new_df


nums = [604, 605, 606, 607, 609, 2202]
new_df = remove_rows_by_index(df, nums)

new_df.to_csv('../data_files/final_lyrics_dataset.csv')