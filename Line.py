# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:06:10 2023

@author: dpsma
"""


import pandas as pd
import matplotlib.pyplot as plt


# reading from a csv file
gdp_india = pd.read_csv("India_GDP.csv", index_col=0)


def plot_timeseries(axes, x, y, color, label, xlabel, ylabel, loc):
    """ This function plots the line graph by assigning values to the plot,
    x-axis and y-axis labels, ticks and legend"""
    
    
    axes.plot(x, y, color=color , label=label)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', color=color)
    axes.legend(loc=loc)


fig ,ax = plt.subplots()

# function plot_timeseries is called
plot_timeseries(ax, gdp_india['Year'], gdp_india['Gdp'], 'gold',
                'GDP in billion($)', 'Year', 'GDP in billion($)', 'best')

# instantiate a second axis that shares the same x-axis
ax2 = ax.twinx()

# function plot_timeseries is called
plot_timeseries(ax2, gdp_india['Year'], gdp_india['Growth %'], 'blue',
                'Growth %', 'Year', 'Growth %', 'lower center')

# save the plot to a file
plt.savefig('India_GDP.png')
plt.show()



