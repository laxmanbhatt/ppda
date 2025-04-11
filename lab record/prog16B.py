import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('5ds_salaries.csv')


print(df.head())

plt.figure(figsize=(10, 6))  
sns.scatterplot(x='years_experience', y='salary', data=df)


plt.title('Relationship between Years of Experience and Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')

plt.tight_layout()
plt.show()
