#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 11:49:44 2018

@author: jorge.gomez
"""


import matplotlib.pyplot as plt
import pandas as pd

#Defines data file and brings in csv file
mouse_data='180510_Diazepam_ZeroMaze_c57mice - Test 1.csv'
data_file = pd.read_csv(mouse_data)

#Define how the mouse should be tracked
positionX=str(input('Type in how you want to track the mouse? Centre, Head or Tail: ')) + ' '
positionY=positionX

time = data_file['Time']
x = data_file[positionX+ 'position X']
y = data_file[positionY+ 'position Y']

#Defining the thickness of the line
thickness=input("How thick should the line be? ")
#defining what color the line should be
line_color=input("What color should the line be? ")
plt.plot(x, y, color = line_color, linewidth=thickness)

## Add title and axis names
plt.title('Zero maze')
plt.xlabel('')
plt.ylabel('')
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

#prints out a PDF file
plt.savefig('mouse_data_tracked_by' + '_' + positionX + '.pdf')
