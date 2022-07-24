import pandas as pd
import matplotlib.pyplot as plt
import HelperFunctions as hf


liver_doc = pd.read_csv(r"C:\Users\jjjohnson\Documents\LiverCSV\liver_data.csv", low_memory=False, index_col=0)
barGraph = liver_doc['WGT_KG_TCR'].hist(bins=100)
barGraph.plot(kind='bar')
print(hf.GetModeValue(liver_doc['WGT_KG_TCR'], 100))
plt.show()