import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Chemistry.csv")
#prit(df.tail())
x=df.tail().iloc[:,1]
y=df.tail().iloc[:,2]
print(x,y)

#print (df.isnull().sum())
plt.bar(x,y)
plt.show()
