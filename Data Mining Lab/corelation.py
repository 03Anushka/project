import pandas as pd
import numpy as np
from numpy import mean
from numpy import std
from matplotlib import pyplot
import matplotlib.pyplot as plt

df = pd.read_csv('corelation.csv', sep=',')

height = df["Height"].to_list()
weight = df["Weight"].to_list()

print('Height: mean=%.3f stdv=%.3f' % (mean(height), std(height)))
print('Weight: mean=%.3f stdv=%.3f' % (mean(weight), std(weight)))

covariance = np.cov(height, weight)
print(covariance)

pyplot.scatter(height, weight)
pyplot.show()
