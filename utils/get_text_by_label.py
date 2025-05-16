import os
import random
import pandas as pd
from better_profanity import profanity

from utils.get_data_path import get_data_path


def get_clean_sample(filtered_df, text_column_index):
    while True:
        row = filtered_df.sample(n=1, random_state=None)
        if pd.isna(row.iloc[0, text_column_index]):
            continue
        text = row.iloc[0, text_column_index]
        if not profanity.contains_profanity(str(text)):
            return str(text)



# a util function which gets random texts from a csv file.
# cls_type - topic to classify, spam / sentiment.
# label - the label in the csv file, spam / ham for spam, 0 / 4 for sentiment.
# TODO: get positive / negative as label and convert here to 0 / 4
# count - how many texts to return.
# text_column_index - the index of the text column in the csv file.
# TODO: figure text_column_index here instead of getting it as a parameter
# set_filename - get the random texts from a specific file (for testing and balance)
def get_texts_by_label(cls_type, label, count, text_column_index, set_filename=None):
    dpath = get_data_path(cls_type)
    filename = set_filename if set_filename else random.choice(os.listdir(dpath))
    df = pd.read_csv(f'{dpath}/{filename}', encoding='latin1')
    filtered_df = df[df.iloc[:, 0].astype(str) == str(label)]

    random_samples = []
    while len(random_samples) < count:
        sample = get_clean_sample(filtered_df, text_column_index)
        random_samples.append(sample)

    return random_samples