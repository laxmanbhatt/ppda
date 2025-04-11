import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('6mcd.csv')

print(df.head())


df['date'] = pd.to_datetime(df['date'])

sns.set(style="whitegrid") 

plt.figure(figsize=(10, 6))  
sns.lineplot(x='date', y='value', data=df)


plt.title('Trend of the Variable over Time')
plt.xlabel('Date')
plt.ylabel('Value')


plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()
