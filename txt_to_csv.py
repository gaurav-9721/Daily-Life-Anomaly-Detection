#This script will convert txt file into csv file. Also removes unwanted data like sensor details.

import pandas as pd

DATASETS = [str(x) for x in range(101, 131)]

def main():
    path = r'DataSets/hh' + DATASET + '.txt'
    file = open(path)
    Lines = sum(1 for line in file)  #Calculating total lines in txt file
    file.close()

    file = open(path)
    FilterData = []
    for i in range(Lines):
        s = str(file.readline())
        s = s.split()

        FilterData.append([s[0], s[1], s[3], s[-1]]) #Chooseing Required Columns from each line
        #S[0] Date, S[1] Time, S[2] Sensor, S[3] Location, S[4] Sensor Status, S[5] Sensor Type, S[6] Activity

    data = pd.DataFrame(FilterData, columns=['Date', 'Time', 'Location', 'Activity'])
    file.close()

    save_path = r'CSV_Datasets/hh' + DATASET + '.csv'
    print(save_path, 'written successfully')
    data.to_csv(save_path, index=False)

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




