#HDBSCAN Clustering for each activity

import hdbscan
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from txt_to_csv import DATASETS

#Processing data suitable for clustering
def processData(df):
    data = df[['Start_Time', 'Duration']]
    data = data.values.astype('float32', copy=False)
    return data

#Scaling data using Standard Scaler for clsutering
def scaleData(data):
    scaler = StandardScaler().fit(data)
    scaled_data = scaler.transform(data)
    return scaled_data

# A is a list of tuples (Start, Duration). Returns List of Start time and Duration separatly
def toStartDuration(A):
    Start = []
    Duration = []
    for i in range(len(A)):
        Start.append(A[i][0])
        Duration.append(A[i][1])
    return Start, Duration

def clustering(df, r, mp):
    data = processData(df)
    X = scaleData(data)

    model = hdbscan.HDBSCAN(min_cluster_size=r, min_samples=mp, metric='euclidean').fit(X)
    #model = DBSCAN(eps=r, min_samples=mp, metric='euclidean').fit(X)
    #model = OPTICS(min_cluster_size=r, min_samples=mp, metric='euclidean', cluster_method='xi').fit(X)

    if -1 in set(model.labels_): #-1 points are outliers in clusters which are not needed
        clusters = len(set(model.labels_)) -1
    else:
        clusters = len(set(model.labels_))

    Cluster_set = []
    for i in range(clusters):
        a = data[model.labels_ == i]
        Cluster_set.append(a)
    return Cluster_set

#Find average of a List
def avg(A):
    a = sum(A)/len(A)
    a = float('%.2f'%a)
    return a

#Find minimum of a List
def Min(A):
    a = min(A)
    a = float('%.2f'%a)
    return a

#Find Maximum of a List
def Max(A):
    a = max(A)
    a = float('%.2f'%a)
    return a

#Takes a list of list of locations. Return string of locations with thier percentage
def locate(Locations):
    s = set(Locations)
    if 'Ignore' in s: #Removing this Location
        s.remove('Ignore')

    L = []
    total = 0
    for i in s:
        if Locations.count(i) >= 8:
            total += Locations.count(i)

    for i in s:
        lc = Locations.count(i)
        if lc >= 8:
            v = str(int((100*lc)/total))
            L.append(i+'#'+v)
    locstr = '-'.join(L)
    return locstr

def main():
    Normal = []

    Activity = {
        'Eat': {
            'read_path': r'CASAS_DATA\HH' + DATASET + r'\Activities\Eat.csv',
            'Clusters': [],
            'min_samples': 3, #Change accrding to clustering method
            'min_pts': 10,  #Change accrding to clustering method
            'save_path': r'CASAS_DATA\HH' + DATASET + r'\Activities\Clusters\Eat'

        },

        'Sleep': {
            'read_path': r'CASAS_DATA\HH' + DATASET + r'\Activities\Sleep.csv',
            'Clusters': [],
            'min_samples': 4, #Change accrding to clustering method
            'min_pts': 15,
            'save_path': r'CASAS_DATA\HH' + DATASET + r'\Activities\Clusters\Sleep'
        },

        'Medicine': {
            'read_path': r'CASAS_DATA\HH' + DATASET + r'\Activities\Medicine.csv',
            'save_path': r'CASAS_DATA\HH' + DATASET + r'\Activities\Clusters\Medicine',
            'Clusters': [],
            'min_samples': 5, #Change accrding to clustering method
            'min_pts': 25 #Change accrding to clustering method
        },
    }

    for activity in Activity:
        path = Activity[activity]['read_path']
        data = pd.read_csv(path)
        locations = list(data['Location'])
        Activity[activity]['Clusters'] = clustering(
            data,
            Activity[activity]['min_samples'],
            Activity[activity]['min_pts']
        )

        clus = 1
        locstr = locate(locations)

        for cluster in Activity[activity]['Clusters']:
            Start, Duration = toStartDuration(cluster)
            avgStart = avg(Start)
            minStart = Min(Start)
            maxStart = Max(Start)
            avgDur = avg(Duration)
            minDur = Min(Duration)
            maxDur = Max(Duration)
            label = activity + str(clus)

            Normal.append([activity, label, locstr, avgStart, avgDur, minStart, maxStart, minDur, maxDur])

            new_df = pd.DataFrame({
                'Start': Start,
                'Duration': Duration
            })
            savepath = Activity[activity]['save_path'] + str(clus) + '.csv'
            new_df.to_csv(savepath, index=False)
            print(savepath)
            clus += 1

    normal_df = pd.DataFrame(Normal,
                             columns=['Activity', 'Label', 'Location', 'Start', 'Duration', 'min_start', 'max_start',
                                      'min_dur', 'max_dur'])
    normal_path = r'CASAS_DATA\HH' + DATASET + r'\Activities\Normal.csv'
    #adaptive_normal_path = r'D:\Daily Life Anomaly Detection\CASAS_DATA\HH' + DATASET + r'\ActivitIes\Adaptive_Normal.csv'
    normal_df.to_csv(normal_path, index=False)
    print(normal_path)
    #normal_df.to_csv(adaptive_normal_path, index=False)
    #print(adaptive_normal_path)


if __name__ == '__main__':
    DATASET = ''
    # This will Run script for all Datasets HH101-HH130
    for dataset in DATASETS:
        DATASET = d
        main()


    # If you want to run script for few chosen datasets only. Use this code.
    # for d in ['101', '104','121']: #Add datasets in this list
    #     DATASET = d
    #     main()