import pandas as pd
import seaborn as sns
import madplotlip.pyplot as plt
df=pd.read_csv("salaries.csv")
numeric_df=df.select_dtypes(include=['float 64', 'int 64'])
sns.pairplot(numeric_df)
plt.suptile("pairplot for numrerical columns in salaries.csv", y=1.02)
plt.tight_layout()
plt.show()
