# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 08:49:50 2017

@author: JH218595
"""
import matplotlib.pyplot as plt
import pandas as pd
from scipy.constants import m_e, e, pi, c, mu_0
import numpy as np

#%% Pth vs Toroidal field
C3_Pth_vs_By = pd.read_csv('C3_Pth_vs_By_SEY-Spark_1000electrons.csv', delimiter='\t')
C4_Pth_vs_By = pd.read_csv('C4_Pth_vs_By_SEY-Spark_1000electrons.csv', delimiter='\t')

#%% Converting Power Threshold to Electric Field Threshold
# P = 1/4 E^2 k0/(mu0*omega)*a*b
a_C3 = 70e-3
b_C3 = 8e-3
a_C4 = 76e-3
b_C4 = 14.65e-3
f = 3.7e9
omega = 2*pi*f
k0 = omega/c
# Power Threshold without magnetic field
Pth_C3_0 = 25.78*1e3 # W, LH1
Pth_C4_0 = 60.02475*1e3 # W, LH2

def P_2_E(P, a, b):
    return np.sqrt(4*mu_0*omega/(k0*a*b)*P)

C3_Pth_vs_By['Eth'] = C3_Pth_vs_By['Pth'].apply(P_2_E, args=(a_C3, b_C3))
# remove 0s
C3_Pth_vs_By = C3_Pth_vs_By.loc[(C3_Pth_vs_By.Pth!=0)]

C4_Pth_vs_By['Eth'] = C4_Pth_vs_By['Pth'].apply(P_2_E, args=(a_C4, b_C4))

Eth_C3_0 = P_2_E(Pth_C3_0, a_C3, b_C3)
Eth_C4_0 = P_2_E(Pth_C4_0, a_C4, b_C4)

#%% In the dataset, there is few points per magnetic field value.
# Perform the average of each magnetic field value
C4_mean = C4_Pth_vs_By.groupby('By').mean()
C3_mean = C3_Pth_vs_By.groupby('By').mean()
C4_std = C4_Pth_vs_By.groupby('By').std()
C3_std = C3_Pth_vs_By.groupby('By').std()

#%% Plot Power Threshold vs Magnetic field
fig,ax=plt.subplots()
ax.errorbar(x=C3_mean.index, y=C3_mean.Eth/1e3/1e2, 
            yerr=C3_std.Eth/1e3/1e2, 
            fmt='o', ecolor='grey', alpha=0.7, ms=5)
ax.errorbar(x=C4_mean.index, y=C4_mean.Eth/1e3/1e2, 
            yerr=C4_std.Eth/1e3/1e2, 
            fmt='o', ecolor='grey', alpha=0.7, ms=5, color='r')
ax.set_xscale('log')
#ax.set_yscale('log')
ax.set_xlabel('$B_0$ [T]', fontsize=14)
ax.set_ylabel('Multipactor Threshold Power [kV/cm]', fontsize=14)
ax.set_xlim(1e-3, 3)
ax.set_ylim(2,3)
ax.grid(True)
ax.grid(True, which='minor', color='grey', alpha=0.3)
ax.set_title('Multipactor Electric Field Threshold', fontsize=16)
ax.legend(('LH1', 'LH2'))

# average value without magnetic field
ax.axhline(Eth_C3_0/1e3/1e2, color='#84d0ff', ls='--', lw=2, alpha=0.8) # LH1
ax.axhline(Eth_C4_0/1e3/1e2, color='#ff8383', ls='--', lw=2, alpha=0.8) # LH2

# shows the cyclotron resonance magnetic field at 3.7 GHz
B_ec = 2*pi*m_e/ e * 3.7e9
ax.axvline(B_ec, color='#44823a', ls='-.', lw=2, alpha=0.8)

plt.tight_layout()

##%% Multipactor Order vs Toroidal field
## In the dataset, there is few points per magnetic field value.
## Perform the average of each magnetic field value
#
#fig,ax=plt.subplots()
#ax.errorbar(x=C3_mean.index, y=C3_mean['Multipactor Order'], 
#            yerr=C3_std['Multipactor Order'], 
#            fmt='o', ecolor='grey', alpha=0.7, ms=5)
#ax.errorbar(x=C4_mean.index, y=C4_mean['Multipactor Order'], 
#            yerr=C4_std['Multipactor Order'], 
#            fmt='o', ecolor='grey', alpha=0.7, ms=5, color='r')
#ax.set_xscale('log')
##ax.set_yscale('log')
#ax.set_xlabel('By [T]', fontsize=14)
#ax.set_ylabel('Multipactor Threshold Power [kW]', fontsize=14)
#ax.set_xlim(1e-3, 3)
#ax.set_ylim(0,60)
#ax.grid(True)
#ax.grid(True, which='minor', color='grey', alpha=0.3)
#ax.set_title('Multipactor Order', fontsize=16)
#ax.legend(('LH1', 'LH2'))
#plt.tight_layout()