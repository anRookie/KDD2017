# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Calculate volume for each 20-minute time window.
"""
import math
from datetime import datetime,timedelta

file_suffix = '.csv'
path = '../datasets/'  # set the data directory

def avgVolume(in_file):

    out_suffix_arr = ['_20min_avg_volume_1_entry','_20min_avg_volume_1_exit',
                      '_20min_avg_volume_2_entry',
                      '_20min_avg_volume_3_entry','_20min_avg_volume_3_exit']
    in_file_name = in_file + file_suffix
    out_file_name_arr = []
    for i in range(len(out_suffix_arr)):
        out_file_name_arr.append(in_file.split('_')[1] + out_suffix_arr[i] + file_suffix)
       


    # Step 1: Load volume data
    fr = open(path + in_file_name, 'r')
    fr.readline()  # skip the header
    vol_data = fr.readlines()
    fr.close()

    # Step 2: Create a dictionary to caculate and store volume per time window
    volumes = {}  # key: time window value: dictionary
    for i in range(len(vol_data)):
        each_pass = vol_data[i].replace('"', '').split(',')
        tollgate_id = each_pass[1]
        direction = each_pass[2]
        
        vehicle_model = each_pass[3]
        has_etc = each_pass[4]
        vehicle_type = each_pass[5].strip('\n')

        pass_time = each_pass[0]
        pass_time = datetime.strptime(pass_time, "%Y-%m-%d %H:%M:%S")
        time_window_minute = int(math.floor(pass_time.minute / 20) * 20)
        #print pass_time
        start_time_window = datetime(pass_time.year, pass_time.month, pass_time.day,
                                     pass_time.hour, time_window_minute, 0)

        if start_time_window not in volumes:
            volumes[start_time_window] = {}
        if tollgate_id not in volumes[start_time_window]:
            volumes[start_time_window][tollgate_id] = {}
        if direction not in volumes[start_time_window][tollgate_id]:
            volumes[start_time_window][tollgate_id][direction] = {}
            volumes[start_time_window][tollgate_id][direction]["volume"] = 1
            volumes[start_time_window][tollgate_id][direction]["has_etc"] = float(has_etc)
           
            volumes[start_time_window][tollgate_id][direction]["vehicle_model_0"] = 0.00
            volumes[start_time_window][tollgate_id][direction]["vehicle_model_1"] = 0.00
            volumes[start_time_window][tollgate_id][direction]["vehicle_model_2"] = 0.00
            volumes[start_time_window][tollgate_id][direction]["vehicle_model_3"] = 0.00
            volumes[start_time_window][tollgate_id][direction]["vehicle_model_4"] = 0.00
            volumes[start_time_window][tollgate_id][direction]["vehicle_model_5"] = 0.00
            volumes[start_time_window][tollgate_id][direction]["vehicle_model_6"] = 0.00
            volumes[start_time_window][tollgate_id][direction]["vehicle_model_7"] = 0.00
            volumes[start_time_window][tollgate_id][direction]["vehicle_model" + "_" + str(vehicle_model)] += 1

            volumes[start_time_window][tollgate_id][direction]["vehicle_type_0"] = 0.00
            volumes[start_time_window][tollgate_id][direction]["vehicle_type_1"] = 0.00
           
            
            if (str(vehicle_type) in ('1','0')):
                volumes[start_time_window][tollgate_id][direction]["vehicle_type" + "_" + str(vehicle_type)] += 1
            
        else:
            volumes[start_time_window][tollgate_id][direction]["volume"] += 1
            volumes[start_time_window][tollgate_id][direction]["has_etc"] += int(has_etc)
            volumes[start_time_window][tollgate_id][direction]["vehicle_model" + "_" + str(vehicle_model)] += 1
            if (vehicle_type in ("0","1")):
               
                volumes[start_time_window][tollgate_id][direction]["vehicle_type" + "_" + str(vehicle_type)] += 1

    # Step 3: format output for tollgate and direction per time window
    fw_arr = []
    for i in range(len(out_suffix_arr)):
        fw_arr.append(open(out_file_name_arr[i], 'w'))
        fw_arr[i].writelines(','.join(['"tollgate_id"', '"time_window"', '"direction"', '"volume"', '"has_etc"',
                                       "vehicle_model_0", "vehicle_model_1", "vehicle_model_2", "vehicle_model_3",
                                       "vehicle_model_4", "vehicle_model_5", "vehicle_model_6", "vehicle_model_7",
                                       "vehicle_type_0", "vehicle_type_1"]) + '\n')
   
    time_windows = list(volumes.keys())
    time_windows.sort()
    item_volume = 0
    
    for time_window_start in time_windows:
        time_window_end = time_window_start + timedelta(minutes=20)
        for tollgate_id in volumes[time_window_start]:
            for direction in volumes[time_window_start][tollgate_id]:
               item_volume = volumes[time_window_start][tollgate_id][direction]["volume"]
               
               out_line = ','.join([ str(tollgate_id), 
			           str(time_window_start),
                                 str(direction) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["volume"]) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["has_etc"]) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_0"]) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_1"]) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_2"]) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_3"]) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_4"]) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_5"]) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_6"]) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_7"]) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_type_0"]) ,
                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_type_1"]) ,
                                 
##                                 str(volumes[time_window_start][tollgate_id][direction]["has_etc"]/item_volume) ,
##                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_0"]/item_volume) ,
##                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_1"]/item_volume) ,
##                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_2"]/item_volume) ,
##                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_3"]/item_volume) ,
##                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_4"]/item_volume) ,
##                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_5"]/item_volume) ,
##                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_6"]/item_volume) ,
##                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_model_7"]/item_volume) ,
##                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_type_0"]/item_volume) ,
##                                 str(volumes[time_window_start][tollgate_id][direction]["vehicle_type_1"]/item_volume) ,
                                 
                               ]) + '\n'
               
               if(tollgate_id=='1' and direction=='0'):
                   fw_arr[0].writelines(out_line)
               if(tollgate_id=='1' and direction=='1'):
                   fw_arr[1].writelines(out_line)
               if(tollgate_id=='2' and direction=='0'):
                   fw_arr[2].writelines(out_line)
               if(tollgate_id=='3' and direction=='0'):
                   fw_arr[3].writelines(out_line)
               if(tollgate_id=='3' and direction=='1'):
                   fw_arr[4].writelines(out_line)
                   
    for i in range(len(out_suffix_arr)):
        fw_arr[i].close()

def main():

    in_file = 'volume(table 6)_training'
    avgVolume(in_file)

if __name__ == '__main__':
    main()



