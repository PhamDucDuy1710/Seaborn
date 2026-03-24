import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 


df = pd.read_csv('cereal.csv') 
print(df.head())


fields = ['shelf','weight','cups','rating'] 
cereal_df = df.drop(fields, axis = 1) 
print(cereal_df.head())

cereal_corr = cereal_df.corr(numeric_only = True) # numeric_only : loại bỏ dữ liệu string cho hàm corr() trong py
print(cereal_corr)

ones_corr = np.ones_like(cereal_corr, dtype = bool) 
print(ones_corr)  

mask = np.triu(ones_corr) # triu() return only upper triangle matrixx 
print(mask) 


adjusted_mask = mask[1:,:-1] 
print(adjusted_mask)
adjusted_cereal_corr = cereal_corr.iloc[1:, :-1]
print(adjusted_cereal_corr)
fig, ax = plt.subplots(figsize = (10,8))
sns.heatmap(data = adjusted_cereal_corr, mask = adjusted_mask, annot = True,fmt = '.2f',cmap = 'Blues',vmin = -1, vmax = 1, linecolor = 'white', linewidths = 0.5)
yticks = [i.upper() for i in adjusted_cereal_corr.index]
xticks = [i.upper() for i in adjusted_cereal_corr.columns]
ax.set_yticklabels(yticks, rotation = 0, fontsize = 13)
ax.set_xticklabels(xticks, rotation = 0, fontsize = 13)
title = 'CORRELATION MATRIX\nSAMPLED CEREAL COMPOSITION\n'
ax.set_title(title, loc = 'left', fontsize = 18)
plt.show()