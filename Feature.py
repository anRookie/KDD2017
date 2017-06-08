import pandas as pd
import numpy as np
from pandas import DataFrame
import csv
import math
from datetime import datetime,timedelta


volume_train = 'volume(table 6)_training.csv'
volume_train_df = pd.read_csv(volume_train, index_col=0, parse_dates=[0])
tollgate_1 = volume_train_df[volume_train_df['tollgate_id'] ==1]
tollgate_2 = volume_train_df[volume_train_df['tollgate_id'] ==2]
tollgate_3 = volume_train_df[volume_train_df['tollgate_id'] ==3]

"""
tollgate_1.to_csv('tollgate_1.csv')
tollgate_2.to_csv('tollgate_2.csv')
tollgate_3.to_csv('tollgate_3.csv')
"""

tollgate_1_entry = tollgate_1[tollgate_1['direction']==0]
tollgate_1_exit = tollgate_1[tollgate_1['direction']==1]

tollgate_2_entry = tollgate_2[tollgate_2['direction']==0]
tollgate_2_exit = tollgate_2[tollgate_2['direction']==1]

tollgate_3_entry = tollgate_3[tollgate_3['direction']==0]
tollgate_3_exit = tollgate_3[tollgate_3['direction']==1]

"""
tollgate_1_entry.to_csv('tollgate_1_entry.csv')
tollgate_1_exit.to_csv('tollgate_1_exit.csv')
tollgate_2_entry.to_csv('tollgate_2_entry.csv')
tollgate_2_exit.to_csv('tollgate_2_exit.csv')
tollgate_3_entry.to_csv('tollgate_3_entry.csv')
tollgate_3_exit.to_csv('tollgate_3_exit.csv')
"""

def FirstFeature(tollgate):
    tollgate = tollgate.drop(['tollgate_id','vehicle_type', 'vehicle_model'],axis=1)
    no_etc = tollgate[tollgate['has_etc']==0].drop(['direction'],axis=1).resample('20min', how='count', label='left')
    no_etc.columns = ['no_etc']
    use_etc = tollgate[tollgate['has_etc']==1].drop(['direction'],axis=1).resample('20min', how='count', label='left')
    use_etc.columns = ['use_etc']
    feature = tollgate.resample('20min', how='count', label='left').drop(['has_etc'], axis=1)
    feature.columns = ['entry_dir']
    feature = pd.concat([feature,no_etc,use_etc], axis=1)
    return feature

def JudgInterval(pass_time, pre_time_window, lat_time_window):
    if pass_time >= pre_time_window:
        if pass_time < lat_time_window:
            return True
    else:
        return False

def Pre_3min_Feature(tollgate):
    feature = FirstFeature(tollgate)
    feature["pre_3min_dir"] = 0
    feature["pre_3min_etc"] =0
    feature["pre_3min_no_etc"] =0
    tim1 = timedelta(minutes=17)
    tim2 = timedelta(minutes=20)
    for index, row in tollgate.iterrows():
        time_window_minute = int(math.floor((index.minute) / 20) * 20)
        start_time_window = datetime(index.year, index.month, index.day,
                                         index.hour, time_window_minute, 0)
        pre_time_window = start_time_window + tim1
        lat_time_window = start_time_window + tim2
        if JudgInterval(index, pre_time_window, lat_time_window):
            feature["pre_3min_dir"][lat_time_window] += 1 
            if row["has_etc"]:
                feature["pre_3min_etc"][lat_time_window] += 1
            else:
                feature["pre_3min_no_etc"][lat_time_window] += 1
    return  feature

def Pre_5min_Feature(tollgate):
    feature = Pre_3min_Feature(tollgate)
    feature["pre_5min_dir"] = 0
    feature["pre_5min_etc"] =0
    feature["pre_5min_no_etc"] =0
    tim1 = timedelta(minutes=15)
    tim2 = timedelta(minutes=20)
    for index, row in tollgate.iterrows():
        time_window_minute = int(math.floor((index.minute) / 20) * 20)
        start_time_window = datetime(index.year, index.month, index.day,
                                         index.hour, time_window_minute, 0)
        pre_time_window = start_time_window + tim1
        lat_time_window = start_time_window + tim2
        if JudgInterval(index, pre_time_window, lat_time_window):
            feature["pre_5min_dir"][lat_time_window] += 1 
            if row["has_etc"]:
                feature["pre_5min_etc"][lat_time_window] += 1
            else:
                feature["pre_5min_no_etc"][lat_time_window] += 1
    return  feature

def Pre_7min_Feature(tollgate):
    feature = Pre_5min_Feature(tollgate)
    feature["pre_7min_dir"] = 0
    feature["pre_7min_etc"] =0
    feature["pre_7min_no_etc"] =0
    tim1 = timedelta(minutes=13)
    tim2 = timedelta(minutes=20)
    for index, row in tollgate.iterrows():
        time_window_minute = int(math.floor((index.minute) / 20) * 20)
        start_time_window = datetime(index.year, index.month, index.day,
                                         index.hour, time_window_minute, 0)
        pre_time_window = start_time_window + tim1
        lat_time_window = start_time_window + tim2
        if JudgInterval(index, pre_time_window, lat_time_window):
            feature["pre_7min_dir"][lat_time_window] += 1 
            if row["has_etc"]:
                feature["pre_7min_etc"][lat_time_window] += 1
            else:
                feature["pre_7min_no_etc"][lat_time_window] += 1
    return  feature

def Pre_10min_Feature(tollgate):
    feature = Pre_7min_Feature(tollgate)
    feature["pre_10min_dir"] = 0
    feature["pre_10min_etc"] =0
    feature["pre_10min_no_etc"] =0
    tim1 = timedelta(minutes=10)
    tim2 = timedelta(minutes=20)
    for index, row in tollgate.iterrows():
        time_window_minute = int(math.floor((index.minute) / 20) * 20)
        start_time_window = datetime(index.year, index.month, index.day,
                                         index.hour, time_window_minute, 0)
        pre_time_window = start_time_window + tim1
        lat_time_window = start_time_window + tim2
        if JudgInterval(index, pre_time_window, lat_time_window):
            feature["pre_10min_dir"][lat_time_window] += 1 
            if row["has_etc"]:
                feature["pre_10min_etc"][lat_time_window] += 1
            else:
                feature["pre_10min_no_etc"][lat_time_window] += 1
    return  feature


feature = Pre_10min_Feature(tollgate_1_entry)





