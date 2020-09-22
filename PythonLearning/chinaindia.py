from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

years = map(str, range(1980, 1984))

df_chinaindia=pd.read_excel(r"C:\Users\natha\Documents\GitHub\firstlocalrepos\PythonLearning\chinaindia.xls")
print(df_chinaindia.head())
#this kind of worked to set my x axis to the first year column
df_chinaindia.set_index('Year').plot(kind='line')
plt.title('Immigration from India and China')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show()
