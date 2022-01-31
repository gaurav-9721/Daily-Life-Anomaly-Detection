#Data Cleaning: Remove days which have activities missing

import pandas as pd
import os
from txt_to_csv import DATASETS

eat = ['Eat', 'Eat_Breakfast', 'Eat_Lunch', 'Eat_Dinner']
sleep = ['Sleep']
med = ['Morning_Meds', 'Evening_Meds']
A = {'Eat': eat,  'Sleep': sleep, 'Medicine': med}

#Returns True if Activities are present, false if missing.
def frequency(df):
    eat_df = df[df['Activity'].isin(eat)]
    sleep_df = df[df['Activity'].isin(sleep)]
    med_df = df[df['Activity'].isin(med)]

    e = len(eat_df)
    s = len(sleep_df)
    m = len(med_df)

    if e > 0 and s == 2 and m == 2:
        return True
    else:
        return False

def main():
    dirc = r'CASAS_DATA\HH' + DATASET + r'\processed_data'
    Days = len(os.listdir(dirc))

    clean = 1

    for day in range(1, Days + 1):
        read_path = r'CASAS_DATA\HH' + DATASET + r'\processed_data\Day' + str(
            day) + r'.csv'x
        df = pd.read_csv(read_path)

        if frequency(df):
            savepath = r'CASAS_DATA\HH' + DATASET + r'\cleaned\Day' + str(
                clean) + r'.csv'
            df.to_csv(savepath, index=False)
            clean += 1
            print(savepath, 'writtern successfully')


if __name__  == '__main__':
    DATASET = ''

    for d in DATASETS:
        DATASET = d
        main()