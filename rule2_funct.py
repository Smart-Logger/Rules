
# Import libraries
import statistics

def rule2(k,arr2_max,arr2_time):    
 # Apply Condition (2)
 # "k points consécutifs, tous croissants ou tous décroissants"
    
 def rule2_acsending(k,arr2_max,arr2_time):    
 
    xBar = arr2_max.mean()
   # Calculate mRbar
    mRiList = []
    for index in arr2_max.index:
     if (index > 0):
      mRiList.append(
            abs(arr2_max[index] - arr2_max[index - 1]))
    mrBar = statistics.mean(mRiList)
    j=1
    i=1
    while i<len(arr2_max):
     if(arr2_max[i] < arr2_max[i-1]):
      j +=1
     else: 
      j=1
     if(j==k):
      #print ('k points found',k)  
      j=1
      return False,arr2_time[i] 
     else:
      mRiList = []
      for index in arr2_max.index:
       if (index > 0):
        mRiList.append(
            abs(arr2_max[index] - arr2_max[index - 1]))
      mrBar = statistics.mean(mRiList)    
      while i<len(mRiList):
       if(mRiList[i] > mRiList[i-1]):
        j +=1   
       else: 
        j=1
       if(j==k):
        #print ('k points found',k)
        j=1
        return False,arr2_time[i] 
     i +=1
 
  
 def rule2_decsending(k,arr2_max,arr2_time):    
 
  xBar = arr2_max.mean()
# Calculate mRbar
 
 j=1
 i=1
 while i<len(arr2_max):
  if(arr2_max[i] > arr2_max[i-1]):
    j +=1   
  else: 
    j=1
  if(j==k):
    #print ('k points found',k)
    j=1
    return False,arr2_time[i] 
  
  else:
    mRiList = []
    for index in arr2_max.index:
      if (index > 0):
        mRiList.append(
            abs(arr2_max[index] - arr2_max[index - 1]))
    mrBar = statistics.mean(mRiList)    
    while i<len(mRiList):
      if(mRiList[i] > mRiList[i-1]):
       j +=1   
      else: 
       j=1
      if(j==k):
        #print ('k points found',k)
        j=1
        return False,arr2_time[i] 
  i +=1
  
 if(rule2_decsending(k,arr2_max,arr2_time) or rule2_acsending(k,arr2_max,arr2_time)):
     return False,arr2_time[i] 
 else:
     return True
 