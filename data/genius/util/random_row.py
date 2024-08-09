import csv
import random


def random_select_and_save(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        headers = next(reader)
        writer.writerow(headers)

        buffer = []

        for row in reader:
            buffer.append(row)
            if len(buffer) == 3:
                selected_row = random.choice(buffer)
                writer.writerow(selected_row)
                buffer = []

input_csv_file = '../data_files/dataset.csv'  
output_csv_file = '../data_files/train_data.csv'  
random_select_and_save(input_csv_file, output_csv_file)