
import pandas as pd  

df = pd.read_csv("2Salary.csv") 


print("Dataset:")
print(df)

mean_salary = df['Salary'].mean()
median_salary = df['Salary'].median()

print("\nCentral Tendencies:")
print(f"Mean Salary: {mean_salary}")
print(f"Median Salary: {median_salary}")

variance_salary = df['Salary'].var()
std_dev_salary = df['Salary'].std()

print("\nDispersion Measures:")
print(f"Variance of Salary: {variance_salary}")
print(f"Standard Deviation of Salary: {std_dev_salary}")
