import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
from sklearn.metrics.pairwise import pairwise_distances
import sys
import pandas as pd

df = pd.read_csv('single_linkage_csv.csv', sep=',')

data = np.asarray(df)

def find_clusters(input,linkage):
    clusters = {}
    row_index = -1
    col_index = -1
    array = []
    for n in range(input.shape[0]):
        array.append(n)
       
    clusters[0] = array.copy()
    for k in range(1, input.shape[0]):
        min_val = sys.maxsize
       
        for i in range(0, input.shape[0]):
            for j in range(0, input.shape[1]):
                if(input[i][j]<=min_val):
                    min_val = input[i][j]
                    row_index = i
                    col_index = j
                   
       
        #for Single Linkage
        if(linkage == "single" or linkage =="Single"):
            for i in range(0,input.shape[0]):
                if(i != col_index):
                    temp = min(input[col_index][i],input[row_index][i])
                    input[col_index][i] = temp
                    input[i][col_index] = temp
       
                   
        for i in range (0,input.shape[0]):
            input[row_index][i] = sys.maxsize
            input[i][row_index] = sys.maxsize
           
       
        minimum = min(row_index,col_index)
        maximum = max(row_index,col_index)
        for n in range(len(array)):
            if(array[n]==maximum):
                array[n] = minimum
        clusters[k] = array.copy()
       
    return clusters



   
def hierarchical_clustering(data,linkage,no_of_clusters):  
    color = ['r','g','b','y','c','m','k','w']
    initial_distances = pairwise_distances(data,metric='euclidean')
    np.fill_diagonal(initial_distances,sys.maxsize)
    clusters = find_clusters(initial_distances,linkage)
   
    iteration_number = initial_distances.shape[0] - no_of_clusters
    clusters_to_plot = clusters[iteration_number]
    arr = np.unique(clusters_to_plot)
   
    indices_to_plot = []
   
    for x in np.nditer(arr):
        indices_to_plot.append(np.where(clusters_to_plot==x))
    p=0
   
    print(clusters_to_plot)
    for i in range(0,len(indices_to_plot)):
        for j in np.nditer(indices_to_plot[i]):
               ax.scatter(data[j,0],data[j,1], c= color[p])
        p = p + 1

for i in range (2, len(data)):
  hierarchical_clustering(data,"single", i)
Z = linkage(distArray, method = 'single')
dendro = dendrogram(Z)
plt.title('Dendrogram')
plt.ylabel('Euclidean distance')
plt.show()
