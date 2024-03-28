#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:27:18 2024

@author: Hasith
"""

import matplotlib.pyplot as plt
import numpy as np

import pandas as pd


staticfire_file = './data/2024StaticFire.eng';

df = pd.read_csv(staticfire_file,skiprows=2,header=None,sep=' ',
                 names=['a','b','time','thrust']);
df.keys = ['a','b','time','thrust']

df = df.drop(columns=['a', 'b'])

# plt.plot(df['time'],df['thrust'])



## get telemega flight data

flight_data = './data/2024-03-23-serial-6606-flight-0005.csv'
df1 = pd.read_csv(flight_data)


plt.figure(2)

plt.subplot(211)
plt.plot(df1['time'],df1['altitude']-df1['altitude'][0])





## load APRS export data from the simulation (from Ben and Rex)

sim_data = './data/aprsExport2.csv'

# data format
# Time (s),Altitude (ft),Vertical velocity (mph),Vertical acceleration (G)

df2 = pd.read_csv(sim_data,comment='#',names=['time','alt','vel','acc_g'])

df2['alt_m'] = df2['alt']*0.3048;


plt.plot(df2['time'],df2['alt_m'],'-')

plt.ylabel('altitude (m)')
plt.xlabel('time (s)')
plt.xlim([0,30])

plt.legend(['KS flight','Sim from Ben/Rex 28/02'])

plt.axvspan(0, 9, color='red', alpha=0.1)


plt.subplot(212)
plt.plot(df1['time'],df1['accel_x'])

#sim data
plt.plot(df2['time'],df2['acc_g']*9.8,'-')

plt.plot([0,30],[0,0],'k:')
plt.xlim([0,30])

plt.ylabel('$acc_x$ ($ms^{-2}$)')
plt.xlabel('time (s)')


## find burn out time

acc_x = np.array(df1['accel_x'])

indx = np.argmin(np.abs(acc_x));
print(f'burnout: {df1["time"][indx]}s')



