import os
import random
import pandas as pd

def get_texts_by_label(label, count, cls_type):
    texts = set()
    filename = random.choice(os.listdir(f'learning_data/{cls_type}'))
    df = pd.read_csv(f'learning_data/{cls_type}/{filename}', encoding='latin1')
    filtered_df = df[df.iloc[:, 0] == label]
    random_samples = filtered_df.sample(n=count, random_state=None).iloc[:, 1].dropna().tolist()
    return random_samples