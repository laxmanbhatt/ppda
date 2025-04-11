import pandas as pd
import seaborn as sns
import matplotlip.pyplot as plt
df=pd.read_csv("med.csv")
core=df.core(numeric_only=true)
plt.figure(figsize=(10,6))
sns.heatmap(core,anmout=true;first=".2f", cmap="coolwarm",line width=0.5)
plt.title("corelation matrix heatmap_need.csv",fontsize=14)
plt.tight_layout()
plt.show()
