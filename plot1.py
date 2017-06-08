import MySQLdb as mdb
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

file_suffix = '.csv'
path = ''
in_file = 'training_20min_avg_volume_t1_0_volume'
in_file_name = in_file + file_suffix
fr = open(path + in_file_name, 'r')
fr.readline()
vol_data = fr.readlines()

in_file = 'training_20min_avg_volume_t1_1_start_time'
in_file_name = in_file + file_suffix
fr = open(path + in_file_name, 'r')
fr.readline()
time_data = fr.readlines()

num_volome = []
for j in vol_data:
    num_volome.append(float(j))

time_new = []
for j in range(len(time_data)):
    time_new.append((time_data[j]))

X = []
Y = []
num_volome_label = []
time_new_label = []
for j in range(len(time_data)):
    X.append(j+1)
    remainder = j%72
    if((remainder>23 and remainder<30) or (remainder>50 and remainder<57)):
        num_volome_label.append(num_volome[j])
        time_new_label.append((time_data[j]))
        Y.append(j+1)

# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
figure(figsize=(8,6), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1,1,1)

dta = np.array(num_volome,dtype=np.float)

dta = pd.Series(dta)

##dta.index = pd.Index(X)

dta_label = np.array(num_volome_label,dtype=np.float)

##dta_label = pd.Series(dta_label)

##dta_label.index = pd.Index(Y)

plot_date(time_new_label, dta_label, color="green", linewidth=4.0, linestyle="-",label="t1-0_label")

plot_date(time_new, dta, color="blue", linewidth=1.0, linestyle="-",label="t1-0")

##plot(X, dta, color="blue", linewidth=1.0, linestyle="-",label="t1-0")

legend(loc='best')
   
# savefig("exercice_2.png",dpi=72)

show()


