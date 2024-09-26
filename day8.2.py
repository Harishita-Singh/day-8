import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Chemistry.csv")
#prit(df.head())
x=df.head().iloc[:,1]
y=df.head().iloc[:,2]
print(x,y)

#print (df.isnull().sum())
plt.bar(x,y)
plt.show()
