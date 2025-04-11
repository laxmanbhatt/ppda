import pandas as pd  


data = [
    {"Product Name": "Laptop", "Category": "Electronics", "Price": 70000},
    {"Product Name": "Smartphone", "Category": "Electronics", "Price": 30000},
    {"Product Name": "Table", "Category": "Furniture", "Price": 15000},
    {"Product Name": "Chair", "Category": "Furniture", "Price": 5000},
]
df = pd.DataFrame(data)

df["Discounted Price"] = df["Price"] * 0.99


print("DataFrame with Discounted Prices:")
print(df)
