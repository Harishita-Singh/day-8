import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Physics.csv")
#print(df.tail())
x=df.iloc[:,1]
y=df.iloc[:,2]
print(x,y)

#print(df.isnull().sum())
plt.bar(x,y)
plt.show()
