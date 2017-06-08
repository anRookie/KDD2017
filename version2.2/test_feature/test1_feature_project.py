import pandas as pd
import datetime

pre_suffix = '../test_window/'
suffix = '.csv'

feature_columns = ['delta_1_volume','delta_2_volume','delta_3_volume',
                   'delta_4_volume','delta_5_volume',
##                   'has_etc',
                   'is_next_1','is_next_2','is_next_3','is_next_4','is_next_5',
                   'is_next_6','pre_1','pre_2','pre_3','pre_4','pre_5','pre_6',
                   'pre_avg','starttime',
##                   'vehicle_model_0','vehicle_model_1','vehicle_model_2','vehicle_model_3',
##                   'vehicle_model_4','vehicle_model_5','vehicle_model_6','vehicle_model_7',
                   ]

in_file_arr = ['test1_20min_avg_volume_1_entry','test1_20min_avg_volume_1_exit',
               'test1_20min_avg_volume_2_entry',
               'test1_20min_avg_volume_3_entry','test1_20min_avg_volume_3_exit',]
out_file_arr = ['test1_feature_1_entry','test1_feature_1_exit',
               'test1_feature_2_entry',
               'test1_feature_3_entry','test1_feature_3_exit',]

t_index = 1
v_index = 3

delta_time = [[1,-40],
              [1,-20],
              [1,0],
              [2,-40],
              [2,-20],
              [2,0]]

next = [[1,0,0,0,0,0],
        [0,1,0,0,0,0],
        [0,0,1,0,0,0],
        [0,0,0,1,0,0],
        [0,0,0,0,1,0],
        [0,0,0,0,0,1]]

def pro_feature(in_file,out_file):
    df = pd.DataFrame()
     
    df.column = feature_columns
    print (pre_suffix + in_file + suffix)
    datas = pd.read_csv(pre_suffix + in_file + suffix,parse_dates=[t_index])

    hour = 0
    minute = 0
  
    for i in range(len(datas)):

        if((i+1)%6 == 0):
           
            sum = 0
            for num in range(6):
                sum = datas.iloc[i-num,v_index]+sum
            avg = sum/6
            
            for j in range(6):
                starttime = datas.iloc[i][t_index] + datetime.timedelta(hours=delta_time[j][0],minutes=delta_time[j][1])
                item = pd.DataFrame({'delta_1_volume':[datas.iloc[i-4,v_index]-datas.iloc[i-5,v_index]],
                                    'delta_2_volume':[datas.iloc[i-3,v_index]-datas.iloc[i-4,v_index]],
                                    'delta_3_volume':[datas.iloc[i-2,v_index]-datas.iloc[i-3,v_index]],
                                    'delta_4_volume':[datas.iloc[i-1,v_index]-datas.iloc[i-2,v_index]],
                                    'delta_5_volume':[datas.iloc[i-0,v_index]-datas.iloc[i-1,v_index]],
##                                    'has_etc':[datas.iloc[i,v_index+1]],
                                    'is_next_1':[next[j][0]],'is_next_2':[next[j][1]],'is_next_3':[next[j][2]],
                                    'is_next_4':[next[j][3]],'is_next_5':[next[j][4]],'is_next_6':[next[j][5]],
                                    'pre_1':[datas.iloc[i-5,v_index]],'pre_2':[datas.iloc[i-4,v_index]],
                                    'pre_3':[datas.iloc[i-3,v_index]],'pre_4':[datas.iloc[i-2,v_index]],
                                    'pre_5':[datas.iloc[i-1,v_index]],'pre_6':[datas.iloc[i-0,v_index]],
                                    'pre_avg':[avg],'starttime':[starttime],
##                                    'vehicle_model_0':[datas.iloc[i,v_index+2]],'vehicle_model_1':[datas.iloc[i,v_index+3]],
##                                    'vehicle_model_2':[datas.iloc[i,v_index+4]],'vehicle_model_3':[datas.iloc[i,v_index+5]],
##                                    'vehicle_model_4':[datas.iloc[i,v_index+6]],'vehicle_model_5':[datas.iloc[i,v_index+7]],
##                                    'vehicle_model_6':[datas.iloc[i,v_index+8]],'vehicle_model_7':[datas.iloc[i,v_index+9]],
                    
                                       })
                    
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



