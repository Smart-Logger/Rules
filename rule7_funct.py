# Import libraries
import statistics



     
def rule7(k,arr7_value,arr7_time):
 # Apply Condition (7)
 # k point consécutifs > 1 écart type à partir de la ligne centrale de la même côté"    
 
 
 
 def rule7_inf(k,arr7_value,arr7_time):
     # Apply Condition (7)
 # k point consécutifs > 1 écart type à partir de la ligne centrale de la même côté"     
  j=1
  i=1
 
 # Calculate xBar
  xBar = arr7_value.mean()
# Calculate mRbar
  mRiList = []
  for index in arr7_value.index:
    if (index > 0):
        mRiList.append(
            abs(arr7_value[index] - arr7_value[index - 1]))
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
  while i< len(arr7_value) :
    if ((arr7_value[i] <  xBar  - ecart_type_X) and (arr7_value[i-1] < xBar  - ecart_type_X)):
       j +=1
    else: 
       j=1
    if(j==k):
      print ('k points found',k) 
      j=1 
      return False, arr7_time[i]
    else:
      if ((mRiList[i] <  mrBar  - ecart_type_mR) and ( mRiList[i-1] < mrBar  - ecart_type_mR)):
        j +=1
      else: 
       j=1
      if(j==k):
       print ('k points found',k)  
       j=1  
       return False, arr7_time[i]  
    i +=1     
    
    
    
 def rule7_sup(k,arr7_value,arr7_time):
 # Apply Condition (7)
 # k point consécutifs > 1 écart type à partir de la ligne centrale de la même côté"      
  j=1
  i=1
 
 # Calculate xBar
  xBar = arr7_value.mean()
# Calculate mRbar
  mRiList = []
  for index in arr7_value.index:
    if (index > 0):
        mRiList.append(
            abs(arr7_value[index] - arr7_value[index - 1]))
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
  while i< len(arr7_value) :
    if ((arr7_value[i] > xBar  + ecart_type_X) and (arr7_value[i-1] > xBar  + ecart_type_X)):
       j +=1
    else: 
       j=1
    if(j==k):
      print ('k points found',k)  
      j=1
      return False,arr7_time[i]
    else:
      if ((mRiList[i] > mrBar  + ecart_type_mR) and (mRiList[i-1] > mrBar  + ecart_type_mR)):
           j +=1
      else: 
       j=1
      if(j==k):
       print ('k points found',k)  
       return False,arr7_time[i]
      j=1  
    i +=1       
 
 if(rule7_sup(k,arr7_value,arr7_time) or rule7_inf(k,arr7_value,arr7_time)): 
     return False,arr7_time[i]
 else:
     return True
     