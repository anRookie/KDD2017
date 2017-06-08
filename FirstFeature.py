import pandas as pd
import numpy as np
from pandas import DataFrame
import csv


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


feature_1 = FirstFeature(tollgate_1_entry)
