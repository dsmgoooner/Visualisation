# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 21:34:12 2023

@author: dpsma
"""

import pandas as pd
import matplotlib.pyplot as plt

# reading from a csv file
df_happ = pd.read_csv("Happiness Report.csv", index_col=0)

def generate_scatter_plot(df, x_label, y_label, title, filename):
    """ This function sets the plot, x-axis and y-axis labels,
    title, add text annotation, grid, legend and plots the graph"""
    
    
    plt.figure()
    plt.scatter(df[x_label], df[y_label], label='Countries')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    
    # add text annotations for specific data points
    text_annots = {'Finland': (1.892, 7.821), 'Afghanistan': (0.758, 2.404)}
    for label, coords in text_annots.items():
        plt.text(coords[0], coords[1], label)
    
    plt.grid(True)
    plt.legend()
    
    # save the plot to a file
    plt.savefig(filename)
    plt.show()
    
    
# function generate_scatter_plot is called
generate_scatter_plot(df_happ, ' GDP per capita', 'Happiness score', 
                      'World Happiness Report 2022', 'Happiness_Report.png')
