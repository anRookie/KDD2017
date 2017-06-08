import pandas as pd
import numpy as np
from pandas import DataFrame
import csv
import matplotlib.pyplot as plt
from pylab import *

total_datas = 'feature.csv'

total_datas_df = pd.read_csv(total_datas, index_col=13, parse_dates=[13])

tests  = total_datas_df[total_datas_df.index>='2016-10-11 00:00:00']['volume']

pred_datas = 'xgb_predict.csv'

preds = pd.read_csv(pred_datas, index_col=0)

plot_date(tests.index, preds, color="green", linewidth=1.0, linestyle="-",label="preds")
plot_date(tests.index, tests, color="blue", linewidth=1.0, linestyle="-",label="reals")

legend(loc='best')

show()
