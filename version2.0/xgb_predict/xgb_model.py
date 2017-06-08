import pandas as pd
import numpy as np
from pandas import DataFrame
import csv
import xgboost as xgb
import time
import matplotlib.pyplot as plt


path_train = '../train_feature/'
path_test = '../test_feature/'
suffix = '.csv'

train_file_arr = ['training_feature_1_entry','training_feature_1_exit',
               'training_feature_2_entry',
               'training_feature_3_entry','training_feature_3_exit',]

test_file_arr = ['test1_feature_1_entry','test1_feature_1_exit',
               'test1_feature_2_entry',
               'test1_feature_3_entry','test1_feature_3_exit',]

t_index = 13

def xgbmodel(train_file,test_file):
    now = time.time()

    training_f = path_train + train_file + suffix
    test_f = path_test + test_file + suffix

    print test_f

    training_df = pd.read_csv(training_f, index_col=t_index, parse_dates=[t_index])
    test_df =pd.read_csv(test_f, index_col=t_index, parse_dates=[t_index])

    train = training_df.iloc[:,:13].values
    labels = training_df.iloc[:,13:].values

    test = test_df.iloc[:,:13].values
   
    params={
    'booster':'gbtree',
    'gamma':0.05,  # 在树的叶子节点下一个分区的最小损失，越大算法模型越保守 。[0:]
    'max_depth':12, # 构建树的深度 [1:]
    #'lambda':450,  # L2 正则项权重
    'subsample':0.4, # 采样训练数据，设置为0.5，随机选择一般的数据实例 (0:1]
    'colsample_bytree':0.7, # 构建树树时的采样比率 (0:1]
    #'min_child_weight':12, # 节点的最少特征数
    'silent':1 ,
    'eta': 0.005, # 如同学习率
    'seed':710,
    'nthread':4,
    }

    plst = list(params.items())

    offset = len(training_df[training_df.index<'2016-10-11 00:00:00'])   # 划分验证集从2016-10-XX 00:00:00
    num_rounds = 10000

    xgtest = xgb.DMatrix(test)
    xgtrain = xgb.DMatrix(train[:offset,:], label=labels[:offset])
    xgval = xgb.DMatrix(train[offset:,:], label=labels[offset:])

    watchlist = [(xgtrain, 'train'),(xgval, 'val')]

    model = xgb.train(plst, xgtrain, num_rounds, watchlist,early_stopping_rounds=100)

    preds = model.predict(xgtest,ntree_limit=model.best_iteration)

    s_txt = test_file.split('_')
    np.savetxt(s_txt[2] + '_' + s_txt[3] + '_xgb_predict.csv',np.c_[range(1,len(test)+1),preds],
                    delimiter=',',header='time,Entry',comments='',fmt='%d')

    cost_time = time.time()-now
    print "end ......",'\n',"cost time:",cost_time,"(s)......"

if __name__ == '__main__':
    for i in range(len(train_file_arr)):
        xgbmodel(train_file_arr[i],test_file_arr[i])
