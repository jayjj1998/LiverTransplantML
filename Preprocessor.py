
import csv
import pandas as pd
import matplotlib.pyplot as plt


def normalize(df):
    result = df.copy()
    max_value = df.max()
    min_value = df.min()
    result = (df - min_value) / (max_value - min_value)
    return result


liverDoc = pd.read_csv(r"C:\Users\jraiti\Documents\liver_data.csv")
liverDoc['NUM_PREV_TX'] = normalize(liverDoc['NUM_PREV_TX'])
barGraph = liverDoc['NUM_PREV_TX'].value_counts()
barGraph.plot(kind='bar')
print(liverDoc['NUM_PREV_TX'].isna().sum())
plt.show()

normBarGraph = normalize(liverDoc['NUM_PREV_TX']).value_counts().plot(kind='bar')
plt.show()
