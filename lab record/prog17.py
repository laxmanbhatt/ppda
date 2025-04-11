import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('5ds_salaries.csv')

print(df.head())


plt.figure(figsize=(10, 6)) 
sns.barplot(x='job_title', y='salary', data=df)


plt.title('Average Salary by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Average Salary')

plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.show()
