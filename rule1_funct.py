import statistics

def rule1(k,arr1_max,arr1_time):    
 # Apply Condition (1)
 # "un point > k écarts types à partir de la ligne centrale"
 
 # Calculate xBar
 xBar = arr1_max.mean()
# Calculate mRbar
 mRiList = []
 for index in arr1_max.index:
    if (index > 0):
        mRiList.append(
            abs(arr1_max[index] - arr1_max[index - 1]))
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
 controlX_1 = True
 for index in arr1_max.index:
    if arr1_max[index] > (xBar + k * ecart_type_X) or arr1_max[index] < (xBar - k * ecart_type_X):
        controlX_1 = False 
        return False, arr1_time[index]
       
 if controlX_1 == True:
        controlX_1 = True
        for index,mri in enumerate(mRiList):
         if mRiList[index] > (mrBar + k * ecart_type_mR) or mRiList[index] < (mrBar - k * ecart_type_mR):
          controlX_1 = False    
          return False, arr1_time[index]
        if controlX_1 == True:
         return True
