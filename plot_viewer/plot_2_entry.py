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
path_2_0 = '../version2.0/xgb_predict/'
path_2_1 = '../version2.1/xgb_predict/'
path_2_2 = '../version2.2/xgb_predict/'
file_name = '2_entry_xgb_predict'

time_name = '../training_20min_avg_volume_t1_1_start_time'

df_2_0 = pd.read_csv(path_2_0 + file_name + suffix)
df_2_1 = pd.read_csv(path_2_1 + file_name + suffix)
df_2_2 = pd.read_csv(path_2_2 + file_name + suffix)
print path_2_0 + file_name + suffix
print path_2_1 + file_name + suffix
print path_2_2 + file_name + suffix

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


##plot(X, dta, color="blue", linewidth=1.0, linestyle="-",label="t1-0")

legend(loc='best')
   
# savefig("exercice_2.png",dpi=72)

show()


