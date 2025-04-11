import pandas as pd  
import matplotlib.pyplot as plt 


df = pd.read_csv("2Salary.csv")  


print("Dataset:")
print(df)

experience_mean = df['YearsExperience'].mean()
experience_median = df['YearsExperience'].median()
experience_std = df['YearsExperience'].std()

print("\nAnalysis of Employee Experience:")
print(f"Mean Experience: {experience_mean}")
print(f"Median Experience: {experience_median}")
print(f"Standard Deviation of Experience: {experience_std}")

plt.hist(df['YearsExperience'], bins=10, color='skyblue', edgecolor='black')
plt.title('Distribution of Employee Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
