from datalabs import load_dataset
import os


def load_signal(dataset_name):
    # print(os.path.dirname(__file__))
    return load_dataset(f"{os.path.dirname(__file__)}/qomolangma.py", dataset_name)
