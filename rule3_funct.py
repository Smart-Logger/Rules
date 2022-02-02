
# Import libraries
import statistics




    
def rule3(k,arr3_max,arr3_time):    
 # Apply Condition (3)
 # "k points consécutifs, croissants ou décroissants en alternance" 
 
 
 def rule3_acs(k,arr3_max,arr3_time):  
# Apply Condition (3)
 # "k points consécutifs, croissants ou décroissants en alternance"  
 
# Calculate xBar
  xBar = arr3_max.mean()
# Calculate mRbar
 mRiList = []
 for index in arr3_max.index:
    if (index > 0):
        mRiList.append(
            abs(arr3_max[index] - arr3_max[index - 1]))
 mrBar = statistics.mean(mRiList)
 
 while k <= len(arr3_max):
    if((((k+1)<len(arr3_max)) and (arr3_max[k] > arr3_max[k-1]) and (arr3_max[k-1] < arr3_max[k-2])) ):
     return False,arr3_time[k]
    else:
      while k <= len(mRiList):
       if((((k+1)<len(mRiList)) and (mRiList[k] > mRiList[k-1]) and (mRiList[k-1] < mRiList[k-2])) ):
         return False,arr3_time[k]
       else:
         return True
  
    k +=1 
    
       
 def rule3_dec(k,arr3_max,arr3_time):    

 
  while k <= len(arr3_max):
    if((((k+1)<len(arr3_max)) and (arr3_max[k] < arr3_max[k-1]) and (arr3_max[k-1] > arr3_max[k-2])) ):
     return False,arr3_time[k]
       
    else:
        while k <= len(mRiList):
         if((((k+1)<len(mRiList)) and (mRiList[k] < mRiList[k-1]) and (mRiList[k-1] > mRiList[k-2])) ):
           return False,arr3_time[k]
         else:
            return True 
    k +=1 
    
    
 if(rule3_dec(k,arr3_max,arr3_time) or rule3_acs(k,arr3_max,arr3_time)):
     return False,arr3_time[k]
 else:
     return True
    