
# Import libraries
import statistics
  
def rule5(k,arr5_max,arr5_time): 
 # Apply Condition (5)
 # "k sur k+1 points > 1 écarts type à partir de la ligne centrale du même côté "
 
   # Calculate xBar
 xBar = arr5_max.mean()
# Calculate mRbar
 mRiList = []
 for index in arr5_max.index:
    if (index > 0):
        mRiList.append(
            abs(arr5_max[index] - arr5_max[index - 1]))
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
 
 def rule5_inf(k,arr5_max,arr5_time):  
  j=1
  i=0
  while i<len(arr5_max):
    compteur = 0
    nb=0
    while compteur < (k+1) and (i + compteur)<len(arr5_max):
      print('value of ',i+compteur,' is =>',arr5_max[i + compteur],arr5_time[i + compteur])
  #  print("[i+compteur]",[i+compteur] )      
      if(arr5_max[i + compteur] < xBar - ecart_type_X) :
        nb+=1
      compteur +=1
      if(nb==k)and (compteur==k+1): 
       print('x',k,' points found in ', k+1,' sequence <',arr5_time[i+compteur])    
       i=i+k+1
       return False,arr5_time[i+compteur]   
       print(arr5_time[i+compteur])
      
      i+=1
#     else: 
 
#        compteur = 0
#        nb=0
#        while compteur < (k+1) and (i + compteur)<len(mRiList):
#         if( mRiList[i + compteur] < mrBar - ecart_type_mR) :
#           nb+=1
#         compteur +=1
#         if(nb==k)and (compteur==k+1):
#          print('mr',k,' points found in ', k+1,' sequence <')
#         # return False,arr5_time[i+compteur]   
#          i=i+k+1
       
#        # else: 
#         # return True 
 
      

#  def rule5_sup(k,arr5_max,arr5_time): 
#    j=1
#    i=0
#  # Calculate xBar
 
#    while i<len(arr5_max):
#     compteur = 0
#     nb=0
#     while compteur < (k+1) and (i + compteur)<len(arr5_max):
#    # print('value of ',i+compteur,' is ',arr5_max[i + compteur])       
#      if( arr5_max[i + compteur] > xBar + ecart_type_X) :
#       nb+=1
#      compteur +=1
#      if(nb==k)and (compteur==k+1):
#       print('x',k,' points found in ', k+1,' sequence >')
#       i=i+k+1
    
#       return False,arr5_time[i+compteur]   
#      else:
#        compteur = 0
#        nb=0    
#        while compteur < (k+1) and (i + compteur)<len(mRiList):
#         if( mRiList[i + compteur] > mrBar + ecart_type_mR) :
#          nb+=1
#         compteur +=1
#         if(nb==k)and (compteur==k+1):
#          print('mr',k,' points found in ', k+1,' sequence >')
#          i=i+k+1 
#         #return False,arr5_time[i+compteur]    
#      i+=1  
      #  else:
       #   return True 
       
 if(rule5_inf(k,arr5_max,arr5_time)):# or rule5_sup(k,arr5_max,arr5_time)):
   return False   
 else:
   return True