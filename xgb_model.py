import pandas as pd
import numpy as np
from pandas import DataFrame
import csv
import xgboost as xgb
import time
import matplotlib.pyplot as plt

now = time.time()

total_datas = 'feature2.csv'

total_datas_df = pd.read_csv(total_datas, index_col=0, parse_dates=[0])


trains = total_datas_df[total_datas_df.index<'2016-10-11 00:00:00']
tests  = total_datas_df[total_datas_df.index>='2016-10-11 00:00:00']

train = trains.drop(['no_etc','use_etc'],axis=1).iloc[:,1:].values
labels = trains.drop(['no_etc','use_etc'],axis=1).iloc[:,:1].values

test = tests.drop(['no_etc','use_etc'],axis=1).iloc[:,1:].values

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

offset = 1152   # 划分验证集从2016-10-05 00:00:00
num_rounds = 10000
xgtest = xgb.DMatrix(test)

xgtrain = xgb.DMatrix(train[:offset,:], label=labels[:offset])
xgval = xgb.DMatrix(train[offset:,:], label=labels[offset:])

watchlist = [(xgtrain, 'train'),(xgval, 'val')]

model = xgb.train(plst, xgtrain, num_rounds, watchlist,early_stopping_rounds=100)

preds = model.predict(xgtest,ntree_limit=model.best_iteration)

np.savetxt('submission_xgb_predicttest.csv',np.c_[range(1,len(test)+1),preds],
                delimiter=',',header='time,Entry',comments='',fmt='%d')

cost_time = time.time()-now
print "end ......",'\n',"cost time:",cost_time,"(s)......"
