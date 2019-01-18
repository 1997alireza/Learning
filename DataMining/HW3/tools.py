import pandas as pd
from sklearn.model_selection import train_test_split


def print_itemsets(itemsets):
    for ik in itemsets:
        print([i.items for i in ik])


def extract_dataset(dataset_address, need_validation=False):
    dataset = pd.read_csv(dataset_address)
    dataset = dataset.iloc[:, :].values
    if need_validation:
        train_size = .5
    else:
        train_size = .75
    train, others = train_test_split(dataset, test_size=1-train_size)
    if need_validation:
        test, validation = train_test_split(others, test_size=0.5)
        return train, test, validation
    return train, others


def frange(start, end=None, inc=None):
    if end is None:
        end = start + 0.0
        start = 0.0

    if inc is None:
        inc = 1.0

    r = []
    while 1:
        next = start + len(r) * inc
        if inc > 0 and next >= end:
            break
        elif inc < 0 and next <= end:
            break
        r.append(next)

    return r
