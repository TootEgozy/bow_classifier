import os
import random
import pandas as pd

def get_data_path(label):
    # Get the absolute path of the current script file
    current_script_dir = os.path.dirname(os.path.abspath(__file__))


    # Navigate up to the root directory of the project
    root_dir = os.path.dirname(current_script_dir)

    # Construct the path to the learning_data folder
    learning_data_path = os.path.join(root_dir, 'learning_data', label)
    return learning_data_path


def get_texts_by_label(label, count):
    dpath = get_data_path(label)
    filename = random.choice(os.listdir(dpath))
    df = pd.read_csv(f'{dpath}/{filename}', encoding='latin1')
    filtered_df = df[df.iloc[:, 0] == label]
    random_samples = filtered_df.sample(n=count, random_state=None).iloc[:, 1].dropna().tolist()
    return random_samples