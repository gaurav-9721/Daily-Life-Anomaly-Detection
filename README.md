## Daily Life Anomaly Detection

### Requirements

```
Python 3.7+
Jupyter Notebook (included in requirements.txt)
```

Download & Install python libraries 


```
pip install -r requirements.txt
```
or 
```
conda install -r requirements.txt
```

### Datasets
Download original datasets [here](http://casas.wsu.edu/datasets/).

Download processed data [here](https://drive.google.com/drive/folders/1gDY_Z3yUJGe7hXTN0m9vy7ZTWafw0i7n?usp=sharing). 
Save this data to your cloned repository and replace with the folders *CASAS_DATA*, *CSV_Datasets* and *DataSets*.

### How to use?

#### Process data into different formats (.py) -

* **txt_to_csv.py :** Converts txt file into csv format
* **Split_daywise.py :** Split days of data from single file to different csv files.
* **process_daily_data.py :** Process each day of data and convert it into (Start time, Finish Time, Activity, Location) format.
* **Data Filling.py :** Fills missing activities with their average values.
* **data_cleaning.py :** Remove days which have missing activities.
* **train_test_split.py :** Splits data into training and testing data.
* **Activities.py :** Extracts Start time, Duration and Location values from each day and create separate files for each activity.
* **Clustering.py :** Creates clusters of each activity and save each cluster in a csv file.

#### Jupyter Notebook Files (.ipynb) -

* **Dataset Details :** Details of all HHxxx type dataset (Frequency and Clustering details)
* **Gantt_Chart :** Gantt chart / Timeline chart of daily data.
* **Fitness Plot :** Graph plot of Fitness score of each day of various datasets.
* **OPTICS VS HDBSCAN :** Clustering algorithm optics and hdbscan comparison. (HDBSCAN better)
* **Fitness Score + Sequence :** Graph plot of (fitness score +sequence score together) and location independently. 
* **Fitness Function Adaptive :** Adaptive Learning.
* **Create New Dataset :** Create new HHxxx type data.
* **Activity-wise Anomaly Detection (Stage 2) :** Stage two of this Framework. Analyze deep details of Start Time anomaly, Duration anomaly, Location Anomaly and Sequqential Anomaly.
* **Fuzzy Cluster :** Fuzzy Modelling Demo.

<br><br>
>> Happy Coding : )

____________________
