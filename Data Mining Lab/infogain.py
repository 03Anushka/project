import numpy as np
import math
import pandas as pd

dataframe1 = pd.read_csv('info.csv', sep=',')

gender = dataframe1['Gender']
wealth = dataframe1['Wealth']
age = dataframe1['Age']
yesno = dataframe1['House']

def calc_entropy(column):
    """
    Calculate entropy given a pandas series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column
    counts = np.bincount(column)
    # Divide by the total column length to get a probability
    probabilities = counts / len(column)
   
    # Initialize the entropy to 0
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy
    for prob in probabilities:
        if prob > 0:
            # use log from math and set base to 2
            entropy += prob * math.log(prob, 2)
   
    return -entropy
genderarray = {}
wealtharray = {}
agearray = {}
dataarray = {}

for index, item in enumerate(gender):
    if(gender[index]=="Male"):
        genderarray[index]=1
   
    if(gender[index]=="Female"):
        genderarray[index]=2

   
for index, item in enumerate(wealth):
    if(wealth[index]=="Rich"):
        wealtharray[index]=1
   
    if(wealth[index]=="Poor"):
        wealtharray[index]=2

for index, item in enumerate(age):
    if(wealth[index]=="Elderly"):
        wealtharray[index]=1
   
    if(wealth[index]=="Adult"):
        wealtharray[index]=2

    if(wealth[index]=="Teenage"):
        wealtharray[index]=3


for index, item in enumerate(yesno):
    if(yesno[index]=="Yes"):
        dataarray[index]=1
   
    if(yesno[index]=="No"):
        dataarray[index]=2

   

entropyOfgender = calc_entropy(pd.Series(genderarray))

entropyOfwealth = calc_entropy(pd.Series(wealtharray))
entropyOfData = calc_entropy(pd.Series(dataarray))

print("Total Entropy: %s " % (entropyOfData))
print("Entropy of wealth: %s " % (entropyOfwealth))
print("Entropy of gender: %s " % (entropyOfgender))

print("Info Gain for wealth: %s " % (entropyOfData-entropyOfwealth))
print("Info Gain for gender: %s " % (entropyOfData-entropyOfgender))

