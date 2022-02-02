# Import libraries
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from rule1_funct import rule1
from rule2_funct import rule2
from rule3_funct import rule3
from rule4_funct import rule4 #check
from rule5_funct import rule5 #check
from rule6_funct import rule6 #check
from rule7_funct import rule7 #check
from rule8_funct import rule8


# Get data from csv file
#temps_cycle_t = pd.read_csv('test/opc_temp_cycle.csv', delimiter='\t', encoding='utf-16')
temps_cycle_t = pd.read_excel("/home/ikram/Downloads/temps_cycle_test.xlsx")
#temps_cycle_t = pd.read_excel("/home/ikram/Downloads/opc-matelas.xlsx")
# Calculate xBar
xBar = temps_cycle_t['Max'].mean()

# Calculate mRbar
mRiList = []
for index in temps_cycle_t.index:
    if (index > 0):
        mRiList.append(
            abs(temps_cycle_t['Max'][index] - temps_cycle_t['Max'][index - 1]))
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
k=3

print(rule5(k,temps_cycle_t['Max'],temps_cycle_t['Heure et date de mesure']))
#print(rule8(30.76,30.64,temps_cycle_t['Max'],temps_cycle_t['Heure et date de mesure']))


# As we started filling mRiList from index = 1, we delete the first element from time array
time_mr_arr = temps_cycle_t['Heure et date de mesure']
time_mr_arr.drop(index=time_mr_arr.index[0], axis=0, inplace=True)
time_mr_arr.reset_index(drop=True, inplace=True)

# PLot Card X to verify
k_X_ecart_type_arr_u = np.array([(xBar + ecart_type_X) for i in range(temps_cycle_t['Max'].size)])
k_X_ecart_type_arr_l = np.array([(xBar - ecart_type_X) for i in range(temps_cycle_t['Max'].size)])
plt.figure('Test graph X', figsize=(12, 4))
plt.title('Carte X')
plt.scatter(temps_cycle_t['Heure et date de mesure'],temps_cycle_t['Max'],marker=".",s=50,edgecolors="black",c="red",label='mRi_Max')
plt.plot(temps_cycle_t['Heure et date de mesure'], temps_cycle_t['Max'])
plt.plot(temps_cycle_t['Heure et date de mesure'], k_X_ecart_type_arr_u)
plt.plot(temps_cycle_t['Heure et date de mesure'], k_X_ecart_type_arr_l)
plt.legend(['Temps cycle', 'ecart_type (UPPER)', 'ecart_type (LOW)'])

# Plot card mR to verify
k_mR_ecart_type_arr_u = np.array([(mrBar + ecart_type_mR) for i in range(len(mRiList))])
k_mR_ecart_type_arr_l = np.array([(mrBar - ecart_type_mR) for i in range(len(mRiList))])
plt.figure('Test graph mR', figsize=(12, 4))
plt.title('Carte mR')
plt.scatter(time_mr_arr, mRiList,marker=".",s=50,edgecolors="black",c="red",label='mRi_Max')
plt.plot(time_mr_arr, mRiList)
plt.plot(time_mr_arr, k_mR_ecart_type_arr_u)
plt.plot(time_mr_arr, k_mR_ecart_type_arr_l)
plt.legend(['mR Temps cycle', 'ecart_type (UPPER)', 'ecart_type (LOW)'])
plt.show()