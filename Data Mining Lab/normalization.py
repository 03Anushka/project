import numpy as np
import math
import pandas as pd
 
dataframe1 = pd.read_excel('normalization.xlsx')
array = dataframe1['Marks']
min = array[0]
max = array[0]
for x in array:
   if(x<min):
       min = x
for x in array:
   if(x>max):
       max = x
 
diff = max - min
in_arr = np.array(array)
in_arr.sort()
n = len(in_arr)
minmaxArray = {}
for index, item in enumerate(array):
    minmaxArray[index] = (item-min)/diff
print("Min Max Transformation: ")
for i, x in enumerate(array):
    print(str(x)+ " : " + str(minmaxArray[i]))
    meansum = sum(in_arr)
mean = meansum/n
deviations = [(x - mean) ** 2 for x in array]
variance = sum(deviations) / n
std_dev = math.sqrt(variance)
 
print("Standard Deviation of the sample is % s "% (std_dev))
print("Mean of the sample is % s " % (mean))
 
zscores = {}
for index, item in enumerate(array):
    zscores[index] = (item-mean)/std_dev
print("Z-score Transformation: ")
for i, x in enumerate(array):
    print(str(x)+ " : " + str(zscores[i]))
