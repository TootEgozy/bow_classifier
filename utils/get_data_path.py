import os

# get the full path for the csv data folder within learning_data folder
def get_data_path(cls_type):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    learning_data_path = os.path.join(root_dir, 'learning_data', cls_type)
    return learning_data_path