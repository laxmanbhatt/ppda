import pandas as pd
import seaborn as sns
import martplotlip.pyplot as plt
df=pd.read.csv("salaries.csv")
sns.set(style="whitegrid:")
plt.figure(figsize=(10,6))
sns.listplot(df["salary_in_usd"].kde=true,colour="skyblue": bins=30)
plt.title("distribution of salary",fontsize=16)
plt.xlabel("salary")
plt.ylabel("frequency")
plt.tight_layout()
plt.show()
