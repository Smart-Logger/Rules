# Import libraries
import statistics     

def rule4(k,arr4_max,arr4_time): 
 # Apply Condition (4)
 # "k sur k+1 points > 2 écarts types à partir de la ligne centrale du même côté"  
 def rule4_sup(k,arr4_max,arr4_time): 

  
 # Calculate xBar
  xBar = arr4_max.mean()
# Calculate mRbar
  mRiList = []
  for index in arr4_max.index:
    if (index > 0):
        mRiList.append(
            abs(arr4_max[index] - arr4_max[index - 1]))
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
  i=0 
  for i in range((len(arr4_max))-(k+1)) :
   compteur = 0
   nb=0
   while compteur < (k+1):
    if(arr4_max[i + compteur] > xBar  + ecart_type_X * 2) :
      nb+=1
    compteur +=1
    if(nb==k)and (compteur==k+1):
     print(k,' points found in ', k+1,' sequence')
     return False,arr4_time[i + compteur]
   
    else:    
      for i in range((len(mRiList))-(k+1)) :
       compteur = 0
       nb=0
       while compteur < (k+1):
        if(mRiList[i + compteur] > mrBar  + ecart_type_mR * 2) :
          nb+=1
        compteur +=1
        if(nb==k)and (compteur==k+1):
         print(k,' points found in ', k+1,' sequence')
         return False,arr4_time[i + compteur]
        else:
         return True
       
 def rule4_inf(k,arr4_max,arr4_time):
    
  # Calculate xBar
  xBar = arr4_max.mean()
# Calculate mRbar
  mRiList = []
  for index in arr4_max.index:
    if (index > 0):
        mRiList.append(
            abs(arr4_max[index] - arr4_max[index - 1]))
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
  i=0 
  for i in range((len(arr4_max))-(k+1)) :
   compteur = 0
   nb=0
   while compteur < (k+1):
    if(arr4_max[i + compteur] < xBar  - ecart_type_X * 2):
      nb+=1
    compteur +=1
    print("nb",nb)
    if(nb==k)and (compteur==k+1):
     print(k,' points found in ', k+1,' sequence')   
     return False,arr4_time[i + compteur]   
    else:  
      i=0 
      for i in range((len(mRiList))-(k+1)):
       compteur = 0
       nb=0
       while compteur < (k+1):
        if(mRiList[i + compteur] < mrBar  - ecart_type_mR * 2):
          nb+=1
        compteur +=1
        if(nb==k)and (compteur==k+1):
          print(k,' points found in ', k+1,' sequence')
          return False,arr4_time[i + compteur]
       # else:
        #     return True

 if(rule4_inf(k,arr4_max,arr4_time) or rule4_sup(k,arr4_max,arr4_time)):
   return False,arr4_time[i + compteur]
 else:
   return True