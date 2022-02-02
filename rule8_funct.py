
# Import libraries
import statistics

def rule8(max_t,min_t,arr8_value,arr8_time):    
 # Apply Condition (8)
 # 1 point au delà des limites de tolérance"     
 
# Calculate xBar
 xBar = arr8_value.mean()
# Calculate mRbar
 mRiList = []
 for index in arr8_value.index:
    if (index > 0):
        mRiList.append(
            abs(arr8_value[index] - arr8_value[index - 1]))
 mrBar = statistics.mean(mRiList)
 controlX_1 = True
 for index in arr8_value.index:
    if arr8_value[index] > max_t or arr8_value[index] < min_t:
        controlX_1 = False  
        return False, arr8_time[index]
 if controlX_1 == True:
        controlX_1 = True
        for index,mri in enumerate(mRiList):
         if mRiList[index] > max_t or mRiList[index] < min_t:
          controlX_1 = False     
          return False, arr8_time[index]
        if controlX_1 == True:
          return True
