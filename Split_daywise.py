#This script will Spilt whole data into days. Original data has many days of data in a single file.

import pandas as pd
from txt_to_csv import DATASETS

def main():
    data = pd.read_csv('CSV_Datasets/hh' + DATASET + r'.csv')
    date_set = set()
    Dates = []

    for date in data['Date']:
        if date not in date_set:
            Dates.append(date)
            date_set.add(date)

    day = 1
    #Warning: This path may differ in your computer
    savepath = r'CASAS_DATA\HH' + DATASET + r'\daily_raw_data'

    for date in Dates:
        savepath = r'CASAS_DATA\HH' + DATASET + r'\daily_raw_data\Day' + str(
            day) + r'.csv'
        df = data[data['Date'] == date]
        df.to_csv(savepath, index=True)
        print(savepath)
        day += 1

if __name__ == '__main__':
    DATASET = ''

    #This will Run script for all Datasets HH101-HH130
    for d in DATASETS:
        DATASET = d
        main()

    # If you want to run script for few chosen datasets only. Use this code
    # for d in ['101', '104','121']:
    #     DATASET = d
    #     main()

