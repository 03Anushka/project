import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
dataframe1 = pd.read_excel('fivenum.xlsx')
array = dataframe1['Marks']
min = array[0]
max = array[0]
for x in array:
   if(x<min):
       min = x
for x in array:
   if(x>max):
       max = x
in_arr = np.array(array)
in_arr.sort()
n = len(in_arr)
if n % 2 == 0:
   median1 = in_arr[n//2]
   median2 = in_arr[n//2 - 1]
   median = (median1 + median2)/2
else:
   median = in_arr[n//2]
meansum = sum(in_arr)
mean = meansum//n
q1=0
q2=0
if n % 2 == 0:
   q1Array = in_arr[0:n//2]
   q2Array = in_arr[n//2+1:]
else:
   q1Array = in_arr[0:n//2]
   q2Array = in_arr[n//2+2:]
k = len(q1Array)
if k % 2 == 0:
   q1m = q1Array[k//2]
   q1n = q1Array[k//2 - 1]
   q1 = (q1m + q1n)/2
else:
   q1 = q1Array[k//2]
l = len(q2Array)
if l % 2 == 0:
   q2m = q2Array[l//2]
   q2n = q2Array[l//2 - 1]
   q2 = (q2m + q2n)/2
else:
   q2= q2Array[l//2]
interquartile = q2-q1
lowerwhiskerslength = q1-1.5*interquartile
upperwhiskerslength = q2+1.5*interquartile
print("Lower Whiskers Length: "+ str(lowerwhiskerslength))
print("Min is:" + str(min))
print("Q1 is: " + str(q1))
print("Median is: " + str(median))
print("Q2 is: " + str(q2))
print("Max is: " +str(max))
print("Upper Whiskers Length: " + str(upperwhiskerslength))
plt.boxplot(array)
plt.show()
