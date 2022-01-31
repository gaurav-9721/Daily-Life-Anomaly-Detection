import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

ACTS = {
    'Sleep': ['Sleep'],
    'Medicine': ['Morning_Meds', 'Evening_Meds', 'Take_Medicine'],
    'Eat': ['Eat', 'Eat_Breakfast', 'Eat_Lunch', 'Eat_Dinner']
}

def to_time(s):
    h = int(s)
    m = int((s - h) * 100)
    m = str(int(m * 0.6))
    h = str(h)
    s = '00'
    if len(h) < 2:
        h = '0' + h
    if len(m) < 2:
        m = '0' + m
    ns = ':'.join([h, m, s])
    return ns


def str_time_to_int(t):
    h, m, s = map(int, t.split(':'))
    tm = h + (m / 60)
    return tm


def fill_day(processed, normal, dataset):
    Addition = []
    for act in ACTS:

        act_day = processed[processed['Activity'].isin(ACTS[act])]
        act_normal = normal[normal['Activity'] == act]

        date = processed.iloc[0]['Date']


        if len(act_day) == 0:
            # print(date, act)
            for i in range(min(2, len(act_normal))):
                st = act_normal.iloc[i]['Start']
                dur = act_normal.iloc[i]['Duration']
                loc = act_normal.iloc[i]['Location'].split('-')[0]
                start = to_time(st)
                finish = to_time(st + (dur / 60))
                Addition.append([date, start, finish, loc, act])

        elif len(act_day) == 1:

            k = -1
            mx = 0
            diff = 0
            act_row = act_day.iloc[0]

            for x in range(min(2, len(act_normal))):
                diff = abs(act_normal.iloc[x]['Start'] - str_time_to_int(act_row['Start']))
                if diff > mx:
                    mx = diff
                    k = x

            st = act_normal.iloc[k]['Start']
            dur = act_normal.iloc[k]['Duration']
            loc = act_normal.iloc[k]['Location'].split('-')[0]
            start = to_time(st)
            finish = to_time(st + (dur / 60))
            Addition.append([date, start, finish, loc, act])

    return Addition


def fill_data(dataset):
    dirc = 'CASAS_DATA\\' + dataset + r'\processed_data'
    Days = len(os.listdir(dirc))
    normalpath = 'CASAS_DATA\\' + dataset + r'\Activities\Normal.csv'
    normalDf = pd.read_csv(normalpath)

    d = 1
    for day in range(1, Days + 1):

        try:
            read_path = 'CASAS_DATA\\' + dataset + r'\processed_data\Day' + str(
                day) + r'.csv'
            daydf = pd.read_csv(read_path)
            add = fill_day(daydf, normalDf, dataset)
            # print('Day:', day, add)

            for a in add:
                daydf.loc[len(daydf)] = a
            daydf.sort_values(by=['Start'], inplace=True)

            savepath = 'CASAS_DATA\\' + dataset + r'\filling\Day' + str(d) + r'.csv'
            daydf.to_csv(savepath, index=False)
            print(savepath, 'written succeesfully')
            d += 1
        except:
            print('Error in day %d in dataset %s' % (day, dataset))


Datsets = ['HH'+str(x) for x in range(101, 131)]

for dataset in ['HH129']:
    fill_data(dataset)