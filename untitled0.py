# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ySAQe_FMovjRN8GjtWQMHyWsQ0sotSOp
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mtcars.csv')
df

plt.hist(df['mpg'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of MPG')
plt.xlabel('MPG')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.scatter(df['wt'], df['mpg'], color='green')
plt.title('Scatter Plot')
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()

transmission_counts = df['am'].value_counts()
transmission_counts.plot(kind='bar', color='lightblue')
plt.title('Frequency Distribution')
plt.xlabel('Transmission Type (0 = Automatic, 1 = Manual)')
plt.ylabel('Frequency')
plt.xticks(rotation=20)
plt.show()

plt.boxplot(df['mpg'], vert=True)
plt.title('Box and Whisker Plot')
plt.xlabel('MPG')
plt.show()

import pandas as pd
import numpy as np
sr1=([1,2,3,4,5])
sr2=([2,4,6,8,10])
set1=set(sr1)
set2=set(sr2)
inter=set1.intersection(set2)
ans=list(inter)
ans