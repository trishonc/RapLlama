from datasets import load_dataset, concatenate_datasets, Dataset
import pandas as pd


def preprocess_function(example, dataset_type):
    themes = example['themes'].strip()
    system_message = "You are a song writing assistant. You always write good lyrics based on the context provided."
    input_variations = {
        'lyrics': [
            f'Generate lyrics for a full rap song on the following topics: {themes}.',
            f'Write a rap song about: {themes}.',
            f'Create a rap track focused on: {themes}.'
        ],
        'annotations': [
            f'Generate rap lyrics on these topics: {themes}',
            f'Create a small portion of a rap song focusing on {themes}',
            f'Write some rap bars about {themes}'
        ]
    }

    responses = {
        'lyrics': example.get('song_lyrics'),
        'annotations': example.get('referent')
    }

    expanded_entries = []
    for i in range(3):
        expanded_entries.append({
            'system_message': system_message,
            'instruction': input_variations[dataset_type][i],
            'response': responses[dataset_type]
        })

    return expanded_entries


def expand_dataset_to_pandas(dataset, dataset_type):
    all_expanded_entries = []
    for example in dataset:
        expanded_entries = preprocess_function(example, dataset_type)
        all_expanded_entries.extend(expanded_entries)

    return pd.DataFrame(all_expanded_entries)


lyrics_path = '../data_files/final_lyrics_dataset.csv'
annotations_path = '../data_files/final_annotations_dataset.csv'

lyrics_dataset = load_dataset('csv', data_files=lyrics_path)['train']
annotations_dataset = load_dataset('csv', data_files=annotations_path)['train']

expanded_lyrics_df = expand_dataset_to_pandas(lyrics_dataset, 'lyrics')
expanded_annotations_df = expand_dataset_to_pandas(annotations_dataset, 'annotations')

combined_df = pd.concat([expanded_lyrics_df, expanded_annotations_df], ignore_index=True)

combined_dataset = Dataset.from_pandas(combined_df)

combined_dataset.to_csv('../data_files/dataset.csv')
