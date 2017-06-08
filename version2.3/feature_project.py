import pandas as pd

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
   

if __name__ == '__main__':
    df = pd.DataFrame()

    cols_name = ['starttime','volume','pre_1','pre_2','pre_3','pre_4','pre_5','pre_6','pre_avg',
    'is_next_1','is_next_2','is_next_3','is_next_4','is_next_5','is_next_6']
    df.column = cols_name

    starttime = pd.read_csv('training_20min_starttime.csv',parse_dates=[0])

    volume = pd.read_csv('training_20min_t1_entry_volume.csv')
    
    starttime = starttime.join(volume)

    hour = 0
    minute = 0
    
    hour_list = (8,9,17,18)
    minute_list = (00,20,40)
    for i in range(len(starttime)):
        hour = starttime.iloc[i,0].hour
        minute = starttime.iloc[i,0].minute
       
        if(hour in hour_list and minute in minute_list):
            next = is_next_feature(hour,minute)
            sum = 0
            for num in range(6):
                sum = starttime.iloc[i-num,1]+sum
            avg = sum/6

            a2 = pd.DataFrame({'starttime':[starttime.iloc[i,0]],'volume':[starttime.iloc[i,1]],
                               'pre_1':[starttime.iloc[i-1,1]],'pre_2':[starttime.iloc[i-2,1]],
                               'pre_3':[starttime.iloc[i-3,1]],'pre_4':[starttime.iloc[i-4,1]],
                               'pre_5':[starttime.iloc[i-5,1]],'pre_6':[starttime.iloc[i-6,1]],
                               'pre_avg':[avg],
                               'is_next_1':[next[0]],'is_next_2':[next[1]],'is_next_3':[next[2]],
                               'is_next_4':[next[3]],'is_next_5':[next[4]],'is_next_6':[next[5]]})
            
            df = df.append(a2,ignore_index=True)
    df.index = df['starttime']
##    df = df.drop(['starttime'],axis=1)
##    print df
    
    fw = open("feature.csv", 'w')
    fw.writelines(','.join(['is_next_1','is_next_2','is_next_3','is_next_4','is_next_5',
                            'is_next_6','pre_1','pre_2','pre_3','pre_4','pre_5','pre_6',
                            'pre_avg','starttime','volume']) + '\n')
    for i in range(len(df)):
        str_line = []
        for j in range(len(feature_columns)):
            str_line.append('"' + str(df.iloc[i,j]) + '"')
        out_line = ",".join(str_line) + '\n'
        fw.writelines(out_line)
    fw.close()

