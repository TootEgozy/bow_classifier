import os
import random
import pandas as pd

from utils.get_data_path import get_data_path


def get_texts_by_label(cls_type, label, count):
    dpath = get_data_path(cls_type)
    filename = random.choice(os.listdir(dpath))
    df = pd.read_csv(f'{dpath}/{filename}', encoding='latin1')
    filtered_df = df[df.iloc[:, 0] == label]
    random_samples = filtered_df.sample(n=count, random_state=None).iloc[:, 1].dropna().tolist()
    return random_samples