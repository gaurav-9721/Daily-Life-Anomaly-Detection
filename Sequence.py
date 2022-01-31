import pandas as pd
import numpy as np
import os

from Bio import pairwise2
from Bio.pairwise2 import format_alignment

#Remove or Add activity here to add in sequence
short = {
    'Sleep': 'S',
    #'Personal_Hygiene': 'P',
    'Morning_Meds': 'M',
    'Evening_Meds':'M',
    'Bathe': 'B',
    'Cook': 'C',
    'Cook_Breakfast': 'C',
    'Cook_Dinner': 'C',
    'Cook_Lunch': 'C',
    'Eat': 'E',
    'Eat_Breakfast':'E',
    'Eat_Dinner':'E',
    'Eat_Lunch':'E',
    'Wash_Breakfast_Dishes': 'W',
    'Wash_Dinner_Dishes': 'W',
    'Wash_Dishes': 'W',
    'Wash_Lunch_Dishes':'W'
}

def get_day_sequence(dataset, day):
    readpath = 'CASAS_DATA\\' +dataset+ r'\processed_data\Day' + str(day) + '.csv'
    df = pd.read_csv(readpath)
    Act = list(df['Activity'])

    sequence = ['@']
    for act in Act:
        if act in short:
            if sequence[-1] != short[act]:
                sequence.append(short[act])
    seq = ''.join(sequence)
    return seq

def get_sequences(dataset):
    dirc = 'CASAS_DATA\\' +dataset+ r'\processed_data'
    Days = len(os.listdir(dirc))
    SEQ = []
    for day in range(1, Days+1):
        seq = get_day_sequence(dataset, day)
        SEQ.append(seq[1:])
    return SEQ

def save_sequences(dataset):
    # Sequence Save
    normal_seqs= get_sequences(dataset)
    days = [x+1 for x in range(len(normal_seqs))]

    seq_df = pd.DataFrame({
        'Day': days,
        'Sequence': normal_seqs
    })
    savepath = r'D:\Daily Life Anomaly Detection\CASAS_DATA\\' + dataset + r'\Activities\Sequence.csv'
    seq_df.to_csv(savepath, index=False)
    print(savepath, 'written successfully')

Datsets = ['HH'+str(x) for x in range(101, 131)]

for data in Datsets:
    save_sequences(data)

