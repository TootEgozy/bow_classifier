import os


def get_data_path(cls_type):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    learning_data_path = os.path.join(root_dir, f'learning_data\\{cls_type}')

    return learning_data_path