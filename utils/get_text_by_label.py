import os
import random
import pandas as pd

from utils.get_data_path import get_data_path


def get_texts_by_label(cls_type, label, count, text_column_index, set_filename=None):
    dpath = get_data_path(cls_type)
    filename = set_filename if set_filename else random.choice(os.listdir(dpath))
    df = pd.read_csv(f'{dpath}/{filename}', encoding='latin1')
    print(' ')
    print(df.head())
    filtered_df = df[df.iloc[:, 0] == label]
    random_samples = filtered_df.sample(n=count, random_state=None).iloc[:, text_column_index].dropna().tolist()
    return random_samples