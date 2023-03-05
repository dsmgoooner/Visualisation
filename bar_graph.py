# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 19:55:49 2023

@author: dpsma
"""

import pandas as pd
import matplotlib.pyplot as plt

# reading from a csv file
medals = pd.read_csv("Medals.csv", index_col=0)

medals_top = medals.iloc[[0, 1, 2, 3, 4], [0, 1, 2]]


def plot_bars(axes, x , y, rotation):
    "This function sets x-axis tick labels,y-axis labels and legend"
    
    
    axes.set_xticklabels(x, rotation = rotation)
    axes.set_ylabel(y)
    axes.legend()
   
fig, ax = plt.subplots()
ax.bar(medals_top.index, medals_top['Gold Medal'], label = 'Gold')
ax.bar(medals_top.index, medals_top['Silver Medal'],
       bottom = medals_top['Gold Medal'], label = "Silver")
ax.bar(medals_top.index, medals_top['Bronze Medal'],
       bottom=medals_top['Gold Medal'] + medals_top['Silver Medal'],
       label = "Bronze")

# function plot_bars is called
plot_bars(ax, medals_top.index, "Number of medals", 60)

# save the plot to a file
plt.savefig('Medals.png')
plt.show()

