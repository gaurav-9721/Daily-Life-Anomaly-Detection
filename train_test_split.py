import pandas as pd
import numpy as np
import os

def save(start, days, destination, dataset):
    day = 1
    while day < days:
        readpath = 'CASAS_DATA\\' + dataset + '\processed_data\Day' + str(
            day + start) + '.csv'
        savepath = 'CASAS_DATA\\' + dataset + '\\' + destination + '\\Day' + str(
            day) + '.csv'
        df = pd.read_csv(readpath)
        df.to_csv(savepath, index=False)
        print(savepath, 'written successfully.')
        day += 1


def train_test_split(N):
    ratio = 0.75
    train = int(ratio * N)
    test = N - train

    return train, test


def split_dataset(dataset):
    dirc1 = 'CASAS_DATA\\' + dataset + '\processed_data'
    dirc2 = 'CASAS_DATA\\' + dataset + '\\filling'

    N = len(os.listdir(dirc1))
    train, test = train_test_split(N)
    save(1, train, 'train_data', dataset)
    save(train + 1, test, 'test_data', dataset)

    N = len(os.listdir(dirc2))
    train, test = train_test_split(N)
    save(1, train, 'filling_train', dataset)
    save(train + 1, test, 'filling_test', dataset)


Datsets = ['HH'+str(x) for x in range(101, 131)]
for data in Datsets:
    split_dataset(data)