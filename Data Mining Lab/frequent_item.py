import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

## Use this to read data directly from github
df = pd.read_csv('frequentitem.csv', sep=',')

df.head(10)

items = set()
for col in df:
    items.update(df[col].unique())
print(items)
itemset = set(items)
encoded_vals = []
for index, row in df.iterrows():
    rowset = set(row)
    labels = {}
    uncommons = list(itemset - rowset)
    commons = list(itemset.intersection(rowset))
    for uc in uncommons:
        labels[uc] = 0
    for com in commons:
        labels[com] = 1
    encoded_vals.append(labels)
encoded_vals[0]
ohe_df = pd.DataFrame(encoded_vals)
freq_items = apriori(ohe_df, min_support=0.2, use_colnames=True, verbose=1)
print(freq_items.head(10))
rules = association_rules(freq_items, metric="confidence", min_threshold=0.6)

print(rules.head(10)[["antecedents", "consequents", "support", "confidence"]])

plt.scatter(rules['support'], rules['confidence'], alpha=0.5)
plt.xlabel('support')
plt.ylabel('confidence')
plt.title('Support vs Confidence')
plt.show()

