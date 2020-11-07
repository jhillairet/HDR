# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:34:35 2020

@author: JH218595
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%
df = pd.read_csv('Multipaction.csv')
df_dict = {g: d for g, d in df.groupby('PowerMultiplier []')}


#%%
with plt.style.context('seaborn'):
    fig, ax = plt.subplots(figsize=(16, 3.8))
    
    for power in df_dict:
        df_dict[power].plot(x='Time [ns]', y='Particles []', ax=ax, label=np.round(power))
    
    ax.get_legend().remove()
    ax.set_xlabel('Time [ns]', fontsize=14)
    ax.set_ylabel('Number of Electrons', fontsize=14)
    ax.legend(ncol=3, fontsize=10)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.3)
    fig.savefig('chapter_head.png', dpi=150)