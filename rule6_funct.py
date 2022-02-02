

# Import libraries
import statistics


def rule6(k,arr6_max,arr6_time): 
# Apply Condition (6)
 # k point consécutifs, dans 1 écart type de la ligne centrale du même côté"  

 def rule6_sup(k,arr6_max,arr6_time):  

 
 # Calculate xBar
  xBar = arr6_max.mean()
# Calculate mRbar
  mRiList = []
  for index in arr6_max.index:
    if (index > 0):
        mRiList.append(
            abs(arr6_max[index] - arr6_max[index - 1]))
  mrBar = statistics.mean(mRiList)
# Our constants
  E2 = 2.66
  D3 = 0
  D4 = 3.267
# LCLx && UCLx
  LCLx = xBar - E2 * mrBar
  UCLx = xBar + E2 * mrBar
# LCLmr && UCLmr
  LCLmr = D3 * mrBar
  UCLmr = D4 * mrBar
# Get ecart_type
  ecart_type_X = (UCLx - LCLx) / 6
  ecart_type_mR = (UCLmr - LCLmr) / 6
   
  j=1
  i=1
  while i< len(arr6_max) :
    if (((arr6_max[i] > xBar) and (arr6_max[i] <  xBar + ecart_type_X))and ((arr6_max[i-1] > xBar) and (arr6_max[i-1] <  xBar + ecart_type_X))):
       j +=1
    else: 
       j=1
    if(j==k):
      print ('k points found',k)  
      j=1
      return False, arr6_time[i]
   
    else:
        if (((mRiList [i] > mrBar) and (mRiList [i] <  mrBar + ecart_type_mR))and ((mRiList [i-1] > mrBar) and (mRiList[i-1] <  mrBar + ecart_type_mR))):
          j +=1
        else: 
          j=1
        if(j==k):
          print ('k points found',k)  
          j=1  
          return False, arr6_time[i]
                      
    i +=1   
    
 def rule6_inf(k,arr6_max,arr6_time):  
 # Calculate xBar
  xBar = arr6_max.mean()
# Calculate mRbar
  mRiList = []
  for index in arr6_max.index:
    if (index > 0):
        mRiList.append(
            abs(arr6_max[index] - arr6_max[index - 1]))
  mrBar = statistics.mean(mRiList)
# Our constants
  E2 = 2.66
  D3 = 0
  D4 = 3.267
# LCLx && UCLx
  LCLx = xBar - E2 * mrBar
  UCLx = xBar + E2 * mrBar
# LCLmr && UCLmr
  LCLmr = D3 * mrBar
  UCLmr = D4 * mrBar
# Get ecart_type
  ecart_type_X = (UCLx - LCLx) / 6
  ecart_type_mR = (UCLmr - LCLmr) / 6 
  j=1
  i=1
  while i< len(arr6_max) :
    if (((arr6_max[i] < xBar) and (arr6_max[i] >  xBar  - ecart_type_X)) and ((arr6_max[i-1] < xBar) and (arr6_max[i-1] >  xBar  - ecart_type_X))) :
       j +=1
    else: 
       j=1
    if(j==k):
      print ('k points found',k)  
      j=1 
      return False, arr6_time[i]
        
    else:
      while i< len(mRiList) :   
        if (((mRiList[i] < mrBar) and (mRiList[i] >  mrBar - ecart_type_mR))and ((mRiList[i-1] < mrBar) and (mRiList[i-1] >  mrBar - ecart_type_mR))):
          j +=1
        else: 
          j=1
        if(j==k):
          print ('k points found',k)  
          j=1        
          return False, arr6_time[i]
        i +=1   
 if(rule6_inf(k,arr6_max,arr6_time) or rule6_sup(k,arr6_max,arr6_time)):
    return False,arr6_time[i]
 else:
    return True    