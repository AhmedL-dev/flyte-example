import pandas as pd

from flytekit import task, workflow


@task
def get_data() -> int:
    """Get the wine dataset."""
    print("Getting data")
    return 1

@task
def process_data(x: int) -> int:
    print("Processing data", x)
    return x

@task
def train_model(y: int) -> int:
    print("Training model", y)
    return y

@workflow
def training_workflow() -> int:
    # print("Starting workflow")
    x = get_data()
    y = process_data(x=x)
    return train_model(y=y)