import numpy as np
import pandas as pd


df = pd.read_csv("ginicsv.csv")
print(df)
allColumns = df.columns
class_name = allColumns[len(allColumns)-1]


def gini_impurity (value_counts):
    n = value_counts.sum()
    p_sum = 0
    for key in value_counts.keys():
        p_sum = p_sum  +  (value_counts[key] / n ) * (value_counts[key] / n )
    gini = 1 - p_sum
    return gini

def gini_split_att(attribute_name):
    attribute_values = df[attribute_name].value_counts()
    gini_A = 0
    for key in attribute_values.keys():
        df_k = df[class_name][df[attribute_name] == key].value_counts()
        n_k = attribute_values[key]
        n = df.shape[0]
        gini_A = gini_A + (( n_k / n) * gini_impurity(df_k))
    return gini_A



giniValues = []
giniMap = {}
for attribute in allColumns:
    if(attribute!=class_name):
      gini = gini_split_att(attribute)
      giniValues.append(gini)
      giniMap[attribute] = gini
      print(f'\nGini for {attribute} is {gini:.3f}')
    else:
        for i in range(2,row+1):
            val=sheet.cell(row=i,column=y).value
            if(val>sel_var):
           
                if(sheet.cell(row=i,column=z).value=="Play"):
                    greater_play+=1
                else:
                    greater_noplay+=1
           
            else:
                if(sheet.cell(row=i,column=z).value=="Play"):
                    lesser_play+=1
                else:
                    lesser_noplay+=1

class_value_counts = df[class_name].value_counts()
gini_class = gini_impurity(class_value_counts)
print(f'\nGini Impurity of the class is {gini_class:.3f}')
min_value = min(giniValues)
selected_attribute = list(giniMap.keys())[list(giniMap.values()).index(min_value)]
print('\nThe minimum value of Gini Impurity : {0:.3} '.format(min_value))
print('\nThe selected attiribute is: ', selected_attribute)
print('\n\n')
