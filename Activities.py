# Extract Activity data from all days and save it into a separate file

import pandas as pd
import os
from txt_to_csv import DATASETS

#Convert 'hh::mm:ss' into floating value in hours
def startTime(s):
    h, m, sec = map(int, s.split(':'))
    hrs = h + m / 60
    hrs = float('%.2f' % hrs)
    return hrs

#Convert 'hh::mm:ss' into floating value of minutes
def duration(s, f):
    s = startTime(s)
    f = startTime(f)
    m = (f - s) * 60
    m = float('%.2f' % m)
    return m

#Add data in Lists of Start Time, Duration and Location
def add_Activity(df, activities, Start, Duration, Location):
    l = len(df)
    for row in range(l):
        if df.iloc[row]['Activity'] in activities:
            start, finish, loc  = df.iloc[row]['Start'], df.iloc[row]['Finish'], df.iloc[row]['Location']
            Start.append(startTime(start))
            Duration.append(duration(start, finish))
            Location.append(loc)


#Save activity file in csv format
def save_activity(act, start, duration, location):
    save_path = r'CASAS_DATA\HH' + DATASET + r'\Filled_Activites'  + '\\'  + act + r'.csv'
    #adaptive_save_path = r'D:\Daily Life Anomaly Detection\CASAS_DATA\HH' + DATASET + r'\Filled_Activites\Adaptive_' + act + r'.csv'
    activity = pd.DataFrame({'Start_Time': start, 'Duration': duration, 'Location': location})
    activity.to_csv(save_path, index=False)
    #activity.to_csv(adaptive_save_path, index=False)
    print(save_path, 'written successfully.')
    #print(adaptive_save_path, 'written successfully.')


def main():
    #Warning: This path may differ in your system
    dirc = r'CASAS_DATA\HH' + DATASET+ r'\filling_train'
    Days = len(os.listdir(dirc))

    #Lists of each activity. To add more activities, add 3 lists for Starttime, Duration and Location here
    Eat_Start_time, Eat_duration, Eat_Location = [], [], []
    Sleep_Start_time, Sleep_Duration, Sleep_Location = [], [], []
    Medicine_Start_time, Medicine_Duration, Medicine_Location = [], [], []

    for day in range(1, Days + 1):
        read_path = r'CASAS_DATA\HH' + DATASET+ r'\filling_train\Day' + str(day) + r'.csv'
        df = pd.read_csv(read_path)

        #Adding data in Lists for each activity
        #Note: 2nd Argument in this function is a list of labels for each activities.
        add_Activity(df, ['Eat', 'Eat_Breakfast', 'Eat_Dinner', 'Eat_Lunch'], Eat_Start_time, Eat_duration, Eat_Location)
        add_Activity(df, ['Sleep'], Sleep_Start_time, Sleep_Duration, Sleep_Location)
        add_Activity(df, ['Morning_Meds', 'Evening_Meds', 'Take_Medicine', 'Medicine'], Medicine_Start_time, Medicine_Duration, Medicine_Location)

    #Set default duration of Medicine to 2mins in all data
    MedicineD = [2 for x in range(len(Medicine_Start_time))]

    #Saving each activity in a separate file
    save_activity('Eat', Eat_Start_time, Eat_duration, Eat_Location)
    save_activity('Sleep', Sleep_Start_time, Sleep_Duration, Sleep_Location)
    save_activity('Medicine',Medicine_Start_time, Medicine_Duration, Medicine_Location)


if __name__  == '__main__':
    DATASET = ''

    # This will Run script for all Datasets HH101-HH130
    for d in DATASETS:
        DATASET = d
        main()

    # If you want to run script for few chosen datasets only. Use this code.
    # for d in ['101', '104','121']: #Add datasets in this list
    #     DATASET = d
    #     main()

#List of All activities
""" 
{'Bathe',
 'Bed_Toilet_Transition',
 'Cook',
 'Cook_Breakfast',
 'Cook_Dinner',
 'Cook_Lunch',
 'Dress',
 'Drink',
 'Eat',
 'Eat_Breakfast',
 'Eat_Dinner',
 'Eat_Lunch',
 'Enter_Home',
 'Entertain_Guests',
 'Evening_Meds',
 'Groom',
 'Leave_Home',
 'Morning_Meds',
 'Other_Activity',
 'Personal_Hygiene',
 'Phone',
 'Read',
 'Relax',
 'Sleep',
 'Step_Out',
 'Toilet',
 'Wash_Breakfast_Dishes',
 'Wash_Dinner_Dishes',
 'Wash_Dishes',
 'Wash_Lunch_Dishes',
 'Watch_TV',
 'Work',
 'Work_At_Desk',
 'Work_At_Table',
 'Work_On_Computer'}
"""
