import pandas as pd
import numpy as np


suffix = '.csv'
old_file_arr = ['1_entry_xgb_predict',
                '1_exit_xgb_predict',
                '2_entry_xgb_predict',
                '3_entry_xgb_predict',
                '3_exit_xgb_predict']
submission_file = 'submission_volume'

total =[]
##order_total = []

def convert(old_file):
    old = pd.read_csv(old_file+suffix)
    print old_file+suffix
   
    for i in range(12):
        for j in range(7):
            num = i + j*12
            item = old.iloc[num,1]
            total.append(old.iloc[num,1])
   
   
if __name__ == '__main__':
   
    for i in range(len(old_file_arr)):
        convert(old_file_arr[i])
        
    total = np.array(total,dtype=np.float)

    ix1 = [0,2,4,6,8,1,3,5,7,9]
    
    fw = open('total.csv','w')
    
    for i in range(len(ix1)):
        for j in range(42):
            fw.writelines(str(total[ix1[i]*42 + j])+'\n')
##            order_total.append(total[ix1[i]*42 + j])
    
    fw.close()

##    submission = pd.read_csv(submission_file+suffix)
##    print submission_file+suffix
##
##    submission = submission.drop(['volume'],axis=1)
##    order_total = pd.DataFrame(order_total)
##    print order_total
##    order_total.columns = ['volume']
##    print order_total
##    submission = pd.concat([submission,order_total],axis=1).drop([''],axis=1)
##    
##
##    submission.to_csv(submission_file+suffix)





