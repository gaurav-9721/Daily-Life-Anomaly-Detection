#This script will process each day of data and convert it onto (Start time, Finish Time, Activity, Location) Format

import pandas as pd
import os
from txt_to_csv import DATASETS

#Removes milliseconds part from Time
def remove_milli_seconds(df):
    l = len(df)
    tim = list(df['Time'])
    new_time = []

    for i in range(l):
        s = tim[i].split('.')
        new_time.append(s[0])
    df['Time'] = new_time
    return df

#Removes unwanted Activities
def remove_activities(df):
    activities = ['Other_Activity'] #Add more activities in this list to remove them
    for act in activities:
        df = df[df['Activity'] != act]
    return df

#Converts data into Intervals format.
def reduce_to_intervals(a):
    df = a.copy()
    df = remove_milli_seconds(df)
    #Removing Unnecessary Activities
    df = remove_activities(df)
    l = len(df)
    start = 0
    finish = 0
    row = 0
    new_df = []

    while row < l:
        if df.iloc[start]['Activity'] != df.iloc[row]['Activity']:
            st = df.iloc[start]['Time']
            ft = df.iloc[finish]['Time']
            loc = df.iloc[start]['Location']
            act = df.iloc[start]['Activity']
            date = df.iloc[start]['Date']

            start = row
            finish = row
            new_df.append([date, st, ft, loc, act])
        else:
            finish = row
        row += 1
    st = df.iloc[start]['Time']
    ft = df.iloc[finish]['Time']
    loc = df.iloc[start]['Location']
    act = df.iloc[start]['Activity']
    date = df.iloc[start]['Date']

    start = row
    finish = row
    new_df.append([date, st, ft, loc, act])

    DF = pd.DataFrame(new_df, columns=['Date', 'Start', 'Finish', 'Location', 'Activity'])
    #print(DF[['Start', 'Finish', 'Activity']])
    return DF


def main():
    #Warning: This path may differ in your system
    dirc = r'D:\Daily Life Anomaly Detection\CASAS_DATA\HH' + DATASET + r'\daily_raw_data'
    Total_Days = len(os.listdir(dirc))

    processed_day_count = 1
    raw_data_day_count = 1
    while d <= Total_Days:
        read_path = r'CASAS_DATA\HH' + DATASET + r'\daily_raw_data\Day' + str(raw_data_day_count) + r'.csv'
        save_path = r'CASAS_DATA\HH' + DATASET + r'\processed_data\Day' + str(processed_day_count) + r'.csv'

        df = pd.read_csv(read_path)
        try:
            df = reduce_to_intervals(df)
            df.to_csv(save_path, index=False)
            print(save_path, 'written successfully.')
            processed_day_count += 1
        except:
            print('Error in day', raw_data_day_count)
        raw_data_day += 1


if __name__ == '__main__':
    DATASET = ''

    # This will Run script for all Datasets HH101-HH130
    for d in DATASETS:
        DATASET = d
        main()

    # If you want to run script for few chosen datasets only. Use this code.
    # for d in ['101', '104','121']: #Add datasets in this list
    #     DATASET = d
    #     main()

