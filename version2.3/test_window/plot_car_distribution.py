import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

suffix = '.csv'
path = ''
file_name = 'test1_20min_avg_volume_1_entry'

colors = ['green','blue','red','black','grey','yellow','purple','pink','brown','maroon','chocolate','peru']

df = pd.read_csv(path + file_name + suffix)
print(path + file_name + suffix)

figure(figsize=(8,6), dpi=80)
subplot(1,1,1)
plot_date(df['time_window'], df['volume'], color=colors[0], linewidth=1.0, linestyle="-",label="volume")
plot_date(df['time_window'], df['has_etc'], color=colors[1], linewidth=1.0, linestyle="-",label="has_etc")
plot_date(df['time_window'], df['vehicle_model_0'], color=colors[2], linewidth=1.0, linestyle="-",label="vehicle_model_0")
plot_date(df['time_window'], df['vehicle_model_1'], color=colors[3], linewidth=1.0, linestyle="-",label="vehicle_model_1")
plot_date(df['time_window'], df['vehicle_model_2'], color=colors[4], linewidth=1.0, linestyle="-",label="vehicle_model_2")
plot_date(df['time_window'], df['vehicle_model_3'], color=colors[5], linewidth=1.0, linestyle="-",label="vehicle_model_3")
plot_date(df['time_window'], df['vehicle_model_4'], color=colors[6], linewidth=1.0, linestyle="-",label="vehicle_model_4")
plot_date(df['time_window'], df['vehicle_model_5'], color=colors[7], linewidth=1.0, linestyle="-",label="vehicle_model_5")
plot_date(df['time_window'], df['vehicle_model_6'], color=colors[8], linewidth=1.0, linestyle="-",label="vehicle_model_6")
plot_date(df['time_window'], df['vehicle_model_7'], color=colors[9], linewidth=1.0, linestyle="-",label="vehicle_model_7")
plot_date(df['time_window'], df['vehicle_type_0'], color=colors[10], linewidth=1.0, linestyle="-",label="vehicle_type_0")
plot_date(df['time_window'], df['vehicle_type_1'], color=colors[11], linewidth=1.0, linestyle="-",label="vehicle_type_1")


legend(loc='best')
show()
