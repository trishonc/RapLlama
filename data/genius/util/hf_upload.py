from datasets import Dataset

dataset = Dataset.from_csv('../data_files/final_annotations_dataset.csv')

dataset.push_to_hub('trishonc/rap-lyrics-annotations')