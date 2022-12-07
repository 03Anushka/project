import math
import csv
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("distancematrix.csv",sep=",")
x1 = dataframe['X']
y1 = dataframe['Y']

distanceArray = []
centerX = sum(x1)//len(x1)
centerY = sum(y1)//len(y1)
minX = 0
minY = 0

for index, item in enumerate(x1):
 distanceArray.insert(index,((((centerX - x1[index] )**2) + ((centerY-y1[index])**2) )**0.5))
 print("("+str(x1[index])+ ","+str(y1[index])+")"+ "  " + str(distanceArray[index]))

minDistanceFromCenter =  distanceArray[0]

print("Initial Center: "+ "("+ str(centerX)+","+str(centerY)+")")

distanceP1P2 = round(((((x1[0] - x1[1] )**2) + ((y1[0]-y1[1])**2) )**0.5))
distanceP1P3 = round(((((x1[0] - x1[2] )**2) + ((y1[0]-y1[2])**2) )**0.5))
distanceP2P3 = round(((((x1[1] - x1[2] )**2) + ((y1[1]-y1[2])**2) )**0.5))

print("0"+"   " +str(round(distanceP1P2))+ "  "+str(round(distanceP1P3)))
print(str(round(distanceP1P2))+ "  "+ "0" + "   "+str(round(distanceP2P3)))
print(str(round(distanceP1P3))+ "  "+str(round(distanceP2P3))+ "   "+ "0")
print("Minimum Distance from center: " + str(minDistanceFromCenter))
minIndex = 0
for i, item in enumerate(x1):
   minDistanceFromCenter = min(distanceArray[i], minDistanceFromCenter)
   if(minDistanceFromCenter==distanceArray[i]):
       minIndex = i

newCenterX = x1[minIndex]
newCenterY = y1[minIndex]

print("New Center: "+ "(" +str(newCenterX)+ "," +str(newCenterY)+")")

distancesFromNewCenter = []

for index, item in enumerate(x1):
 distancesFromNewCenter.insert(index,round((((newCenterX - x1[index] )**2) + ((newCenterY-y1[index])**2) )**0.5))
 print("("+str(x1[index])+ ","+str(y1[index])+")"+ "  " + str(distancesFromNewCenter[index]))
