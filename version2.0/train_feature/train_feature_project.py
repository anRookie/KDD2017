import pandas as pd
import datetime

path = '../train_window/'
suffix = '.csv'

feature_columns = ['is_next_1','is_next_2','is_next_3','is_next_4','is_next_5',
                            'is_next_6','pre_1','pre_2','pre_3','pre_4','pre_5','pre_6',
                            'pre_avg','starttime','volume']

in_file_arr = ['training_20min_avg_volume_1_entry','training_20min_avg_volume_1_exit',
               'training_20min_avg_volume_2_entry',
               'training_20min_avg_volume_3_entry','training_20min_avg_volume_3_exit',]
out_file_arr = ['training_feature_1_entry','training_feature_1_exit',
               'training_feature_2_entry',
               'training_feature_3_entry','training_feature_3_exit',]

t_index = 1
v_index = 3

def is_next_feature(hour,minute):
    if((hour==8 or hour==17) and minute==00):
        return [1,0,0,0,0,0]
    if((hour==8 or hour==17) and minute==20):
        return [0,1,0,0,0,0]
    if((hour==8 or hour==17) and minute==40):
        return [0,0,1,0,0,0]
    if((hour==9 or hour==18) and minute==00):
        return [0,0,0,1,0,0]
    if((hour==9 or hour==18) and minute==20):
        return [0,0,0,0,1,0]
    if((hour==9 or hour==18) and minute==40):
        return [0,0,0,0,0,1]

def pro_feature(in_file,out_file):
    df = pd.DataFrame()
     
    df.column = feature_columns

    datas = pd.read_csv(path + in_file + suffix,parse_dates=[t_index])
    print path + in_file + suffix

    hour = 0
    minute = 0
  
    hour_list = (8,9,17,18)
    minute_list = (00,20,40)
    
    delta = 0
    for i in range(len(datas)):
        hour = datas.iloc[i,t_index].hour
        minute = datas.iloc[i,t_index].minute
        
        if(hour in hour_list and minute in minute_list):
            
            next = is_next_feature(hour,minute)
            sum = 0
            for num in range(6):
                sum = datas.iloc[i-1-delta-num,v_index]+sum
            avg = sum/6
          
            item = pd.DataFrame({'is_next_1':[next[0]],'is_next_2':[next[1]],'is_next_3':[next[2]],
                    'is_next_4':[next[3]],'is_next_5':[next[4]],'is_next_6':[next[5]],
                    'pre_1':[datas.iloc[i-delta-1,v_index]],'pre_2':[datas.iloc[i-delta-2,v_index]],
                    'pre_3':[datas.iloc[i-delta-3,v_index]],'pre_4':[datas.iloc[i-delta-4,v_index]],
                    'pre_5':[datas.iloc[i-delta-5,v_index]],'pre_6':[datas.iloc[i-delta-6,v_index]],
                    'pre_avg':[avg],'starttime':[datas.iloc[i,t_index]],'volume':[datas.iloc[i,v_index]]
                        })
            delta = delta + 1
            if (delta%6 == 0):
                delta = 0
            df = df.append(item,ignore_index=True)
                
    df.index = df['starttime']
    
    fw = open(out_file+suffix, 'w')
    fw.writelines(','.join(feature_columns) + '\n')
    for i in range(len(df)):
        str_line = []
        for j in range(len(feature_columns)):
            str_line.append('"' + str(df.iloc[i,j]) + '"')
        out_line = ",".join(str_line) + '\n'
        fw.writelines(out_line)
    fw.close()

if __name__ == '__main__':
    for i in range(len(in_file_arr)):
        pro_feature(in_file_arr[i],out_file_arr[i])



