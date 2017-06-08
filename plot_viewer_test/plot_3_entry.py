import os
import pandas as pd
import numpy as np
from scipy import  stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima_model import ARMA
from statsmodels.graphics.api import qqplot
from statsmodels.stats.diagnostic import acorr_ljungbox
from pylab import *
import math
from datetime import datetime,timedelta

suffix = '.csv'
path_2_0 = '../version2.0/xgb_test/'
path_2_1 = '../version2.1/xgb_test/'
path_2_2 = '../version2.2/xgb_test/'
path_2_3 = '../version2.3/xgb_test/'
file_name = '3_entry_xgb_predict'

time_name = '../training_20min_avg_volume_t1_1_start_time'

#读入真实值
real_f = '../version2.0/train_feature/' + 'training_feature_3_entry' + suffix
t_index = 13
label_offset = 13
df_real = pd.read_csv(real_f, index_col=t_index, parse_dates=[t_index])
reals = df_real[df_real.index>='2016-10-11 00:00:00'].iloc[:,label_offset:].values

df_2_0 = pd.read_csv(path_2_0 + file_name + suffix)
df_2_1 = pd.read_csv(path_2_1 + file_name + suffix)
df_2_2 = pd.read_csv(path_2_2 + file_name + suffix)
df_2_3 = pd.read_csv(path_2_3 + file_name + suffix)

print path_2_0 + file_name + suffix
print path_2_1 + file_name + suffix
print path_2_2 + file_name + suffix
print path_2_3 + file_name + suffix

dta_time = pd.read_csv(time_name + suffix)



# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
figure(figsize=(8,6), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1,1,1)



##dta_label = pd.Series(dta_label)

##dta_label.index = pd.Index(Y)

plot_date(dta_time[:84], df_2_0['Entry'], color="green", linewidth=2.0, linestyle="-",label="v2.0")
plot_date(dta_time[:84], df_2_1['Entry'], color="blue", linewidth=2.0, linestyle="-",label="v2.1")
plot_date(dta_time[:84], df_2_2['Entry'], color="red", linewidth=2.0, linestyle="-",label="v2.2")
plot_date(dta_time[:84], df_2_3['Entry'], color="purple", linewidth=2.0, linestyle="-",label="v2.3")
plot_date(dta_time[:84], reals, color="black", linewidth=2.0, linestyle="-",label="reals")


##plot(X, dta, color="blue", linewidth=1.0, linestyle="-",label="t1-0")

legend(loc='best')
   
# savefig("exercice_2.png",dpi=72)

show()


