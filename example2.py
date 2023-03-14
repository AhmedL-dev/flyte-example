import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression

import flytekit.extras.sklearn
from flytekit import task, workflow


@task
def get_data() -> pd.DataFrame:
    """Get the wine dataset."""
    print("Getting data")
    return pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

@task
def process_data(data: pd.DataFrame) -> pd.DataFrame:
    print("Processing data")
    return data

@task
def train_model(data: pd.DataFrame, hyperparameters: dict) -> pd.DataFrame:
    print("Training model")
    return data

@workflow
def training_workflow(hyperparameters: dict) -> pd.DataFrame:
    """Put all of the steps together into a single workflow."""
    data = get_data()
    processed_data = process_data(data=data)
    return train_model(
        data=processed_data,
        hyperparameters=hyperparameters,
    )